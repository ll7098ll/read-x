import test from 'node:test';
import assert from 'node:assert/strict';
import { activateDraftUser, clearPrivateDrafts, draftStore } from '../src/services/draftCache';
import { privateDraftPrefix } from '../shared/encrypted-drafts.mjs';
import { examApi } from '../src/services/examApi';

test('account changes, cross-tab logout and late key replies cannot expose or recreate private browser drafts; own legacy drafts migrate encrypted',async()=>{
  const saved={window:globalThis.window,storage:globalThis.localStorage,fetch:globalThis.fetch,channel:globalThis.BroadcastChannel};
  const map=new Map<string,string>(),events=new EventTarget(),channels:any[]=[];
  const storage={get length(){return map.size;},key:(i:number)=>[...map.keys()][i]??null,getItem:(k:string)=>map.get(k)??null,setItem:(k:string,v:string)=>{map.set(k,v);},removeItem:(k:string)=>{map.delete(k);},clear:()=>map.clear()};
  const win:any={localStorage:storage,dispatchEvent:(e:Event)=>events.dispatchEvent(e),addEventListener:(...args:any[])=>events.addEventListener(args[0],args[1]),removeEventListener:(...args:any[])=>events.removeEventListener(args[0],args[1])};
  class Channel {onmessage:any;constructor(){channels.push(this);}postMessage(_value:any){}close(){}}
  let identity='user-a',requested:any[]=[],gate:Promise<void>|null=null,release:()=>void=()=>{},began:()=>void=()=>{};
  const keyA=btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32)))),keyB=btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32))));
  try{
    Object.defineProperty(globalThis,'window',{configurable:true,value:win});Object.defineProperty(globalThis,'localStorage',{configurable:true,value:storage});Object.defineProperty(globalThis,'BroadcastChannel',{configurable:true,value:Channel});
    globalThis.fetch=async(url:any,options:any)=>{requested.push({url,body:JSON.parse(options.body)});const userId=identity;began();if(gate)await gate;return new Response(JSON.stringify({userId,keyId:userId+'-key',key:userId==='user-a'?keyA:keyB}),{status:200});};
    activateDraftUser('user-a');const a=draftStore('user-a'),name='readx-learning:user-a:run';const draft={writing:'가상 학생의 저장 대기 문장',revision:2};map.set(name,JSON.stringify(draft));
    assert.deepEqual(await a.get(name),draft);assert.equal(map.has(name),false);assert.ok(map.has(privateDraftPrefix('user-a')+name));assert.equal(JSON.stringify([...map]).includes(draft.writing),false);assert.equal(JSON.stringify([...map]).includes(keyA),false);assert.deepEqual(requested[0].body,{});
    let clears=0;events.addEventListener('readx-private-session-cleared',()=>clears++);identity='user-b';activateDraftUser('user-b');assert.equal(map.has(privateDraftPrefix('user-a')+name),false);assert.ok(clears>0);
    const b=draftStore('user-b');await b.set('run',{writing:'다른 가상 학생'});channels[0].onmessage({data:'clear'});assert.equal([...map.keys()].some(k=>k.startsWith(privateDraftPrefix('user-b'))),false);
    identity='user-a';activateDraftUser('user-a');const late=draftStore('user-a');let started;const waiting=new Promise<void>(r=>{started=r;});gate=new Promise<void>(r=>{release=r;});began=()=>started();const task=late.set('late',{writing:'늦은 응답은 저장 금지'});await waiting;clearPrivateDrafts();release();await assert.rejects(task,e=>(e as any).code==='CLEARED');assert.equal([...map.keys()].some(k=>k.startsWith(privateDraftPrefix('user-a'))),false);
    assert.equal(requested.every(r=>r.url==='/api/exam/account/device-key'&&Object.keys(r.body).length===0),true);
    gate=null;began=()=>{};
    let complete:()=>void=()=>{},requestStarted:()=>void=()=>{};const replyReady=new Promise<void>(r=>{complete=r;}),requestReady=new Promise<void>(r=>{requestStarted=r;});
    globalThis.fetch=async()=>{requestStarted();await replyReady;return new Response(JSON.stringify({user:{id:'user-a'}}),{status:200});};
    const oldReply=examApi('/dashboard',undefined,'student');await requestReady;clearPrivateDrafts();complete();await assert.rejects(oldReply,e=>(e as any).stale===true);
    globalThis.fetch=async()=>new Response(JSON.stringify({user:{id:'user-a'}}),{status:200});await examApi('/session',undefined,'student');
    globalThis.fetch=async()=>{throw new TypeError('offline');};
    await assert.rejects(examApi('/logout',{},'student'),e=>(e as any).status===503);assert.equal(JSON.parse(map.get('readx-private-logout-pending')!).userId,'user-a');assert.equal([...map.keys()].some(k=>k.startsWith(privateDraftPrefix('user-a'))),false);
    const order:string[]=[];globalThis.fetch=async(url:any)=>{order.push(String(url));return new Response(JSON.stringify(String(url).endsWith('/logout')?{ok:true}:{user:null}),{status:200});};
    await examApi('/session',undefined,'student');assert.deepEqual(order,['/api/exam/logout','/api/exam/session']);assert.equal(map.has('readx-private-logout-pending'),false);
    order.length=0;map.set('readx-private-logout-pending','{broken');await examApi('/session',undefined,'student');assert.deepEqual(order,['/api/exam/logout','/api/exam/session']);
    let allowKey=true,authStage='enroll';globalThis.fetch=async(url:any)=>String(url).endsWith('/account/device-key')?new Response(JSON.stringify(allowKey?{userId:'user-a',keyId:'user-a-key',key:keyA}:{error:'로그인 필요'}),{status:allowKey?200:401}):new Response(JSON.stringify({user:{id:'user-a'},auth:{stage:authStage}}),{status:200});
    activateDraftUser('user-a');const beforeGate=draftStore('user-a');await beforeGate.set('protected',{writing:'본인 재인증 후 복구할 가상 초안'});const clearsBefore=clears;
    const gated=await examApi('/session',undefined,'student');assert.equal(gated.auth.stage,'enroll');assert.equal([...map.keys()].some(k=>k.startsWith(privateDraftPrefix('user-a'))),true);assert.equal(clears,clearsBefore);await assert.rejects(beforeGate.get('protected'),e=>(e as any).code==='CLEARED');
    allowKey=false;await assert.rejects(draftStore('user-a').get('protected'),e=>(e as any).status===401);assert.equal([...map.keys()].some(k=>k.startsWith(privateDraftPrefix('user-a'))),true);
    allowKey=true;authStage='full';await examApi('/session',undefined,'student');assert.equal((await draftStore('user-a').get('protected')).writing,'본인 재인증 후 복구할 가상 초안');clearPrivateDrafts();assert.equal([...map.keys()].some(k=>k.startsWith(privateDraftPrefix('user-a'))),false);
  }finally{
    clearPrivateDrafts();globalThis.fetch=saved.fetch;Object.defineProperty(globalThis,'window',{configurable:true,value:saved.window});Object.defineProperty(globalThis,'localStorage',{configurable:true,value:saved.storage});Object.defineProperty(globalThis,'BroadcastChannel',{configurable:true,value:saved.channel});
  }
});
