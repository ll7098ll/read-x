import React,{useState} from 'react';
import {examApi} from '../../services/examApi';
import type {ExamUser} from '../../types/exam';
export function RestoreAccountPanel({user,onChanged}:{user:ExamUser;onChanged:()=>Promise<unknown>}){
 const [busy,setBusy]=useState(false),[error,setError]=useState('');
 return <section className="ex-card"><h1>복원 후 계정 확인이 필요합니다</h1><p>이전 백업의 비밀번호·권한·보호자 연결로 학습 기록을 바로 열 수 없습니다. 학원에서 본인과 현재 이용 자격을 확인한 뒤 새 복구 코드를 받아 비밀번호를 재설정해 주세요. 교사·운영자의 인증앱과 법정대리인 확인·동의도 다시 확인합니다.</p>{error&&<p className="ex-error" role="alert">{error}</p>}<form onSubmit={async e=>{e.preventDefault();if(busy)return;const f=new FormData(e.currentTarget);setBusy(true);setError('');try{await examApi('/recover',{username:user.username,code:String(f.get('code')||'').trim(),newPassword:String(f.get('newPassword')||'')});await onChanged();}catch(e){setError(e.message);}finally{setBusy(false);}}}><fieldset disabled={busy}><label>계정 아이디<input value={user.username} readOnly autoComplete="username"/></label><label>본인 확인 후 받은 새 복구 코드<input name="code" required maxLength={128} autoComplete="off"/></label><label>새 비밀번호<input name="newPassword" type="password" required minLength={10} maxLength={128} autoComplete="new-password"/></label><button>확인한 계정의 비밀번호 재설정</button></fieldset></form><button disabled={busy} onClick={()=>void onChanged()}>현재 확인 상태 다시 불러오기</button></section>;
}
