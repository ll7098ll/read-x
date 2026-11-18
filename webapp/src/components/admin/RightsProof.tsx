import React from 'react';
import type {ExamUser} from '../../types/exam';
export function RightsProof({user}:{user:ExamUser}){return <fieldset><legend>본인 확인</legend><label>본인의 현재 비밀번호<input name="currentPassword" type="password" required maxLength={128} autoComplete="current-password"/></label>{user.mfaEnabled&&<label>인증앱의 새 코드<input name="mfaCode" pattern="[0-9]{6}" inputMode="numeric" required minLength={6} maxLength={6} autoComplete="one-time-code"/><small>방금 사용한 코드는 다음 코드로 바뀐 뒤 입력하세요.</small></label>}</fieldset>;}
