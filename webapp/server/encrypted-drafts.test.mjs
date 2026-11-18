import test from 'node:test';
import assert from 'node:assert/strict';
import { webcrypto, randomBytes } from 'node:crypto';
import { createEncryptedDraftStore, privateDraftPrefix, DRAFT_TTL_MS } from '../shared/encrypted-drafts.mjs';
class Storage {
  map=new Map();get length(){return this.map.size;}key(i){return [...this.map.keys()][i]||null;}
  getItem(k){return this.map.get(k)??null;}setItem(k,v){this.map.set(k,v);}removeItem(k){this.map.delete(k);}
}
const credential=(userId='owner')=>({userId,keyId:randomBytes(16).toString('hex'),key:randomBytes(32).toString('base64')});
const fixture=(overrides={})=>{const storage=new Storage(),k=credential();return {storage,k,store:createEncryptedDraftStore({userId:k.userId,storage,loadKey:async()=>k,crypto:webcrypto,...overrides})};};

test('private text and key material never enter persistent storage; an authenticated refresh restores exact drafts and uses fresh nonces',async()=>{
  const {storage,k,store}=fixture(),draft={writing:'가상 학생의 비공개 설명',pending:[{id:'q1',choice:0,seq:1}],request:{mutationId:'retry-original'}};
  await store.set('lesson-1',draft);const first=JSON.parse(storage.getItem(privateDraftPrefix('owner')+'lesson-1'));
  assert.equal(JSON.stringify([...storage.map]).includes(draft.writing),false);assert.equal(JSON.stringify([...storage.map]).includes(k.key),false);assert.equal(JSON.stringify([...storage.map]).includes('mutationId'),false);
  const refreshed=createEncryptedDraftStore({userId:'owner',storage,loadKey:async()=>k,crypto:webcrypto});assert.deepEqual(await refreshed.get('lesson-1'),draft);
  await store.set('lesson-1',draft);const next=JSON.parse(storage.getItem(privateDraftPrefix('owner')+'lesson-1'));assert.notEqual(first.nonce,next.nonce);assert.notEqual(first.ciphertext,next.ciphertext);
});

test('moving ciphertext across records or accounts, changing expiry, and altering ciphertext all fail authenticated decryption',async()=>{
  const {storage,k,store}=fixture(),originalKey=privateDraftPrefix('owner')+'run-1';await store.set('run-1',{writing:'가상 비공개 답'});const raw=storage.getItem(originalKey);
  storage.setItem(privateDraftPrefix('owner')+'run-2',raw);await assert.rejects(store.get('run-2'),e=>e.code==='AUTHENTICATION_FAILED');
  const changed=JSON.parse(raw);changed.expiresAt+=60000;storage.setItem(originalKey,JSON.stringify(changed));await assert.rejects(store.get('run-1'),e=>e.code==='AUTHENTICATION_FAILED');
  changed.expiresAt-=60000;changed.ciphertext=(changed.ciphertext[0]==='A'?'B':'A')+changed.ciphertext.slice(1);storage.setItem(originalKey,JSON.stringify(changed));await assert.rejects(store.get('run-1'),e=>e.code==='AUTHENTICATION_FAILED');
  storage.setItem(privateDraftPrefix('other')+'run-1',raw);const otherKey=credential('other'),other=createEncryptedDraftStore({userId:'other',storage,loadKey:async()=>otherKey,crypto:webcrypto});await assert.rejects(other.get('run-1'),e=>e.code==='KEY_CHANGED');
  const wrongAccount=createEncryptedDraftStore({userId:'owner',storage,loadKey:async()=>({...k,userId:'other'}),crypto:webcrypto});await assert.rejects(wrongAccount.get('run-2'),e=>e.code==='WRONG_ACCOUNT');
});

test('expired drafts are removed, key changes cannot read old drafts, and storage or crypto failures never store plaintext',async()=>{
  let at=1000;const {storage,k,store}=fixture({now:()=>at});await store.set('run',{writing:'검사용 초안'});at+=DRAFT_TTL_MS;assert.equal(await store.get('run'),null);assert.equal(storage.length,0);
  await store.set('run',{writing:'다음 초안'});const reset=createEncryptedDraftStore({userId:'owner',storage,loadKey:async()=>credential(),crypto:webcrypto,now:()=>at});await assert.rejects(reset.get('run'),e=>e.code==='KEY_CHANGED');
  const noCrypto=fixture({crypto:{}});await assert.rejects(noCrypto.store.set('run',{writing:'저장 금지'}),e=>e.code==='CRYPTO_UNAVAILABLE');assert.equal(noCrypto.storage.length,0);
  const blocked=new Storage();blocked.setItem=()=>{throw new Error('quota unavailable');};const failStore=createEncryptedDraftStore({userId:'owner',storage:blocked,loadKey:async()=>k,crypto:webcrypto});await assert.rejects(failStore.set('run',{writing:'평문 대체 금지'}),/quota/);assert.equal(blocked.length,0);
});

test('write queues preserve newest input, snapshot before async work, and remove waits for prior encryption',async()=>{
  let release;const ready=new Promise(r=>{release=r;});const k=credential(),storage=new Storage();const store=createEncryptedDraftStore({userId:'owner',storage,loadKey:async()=>{await ready;return k;},crypto:webcrypto});
  const draft={writing:'처음'};const first=store.set('run',draft);draft.writing='외부에서 수정';release();await first;assert.equal((await store.get('run')).writing,'처음');
  const a=store.set('run',{writing:'이전'}),b=store.set('run',{writing:'최신'});await Promise.all([a,b]);assert.equal((await store.get('run')).writing,'최신');
  const c=store.set('run',{writing:'삭제 대기'}),remove=store.remove('run');await Promise.all([c,remove]);assert.equal(await store.get('run'),null);
});

test('logout during key retrieval invalidates pending writes and reads without recreating the cache',async()=>{
  let release,started;const ready=new Promise(r=>{release=r;}),begun=new Promise(r=>{started=r;}),k=credential(),storage=new Storage();const store=createEncryptedDraftStore({userId:'owner',storage,loadKey:async()=>{started();await ready;return k;},crypto:webcrypto});
  const write=store.set('run',{writing:'로그아웃 후 저장 금지'});await begun;store.clear();release();await assert.rejects(write,e=>e.code==='CLEARED');assert.equal(storage.length,0);
  await store.set('run',{writing:'재로그인 가상 자료'});assert.equal((await store.get('run')).writing,'재로그인 가상 자료');store.clear();assert.equal(await store.get('run'),null);
});

test('session lock forgets keys while retaining ciphertext for authenticated recovery; explicit clear deletes it',async()=>{
  const storage=new Storage(),k=credential();let authorized=true,loads=0;const loadKey=async()=>{loads++;if(!authorized)throw Object.assign(new Error('authentication required'),{status:401});return k;};
  const store=createEncryptedDraftStore({userId:'owner',storage,loadKey,crypto:webcrypto});await store.set('run',{writing:'재인증 복구 검사'});store.forget();authorized=false;await assert.rejects(store.get('run'),e=>e.status===401);assert.equal(storage.length,1);
  authorized=true;assert.equal((await store.get('run')).writing,'재인증 복구 검사');assert.equal(loads,3);store.clear();assert.equal(storage.length,0);
});
