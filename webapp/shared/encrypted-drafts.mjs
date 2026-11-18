export const PRIVATE_DRAFT_PREFIX = 'readx-private-draft:v1:';
export const DRAFT_TTL_MS = 12 * 3600000;
const error = (code, message) => Object.assign(new Error(message), { code });
const bytes = value => Uint8Array.from(atob(value), c => c.charCodeAt(0));
const base64 = value => {
  const data = new Uint8Array(value); let binary = '';
  for (let i=0;i<data.length;i+=32768) binary += String.fromCharCode(...data.subarray(i,i+32768));
  return btoa(binary);
};
const entries = storage => Array.from({length:storage.length},(_,i)=>storage.key(i)).filter(Boolean);
export const privateDraftPrefix = userId => PRIVATE_DRAFT_PREFIX+encodeURIComponent(userId)+':';

// Only ciphertext is persisted. The authenticated key loader and CryptoKey stay
// in memory. This cannot protect an unlocked session from malicious same-origin JS.
export function createEncryptedDraftStore({ userId, storage, loadKey, crypto = globalThis.crypto, now = Date.now, ttlMs = DRAFT_TTL_MS }) {
  const prefix=privateDraftPrefix(userId), encoder=new TextEncoder(), decoder=new TextDecoder(), queues=new Map();
  let epoch=0,keyPromise=null;
  const assertCurrent = stamp => { if(stamp!==epoch)throw error('CLEARED','기기 초안 접근이 해제되었습니다.'); };
  const key = async stamp => {
    if(!crypto?.subtle)throw error('CRYPTO_UNAVAILABLE','이 환경에서는 기기 초안을 암호화할 수 없습니다. 서버 저장을 확인해 주세요.');
    if(!keyPromise) keyPromise=(async()=>{
      const k=await loadKey(); assertCurrent(stamp);
      if(k.userId!==userId||typeof k.keyId!=='string'||typeof k.key!=='string'||bytes(k.key).length!==32)throw error('WRONG_ACCOUNT','로그인한 본인의 초안 키가 아닙니다.');
      return {id:k.keyId, key:await crypto.subtle.importKey('raw',bytes(k.key),'AES-GCM',false,['encrypt','decrypt'])};
    })().catch(e=>{if(stamp===epoch)keyPromise=null;throw e;});
    const k=await keyPromise;assertCurrent(stamp);return k;
  };
  const queue=(name,fn)=>{
    const previous=queues.get(name)||Promise.resolve();
    const job=previous.catch(()=>{}).then(fn);queues.set(name,job);
    void job.finally(()=>{if(queues.get(name)===job)queues.delete(name);}).catch(()=>{});return job;
  };
  const aad=(name,record)=>encoder.encode(JSON.stringify([prefix+name,record.v,record.keyId,record.expiresAt]));
  const purgeExpired=()=>{for(const name of entries(storage).filter(k=>k.startsWith(prefix))){try{const r=JSON.parse(storage.getItem(name));if(!r||!Number.isFinite(r.expiresAt)||r.expiresAt<=now())storage.removeItem(name);}catch{storage.removeItem(name);}}};
  return {
    async get(name) {
      const stamp=epoch;await (queues.get(name)||Promise.resolve()).catch(()=>{});assertCurrent(stamp);
      const raw=storage.getItem(prefix+name);if(raw===null)return null;
      let r;try{r=JSON.parse(raw);}catch{throw error('CORRUPT','기기 초안 형식을 확인하지 못했습니다. 서버 기록을 사용합니다.');}
      if(!Number.isFinite(r?.expiresAt)||r.expiresAt<=now()){storage.removeItem(prefix+name);return null;}
      if(r.v!==1||typeof r.nonce!=='string'||r.nonce.length!==16||typeof r.ciphertext!=='string'||r.ciphertext.length>4*1024*1024)throw error('CORRUPT','암호화 초안 형식을 확인하지 못했습니다.');
      const k=await key(stamp);if(r.keyId!==k.id)throw error('KEY_CHANGED','보호 키가 변경되어 이전 기기 초안을 복구할 수 없습니다. 서버 기록을 사용합니다.');
      try { const plain=await crypto.subtle.decrypt({name:'AES-GCM',iv:bytes(r.nonce),additionalData:aad(name,r),tagLength:128},k.key,bytes(r.ciphertext));assertCurrent(stamp);return JSON.parse(decoder.decode(plain)); }
      catch(e){if(e.code==='CLEARED')throw e;throw error('AUTHENTICATION_FAILED','기기 초안이 변경되었거나 손상되어 복구하지 않았습니다.');}
    },
    set(name,value) {
      const plain=encoder.encode(JSON.stringify(value)),stamp=epoch;
      if(plain.length>2*1024*1024)return Promise.reject(error('TOO_LARGE','기기 초안 크기 제한을 넘었습니다. 서버 저장을 확인해 주세요.'));
      return queue(name,async()=>{
        const k=await key(stamp),iv=crypto.getRandomValues(new Uint8Array(12));
        const r={v:1,keyId:k.id,expiresAt:now()+ttlMs,nonce:base64(iv)};
        const cipher=await crypto.subtle.encrypt({name:'AES-GCM',iv,additionalData:aad(name,r),tagLength:128},k.key,plain);assertCurrent(stamp);
        purgeExpired();storage.setItem(prefix+name,JSON.stringify({...r,ciphertext:base64(cipher)}));
      });
    },
    remove(name) { const stamp=epoch;return queue(name,()=>{assertCurrent(stamp);storage.removeItem(prefix+name);}); },
    forget() { epoch++;keyPromise=null; },
    clear() { epoch++;keyPromise=null;for(const name of entries(storage).filter(k=>k.startsWith(prefix)))storage.removeItem(name); },
    purgeExpired,
  };
}
