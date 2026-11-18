import React,{useState} from 'react';
import type {ExamUser} from '../../types/exam';
import {RightsPanel} from '../admin/RightsPanel';
import {PrivacyPanel} from '../admin/PrivacyPanel';
import {MfaPanel} from './MfaPanel';
import {examApi} from '../../services/examApi';
export function RestrictedAccountPanel({user,onChanged}:{user:ExamUser;onChanged:()=>Promise<unknown>}){
 const [busy,setBusy]=useState(false),[error,setError]=useState('');
 return <section><section className="ex-card"><h1>일반 서비스 처리가 정지되어 있습니다</h1><p>수업·평가·일반 리포트 이용이 제한됩니다. 본인의 권리 요청과 필요한 계정 보안 설정은 계속 이용할 수 있습니다. 해제는 학원에서 요청 의사와 처리 근거를 확인한 뒤 진행합니다.</p><button disabled={busy} onClick={()=>void onChanged()}>현재 상태 다시 확인</button></section><RightsPanel user={user} onChanged={onChanged}/>{user.role==='parent'&&<PrivacyPanel user={user} people={[]} onChanged={onChanged}/>}<section className="ex-card"><h2>본인 비밀번호 변경</h2>{error&&<p role="alert">{error}</p>}<form onSubmit={async e=>{e.preventDefault();if(busy)return;const f=new FormData(e.currentTarget);setBusy(true);setError('');try{await examApi('/account/password',{currentPassword:String(f.get('currentPassword')),newPassword:String(f.get('newPassword')),code:String(f.get('code')||'')});await onChanged();}catch(e){setError(e.message);}finally{setBusy(false);}}}><fieldset disabled={busy}><label>현재 비밀번호<input name="currentPassword" type="password" required maxLength={128} autoComplete="current-password"/></label><label>새 비밀번호<input name="newPassword" type="password" required minLength={10} maxLength={128} autoComplete="new-password"/></label>{user.mfaEnabled&&<label>인증앱의 새 코드<input name="code" required pattern="[0-9]{6}" maxLength={6} inputMode="numeric" autoComplete="one-time-code"/></label>}<button>비밀번호 변경</button></fieldset></form></section><MfaPanel user={user} onChanged={onChanged}/></section>;
}
