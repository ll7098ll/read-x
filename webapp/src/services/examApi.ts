import { readExamRoute } from './examNavigation';
import type { ExamRole } from '../types/exam';
import { createHttpExamClient } from '../../shared/http-exam-client.mjs';
import { activateDraftUser, clearPrivateDrafts,lockPrivateDrafts } from './draftCache';

// Production is always server-backed. Demo must be selected explicitly at build time.
export const examDemo = import.meta.env.VITE_EXAM_MODE === 'demo';
const httpClient = createHttpExamClient();
let demoClient: any;
let requestGeneration=0,listening=false,activeUserId='';
let logoutPending:{userId:string}|null=null,markerUnavailable=false;
const pendingKey='readx-private-logout-pending';
const pendingLogout=()=>{try{if(markerUnavailable)return logoutPending;const raw=localStorage.getItem(pendingKey);if(!raw)return null;try{const v=JSON.parse(raw);return v&&typeof v.userId==='string'&&v.userId.length<=100?{userId:v.userId}:{userId:''};}catch{return {userId:''};}}catch{return logoutPending;}};
const markLogout=(pending:{userId:string}|null)=>{logoutPending=pending;try{if(pending)localStorage.setItem(pendingKey,JSON.stringify(pending));else localStorage.removeItem(pendingKey);markerUnavailable=false;}catch{markerUnavailable=true;}};

export async function examApi<T = any>(path: string, body?: unknown, role: ExamRole = readExamRoute(window.location.hash).role || 'student'): Promise<T> {
  if (import.meta.env.VITE_EXAM_MODE === 'demo') {
    if (!demoClient) {
      const { createLocalExamClient } = await import('../../shared/local-exam-client.mjs');
      demoClient = createLocalExamClient({
        storage: { getItem: (key: string) => localStorage.getItem(key), setItem: (key: string, value: string) => localStorage.setItem(key, value) },
        lock: async (action: () => T) => navigator.locks ? navigator.locks.request('readx-exam-demo', action) : action(),
      });
    }
    return demoClient(path, body, role) as Promise<T>;
  }
  if(!listening&&typeof window!=='undefined'){listening=true;window.addEventListener('readx-private-session-cleared',()=>{requestGeneration++;activeUserId='';});}
  if(path==='/logout'){markLogout({userId:activeUserId});clearPrivateDrafts();}
  const generation=requestGeneration;
  try {
    // Complete an interrupted logout before any request can restore a session.
    const queued=pendingLogout();
    if(path!=='/logout'&&queued){await httpClient('/logout',{expectedUserId:queued.userId||undefined});markLogout(null);}
    const data=await httpClient(path,path==='/logout'?{expectedUserId:queued?.userId||undefined}:body);
    if(generation!==requestGeneration)throw Object.assign(new Error('계정 변경으로 이전 요청을 취소했습니다.'),{status:409,stale:true});
    if(data.user?.restoreCredentialHold){requestGeneration++;lockPrivateDrafts(false);}
    if(data.auth?.stage&&data.auth.stage!=='full'){requestGeneration++;if(data.auth.stage==='recovery-enroll')clearPrivateDrafts(false);else lockPrivateDrafts(false);}
    if(path==='/logout')markLogout(null);
    if(['/account/password','/auth/mfa/confirm','/auth/mfa/disable'].includes(path)){requestGeneration++;clearPrivateDrafts(false);}
    else if(['/logout','/recover'].includes(path))clearPrivateDrafts();
    else if(data.user?.id){activateDraftUser(data.user.id);activeUserId=data.user.id;}
    else if(path==='/session'&&!data.user)lockPrivateDrafts();
    return data as T;
  }catch(e){if(generation!==requestGeneration&&!e.stale)throw Object.assign(new Error('계정 변경으로 이전 요청을 취소했습니다.'),{status:409,stale:true});if(e.status===401)lockPrivateDrafts();if(e.code==='MFA_REQUIRED')window.dispatchEvent(new Event('readx-mfa-required'));if(e.code==='RESTORE_CREDENTIALS_REQUIRED')window.dispatchEvent(new Event('readx-restore-required'));if(e.code==='PROCESSING_RESTRICTED')window.dispatchEvent(new Event('readx-processing-changed'));throw e;}
}
