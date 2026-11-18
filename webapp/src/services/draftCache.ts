import { createEncryptedDraftStore, PRIVATE_DRAFT_PREFIX, privateDraftPrefix } from '../../shared/encrypted-drafts.mjs';
import { createHttpExamClient } from '../../shared/http-exam-client.mjs';

type DraftStore = { get:(key:string)=>Promise<any>;set:(key:string,value:any)=>Promise<void>;remove:(key:string)=>Promise<void>;clear:()=>void;forget:()=>void };
const stores=new Map<string,DraftStore>();
const transport=createHttpExamClient();
let activeUser='',channel:BroadcastChannel|null=null,listening=false;
const legacy=(key:string)=>/^readx-(learning|exam-pending):/.test(key);
const keys=()=>Array.from({length:localStorage.length},(_,i)=>localStorage.key(i)).filter((k):k is string=>!!k);
function releaseLocal(purge:boolean,notify=true) {
  for(const store of stores.values())try{if(purge)store.clear();else store.forget();}catch{}
  stores.clear();activeUser='';
  try{for(const k of keys()){
    if(legacy(k)){localStorage.removeItem(k);continue;}
    if(!k.startsWith(PRIVATE_DRAFT_PREFIX))continue;
    if(purge){localStorage.removeItem(k);continue;}
    try{const r=JSON.parse(localStorage.getItem(k)||'null');if(!r||!Number.isFinite(r.expiresAt)||r.expiresAt<=Date.now())localStorage.removeItem(k);}catch{localStorage.removeItem(k);}
  }}catch{}
  if(notify&&typeof window!=='undefined')window.dispatchEvent(new Event('readx-private-session-cleared'));
}
function listen() {
  if(listening||typeof window==='undefined'||import.meta.env.VITE_EXAM_MODE==='demo')return;listening=true;
  try{if(typeof BroadcastChannel!=='undefined'){channel=new BroadcastChannel('readx-private-session');channel.onmessage=e=>{if(e.data==='lock')releaseLocal(false);else if(e.data==='clear')releaseLocal(true);};}}catch{channel=null;}
  window.addEventListener('storage',e=>{if(e.key==='readx-private-session-clear')releaseLocal(!e.newValue?.startsWith('lock:'));});
}
export function clearPrivateDrafts(notify=true) {
  if(import.meta.env.VITE_EXAM_MODE==='demo')return;
  listen();releaseLocal(true,notify);channel?.postMessage('clear');
  try{localStorage.setItem('readx-private-session-clear','clear:'+crypto.randomUUID());}catch{}
}
export function lockPrivateDrafts(notify=true) {
  if(import.meta.env.VITE_EXAM_MODE==='demo')return;
  listen();releaseLocal(false,notify);channel?.postMessage('lock');
  try{localStorage.setItem('readx-private-session-clear','lock:'+crypto.randomUUID());}catch{}
}
export function activateDraftUser(userId:string) {
  if(import.meta.env.VITE_EXAM_MODE==='demo')return;listen();
  if(activeUser&&activeUser!==userId)clearPrivateDrafts();activeUser=userId;
  try{for(const k of keys())if(k.startsWith(PRIVATE_DRAFT_PREFIX)&&!k.startsWith(privateDraftPrefix(userId))||legacy(k)&&!k.startsWith('readx-learning:'+userId+':')&&!k.startsWith('readx-exam-pending:'+userId+':'))localStorage.removeItem(k);}catch{}
}
export function draftStore(userId:string):DraftStore {
  if(import.meta.env.VITE_EXAM_MODE==='demo')return {get:async key=>JSON.parse(localStorage.getItem(key)||'null'),set:async(key,v)=>localStorage.setItem(key,JSON.stringify(v)),remove:async key=>localStorage.removeItem(key),clear:()=>{},forget:()=>{}};
  listen();if(stores.has(userId))return stores.get(userId)!;
  // Access storage lazily: privacy mode may disable it without blocking server save.
  const storage={get length(){return localStorage.length;},key:(i:number)=>localStorage.key(i),getItem:(key:string)=>localStorage.getItem(key),setItem:(key:string,v:string)=>localStorage.setItem(key,v),removeItem:(key:string)=>localStorage.removeItem(key)};
  const encrypted=createEncryptedDraftStore({userId,storage,loadKey:async()=>{try{return await transport('/account/device-key',{});}catch(e){if(e.status===401)lockPrivateDrafts();if(e.code==='MFA_REQUIRED')window.dispatchEvent(new Event('readx-mfa-required'));throw e;}}});
  let released=false;const assertOpen=()=>{if(released)throw Object.assign(new Error('이전 계정의 초안 접근이 해제되었습니다.'),{code:'CLEARED'});};
  const store:DraftStore={...encrypted,forget:()=>{released=true;encrypted.forget();},clear:()=>{released=true;encrypted.clear();},set:async(key,v)=>{assertOpen();await encrypted.set(key,v);},remove:async key=>{assertOpen();await encrypted.remove(key);},get:async key=>{
    assertOpen();
    // Migrate only the authenticated owner's old draft; never send its text to the key API.
    const current=await encrypted.get(key);assertOpen();if(current!==null){if(key.startsWith('readx-learning:'+userId+':')||key.startsWith('readx-exam-pending:'+userId+':'))storage.removeItem(key);return current;}
    if(!(key.startsWith('readx-learning:'+userId+':')||key.startsWith('readx-exam-pending:'+userId+':')))return null;
    const raw=storage.getItem(key);if(!raw)return null;const value=JSON.parse(raw);await encrypted.set(key,value);storage.removeItem(key);return value;
  }};stores.set(userId,store);return store;
}
