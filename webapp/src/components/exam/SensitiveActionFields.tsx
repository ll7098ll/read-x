import React from 'react';
import type {ExamUser} from '../../types/exam';
export const sensitiveProof=(f:FormData)=>({currentPassword:String(f.get('currentPassword')||''),mfaCode:String(f.get('mfaCode')||'')});
export function SensitiveActionFields({user,required=true}:{user:Pick<ExamUser,'mfaEnabled'>;required?:boolean}){
  if(!user.mfaEnabled)return null;
  return <fieldset><legend>보안을 위해 다시 확인해 주세요</legend><label>운영자 본인의 현재 비밀번호<input name="currentPassword" type="password" required={required} maxLength={128} autoComplete="current-password"/></label><label>인증앱의 새 6자리 코드<input name="mfaCode" inputMode="numeric" pattern="[0-9]{6}" required={required} minLength={6} maxLength={6} autoComplete="one-time-code"/></label><small>{required?'권한·연결·복구 변경을 위해 확인합니다.':'담당 반·권한·활성 상태를 변경할 때 입력해 주세요.'} 방금 사용한 코드는 다음 코드로 바뀐 뒤 입력하세요.</small></fieldset>;
}
