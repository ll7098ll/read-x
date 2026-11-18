import React,{useEffect,useState} from 'react';
import {examApi} from '../../services/examApi';
import type {ExamUser} from '../../types/exam';

const value=(f:FormData,k:string)=>String(f.get(k)||'');
export function MfaPanel({user,onChanged,gate=false}:{user:ExamUser;onChanged:()=>Promise<unknown>;gate?:boolean}) {
  const [status,setStatus]=useState<any>(null),[enrollment,setEnrollment]=useState<any>(null),[codes,setCodes]=useState<string[]|null>(null);
  const [busy,setBusy]=useState(false),[error,setError]=useState(''),[message,setMessage]=useState('');
  const refresh=async()=>setStatus(await examApi('/auth/mfa/status'));
  useEffect(()=>{void refresh().catch(e=>setError(e.message));},[user.id]);
  const act=async(path:string,body:any)=>{if(busy)return;setBusy(true);setError('');setMessage('');try{
    const r=await examApi(path,body);
    if(r.recoveryCodes){setCodes(r.recoveryCodes);setEnrollment(null);}
    else if(r.secret)setEnrollment(r);
    else if(path.endsWith('/cancel'))setEnrollment(null);
    else if(path.endsWith('/challenge')||path.endsWith('/disable')||path==='/account/password')await onChanged();
    await refresh();return r;
  }catch(e){setError(e.message);}finally{setBusy(false);}};
  if(codes)return <section className="ex-card"><h2>일회용 복구 코드를 보관하세요</h2><p>인증앱을 잃어버리면 비밀번호와 이 코드 한 개로 새 인증앱을 등록할 수 있습니다. 사용한 코드는 다시 쓸 수 없습니다.</p><p>이 화면을 닫으면 다시 표시되지 않습니다. 휴대전화와 분리된 안전한 곳에 보관하세요.</p><ol>{codes.map(c=><li key={c}><code>{c}</code></li>)}</ol><button className="ex-primary" disabled={busy} onClick={async()=>{setCodes(null);await onChanged();}}>안전한 곳에 보관했습니다 · 계속하기</button></section>;
  if(!status)return <section className="ex-card"><h2>추가 인증</h2>{error?<p className="ex-error" role="alert">{error}</p>:<p role="status">추가 인증 상태를 확인하고 있습니다.</p>}</section>;
  return <section className="ex-card"><h2>{gate?'계정을 확인해 주세요':'추가 인증 설정'}</h2>
    {error&&<p className="ex-error" role="alert">{error}</p>}{message&&<p role="status">{message}</p>}
    {status.stage==='challenge'?<>
      <p>비밀번호가 확인되었습니다. 학생 정보에 접근하려면 추가 인증을 완료해 주세요.</p>
      <form onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act('/auth/mfa/challenge',{method:value(f,'method'),code:value(f,'code').trim()});}}><fieldset disabled={busy}><label>인증 방법<select name="method"><option value="totp">인증앱의 6자리 코드</option><option value="backup">보관한 일회용 복구 코드</option><option value="server-recovery">본인 확인 후 발급받은 서버 복구 코드</option></select></label><label>인증 또는 복구 코드<input name="code" required maxLength={128} autoComplete="one-time-code" spellCheck={false}/></label><p>코드를 이미 사용했다면 다음 코드로 시도하세요. 휴대전화 시간은 자동 설정을 사용해 주세요.</p><button className="ex-primary">추가 인증</button></fieldset></form>
    </>:enrollment?<>
      <h3>인증앱에 계정을 추가하세요</h3><p>수동 등록에서 시간 기반 코드, 6자리, 30초 간격을 선택해 주세요.</p><p>발급자: {enrollment.issuer} · 계정: {enrollment.account}</p><label>인증앱 수동 등록용 설정키<textarea readOnly value={enrollment.secret} autoComplete="off" spellCheck={false} rows={3}/></label><p>설정키를 다른 사람에게 전달하거나 공용 기기에 저장하지 마세요. 등록은 {new Date(enrollment.expiresAt).toLocaleTimeString('ko-KR',{timeZone:'Asia/Seoul'})}까지 유효합니다.</p>
      <form onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act('/auth/mfa/confirm',{enrollmentId:enrollment.enrollmentId,code:value(f,'code')});}}><fieldset disabled={busy}><label>앱에 표시된 6자리 코드<input name="code" inputMode="numeric" pattern="[0-9]{6}" required minLength={6} maxLength={6} autoComplete="one-time-code"/></label><button className="ex-primary">인증앱 등록 완료</button></fieldset></form><button disabled={busy} onClick={()=>void act('/auth/mfa/cancel',{enrollmentId:enrollment.enrollmentId})}>등록 취소</button>
    </>:<>
      <p>{status.stage==='recovery-enroll'?'복구가 확인되었습니다. 학생 정보에 접근하기 전에 새 인증앱을 등록해 주세요.':status.enrolled?`인증앱이 등록되어 있습니다. 남은 복구 코드 ${status.recoveryRemaining}개`:'인증앱을 등록하면 비밀번호에 더해 추가 코드를 확인합니다.'}</p>
      {status.mandatory&&<p>교사·운영자는 추가 인증이 필수입니다.</p>}
      {gate&&user.mustChangePassword&&<form onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act('/account/password',{currentPassword:value(f,'currentPassword'),newPassword:value(f,'newPassword')});}}><fieldset disabled={busy}><legend>먼저 초기 비밀번호를 변경하세요</legend><label>현재 비밀번호<input name="currentPassword" type="password" required maxLength={128} autoComplete="current-password"/></label><label>본인이 사용할 새 비밀번호<input name="newPassword" type="password" required minLength={10} maxLength={128} autoComplete="new-password"/></label><button>초기 비밀번호 변경</button></fieldset></form>}
      <details open={!status.enrolled||status.stage==='recovery-enroll'}><summary>{status.enrolled?'새 인증앱으로 변경':'인증앱 등록 시작'}</summary><form onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act('/auth/mfa/enroll',{currentPassword:value(f,'password'),code:value(f,'code')});}}><fieldset disabled={busy}><label>현재 비밀번호<input name="password" type="password" required maxLength={128} autoComplete="current-password"/></label>{status.enrolled&&status.stage!=='recovery-enroll'&&<FactorField/>}<button>인증앱 등록 시작</button></fieldset></form></details>
      {status.enrolled&&status.stage==='full'&&<>
        <details><summary>복구 코드 다시 발급</summary><p>다시 발급하면 이전 복구 코드는 모두 무효가 됩니다.</p><form onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act('/auth/mfa/recovery-codes',{currentPassword:value(f,'password'),code:value(f,'code')});}}><fieldset disabled={busy}><label>현재 비밀번호<input name="password" type="password" required maxLength={128} autoComplete="current-password"/></label><FactorField/><button>복구 코드 새로 발급</button></fieldset></form></details>
        {!status.mandatory&&<details><summary>추가 인증 해제</summary><form onSubmit={e=>{e.preventDefault();if(!window.confirm('추가 인증을 해제할까요? 이후에는 비밀번호만으로 로그인합니다.'))return;const f=new FormData(e.currentTarget);void act('/auth/mfa/disable',{currentPassword:value(f,'password'),code:value(f,'code')});}}><fieldset disabled={busy}><label>현재 비밀번호<input name="password" type="password" required maxLength={128} autoComplete="current-password"/></label><FactorField/><button>추가 인증 해제</button></fieldset></form></details>}
      </>}
      {user.mustChangePassword&&<p role="status">위에서 초기 비밀번호를 본인 비밀번호로 변경한 뒤 인증앱을 등록해 주세요.</p>}
    </>}
  </section>;
}
function FactorField(){return <label>인증앱의 새 6자리 코드<input name="code" inputMode="numeric" pattern="[0-9]{6}" required minLength={6} maxLength={6} autoComplete="one-time-code"/><small>방금 사용한 코드는 다음 코드로 바뀐 뒤 입력하세요.</small></label>;}
