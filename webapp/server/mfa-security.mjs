import { randomBytes, randomUUID, createHash, timingSafeEqual } from 'node:crypto';
import { RESPONSE_STATUS } from '../shared/http-response.mjs';
import { encodeBase32, matchTotp } from './totp.mjs';
import { createMfaProtector } from './mfa-keys.mjs';

const fail=(status,message,code='MFA_INVALID')=>({[RESPONSE_STATUS]:status,error:message,code});
const digest=value=>createHash('sha256').update(value).digest('hex');
const tokenHash=(u,code)=>digest(u.id+':'+code);
const sameHash=(a,b)=>typeof a==='string'&&a.length===64&&timingSafeEqual(Buffer.from(a,'hex'),Buffer.from(b,'hex'));
const normalizeBackup=code=>typeof code==='string'&&/^[a-fA-F0-9-]{32,39}$/.test(code)?code.replaceAll('-','').toLowerCase():'';
const revoke=(s,id)=>{for(const [key,session]of Object.entries(s.sessions))if(session.userId===id)delete s.sessions[key];};

export function createMfaSecurity({dbPath,keyring,state}) {
  const protector=createMfaProtector({dbPath,keyring,hasSecrets:state.users.some(u=>u.mfa?.secret||u.pendingMfa?.secret)});
  for(const u of state.users)for(const record of [u.mfa?.secret,u.pendingMfa?.secret].filter(Boolean))protector.open(record,u);
  const mandatory=(s,u)=>u.role==='teacher'&&s.organizations.find(o=>o.id===u.tenantId)?.privacyMode!=='synthetic';
  const stage=(s,u,session,at)=>{
    if(session?.recoveryVersion&&session.recoveryVersion===u.mfa?.version&&Number.isFinite(session.recoveryVerifiedAt)&&at-session.recoveryVerifiedAt<5*60000)return 'recovery-enroll';
    if(!u.mfa?.secret)return mandatory(s,u)?'enroll':'full';
    return !u.mfa.recoveryRequired&&session?.mfaVersion===u.mfa.version&&Number.isFinite(session.mfaVerifiedAt)&&at-session.mfaVerifiedAt<8*3600000?'full':'challenge';
  };
  const status=(s,u,session,at)=>({stage:stage(s,u,session,at),mandatory:mandatory(s,u),enrolled:!!u.mfa?.secret,recoveryRemaining:u.mfa?.backups.filter(v=>!v.usedAt).length||0,pendingExpiresAt:u.pendingMfa?.expiresAt||null,serverNow:at});
  const audit=(s,u,at,action)=>s.audit.push({at,actor:u.id,action});
  const throttled=(u,at)=>u.mfaFailures?.lockedUntil>at;
  const bad=(s,u,at,message='인증 정보가 맞지 않거나 이미 사용한 코드입니다. 다시 확인해 주세요.')=>{
    const old=u.mfaFailures;if(!old||at-old.startedAt>=15*60000)u.mfaFailures={startedAt:at,count:0,lockedUntil:0};
    u.mfaFailures.count++;if(u.mfaFailures.count>=8)u.mfaFailures.lockedUntil=at+15*60000;
    audit(s,u,at,'auth.reauthentication.failed');return fail(u.mfaFailures.lockedUntil>at?429:400,u.mfaFailures.lockedUntil>at?'추가 인증 시도가 많습니다. 15분 뒤 비밀번호로 다시 로그인해 주세요.':message);
  };
  const password=(u,value,check)=>typeof value==='string'&&value.length<=128&&check(value,u.password);
  const verifyApp=(u,code,at)=>{
    if(!u.mfa?.secret||u.mfa.recoveryRequired)return false;
    const secret=protector.open(u.mfa.secret,u),counter=matchTotp(secret,code,at,u.mfa.lastCounter??-1);
    if(counter===null)return false;u.mfa.lastCounter=counter;
    if(u.mfa.secret.keyId!==protector.activeId)u.mfa.secret=protector.seal(secret,u);return true;
  };
  const backups=(u,at)=>{
    const codes=Array.from({length:10},()=>randomBytes(16).toString('hex').toUpperCase().match(/.{4}/g).join('-'));
    u.mfa.backups=codes.map(code=>({hash:tokenHash(u,normalizeBackup(code)),createdAt:at}));return codes;
  };
  const consumeBackup=(u,code,at)=>{
    const normalized=normalizeBackup(code);if(normalized.length!==32)return false;
    const value=tokenHash(u,normalized),record=u.mfa?.backups.find(v=>!v.usedAt&&sameHash(v.hash,value));if(!record)return false;record.usedAt=at;return true;
  };
  const options=(s,u,at,proof={})=>{
    if(proof.recovering&&u.mfa)return {expiresAt:at+5*60000,recoveryVerifiedAt:at,recoveryVersion:u.mfa.version,mfaPending:true};
    if(proof.verified&&u.mfa?.secret&&!u.mfa.recoveryRequired)return {expiresAt:at+8*3600000,mfaVerifiedAt:at,mfaVersion:u.mfa.version};
    if(u.mfa?.secret)return {expiresAt:at+5*60000,mfaPending:true};
    if(mandatory(s,u))return {expiresAt:at+10*60000,mfaPending:true};
    return {expiresAt:at+12*3600000};
  };
  const route=({s,u,session,sessionKey,path,method,body,at,res,issueSession,passwordOK})=>{
    if(path==='/auth/mfa/status'&&method==='GET')return status(s,u,session,at);
    if(method!=='POST')return fail(404,'추가 인증 요청을 찾을 수 없습니다.');
    if(!['/auth/mfa/enroll','/auth/mfa/confirm','/auth/mfa/cancel','/auth/mfa/challenge','/auth/mfa/recovery-codes','/auth/mfa/disable'].includes(path))return fail(404,'추가 인증 요청을 찾을 수 없습니다.');
    if(throttled(u,at))return fail(429,'추가 인증 시도가 많습니다. 15분 뒤 비밀번호로 다시 로그인해 주세요.');
    const current=stage(s,u,session,at);
    if(path==='/auth/mfa/challenge'){
      if(current!=='challenge')return fail(409,'현재 세션의 추가 인증 상태를 다시 확인해 주세요.');
      if(body.method==='totp'){
        if(!verifyApp(u,body.code,at))return bad(s,u,at);
        u.mfaFailures=null;issueSession(s,u,res,at,{verified:true});audit(s,u,at,'auth.mfa.login');return {ok:true,auth:{stage:'full'}};
      }
      let accepted=false;
      if(body.method==='backup')accepted=consumeBackup(u,body.code,at);
      if(body.method==='server-recovery'&&typeof body.code==='string'&&/^[a-f0-9]{64}$/i.test(body.code)){
        s.mfaRecoveries||=[];const record=s.mfaRecoveries.find(r=>r.userId===u.id&&r.expiresAt>at&&sameHash(r.hash,tokenHash(u,body.code.toLowerCase())));
        if(record){accepted=true;s.mfaRecoveries=s.mfaRecoveries.filter(v=>v!==record);}
      }
      if(!accepted)return bad(s,u,at);
      u.mfa.version=randomUUID();u.mfa.recoveryRequired=true;u.mfaFailures=null;delete u.pendingMfa;delete u.deviceDraftKey;revoke(s,u.id);
      issueSession(s,u,res,at,{recovering:true});audit(s,u,at,'auth.mfa.recovery');return {ok:true,auth:{stage:'recovery-enroll'}};
    }
    if(current==='challenge')return fail(403,'추가 인증을 먼저 완료해 주세요.','MFA_REQUIRED');
    if(path==='/auth/mfa/cancel'){
      if(u.pendingMfa?.id===body.enrollmentId){delete u.pendingMfa;audit(s,u,at,'auth.mfa.enroll.cancel');}return {ok:true};
    }
    if(path==='/auth/mfa/enroll'){
      if(!password(u,body.currentPassword,passwordOK))return bad(s,u,at,'현재 비밀번호를 확인해 주세요.');
      if(u.mustChangePassword)return fail(409,'초기 비밀번호를 본인 비밀번호로 변경한 뒤 진행해 주세요.');
      if(u.mfa?.secret&&current!=='recovery-enroll'&&!verifyApp(u,body.code,at))return bad(s,u,at);
      const secret=encodeBase32(randomBytes(32));u.pendingMfa={id:randomUUID(),secret:protector.seal(secret,u),expiresAt:at+10*60000,sessionKey};u.mfaFailures=null;
      audit(s,u,at,'auth.mfa.enroll.begin');
      return {secret,enrollmentId:u.pendingMfa.id,expiresAt:u.pendingMfa.expiresAt,issuer:'Read X',account:u.username,uri:`otpauth://totp/${encodeURIComponent('Read X:'+u.username)}?secret=${secret}&issuer=${encodeURIComponent('Read X')}&algorithm=SHA1&digits=6&period=30`};
    }
    if(path==='/auth/mfa/confirm'){
      const pending=u.pendingMfa;
      if(!pending||pending.id!==body.enrollmentId||pending.expiresAt<=at||pending.sessionKey!==sessionKey)return fail(409,'인증앱 등록이 만료되었거나 변경되었습니다. 등록을 다시 시작해 주세요.');
      const secret=protector.open(pending.secret,u),counter=matchTotp(secret,body.code,at);
      if(counter===null)return bad(s,u,at);
      u.mfa={secret:protector.seal(secret,u),version:randomUUID(),lastCounter:counter,enrolledAt:at,recoveryRequired:false,backups:[]};delete u.pendingMfa;delete u.deviceDraftKey;
      const codes=backups(u,at);u.mfaFailures=null;revoke(s,u.id);issueSession(s,u,res,at,{verified:true});audit(s,u,at,'auth.mfa.enroll.confirm');return {ok:true,recoveryCodes:codes};
    }
    if(current!=='full'||!u.mfa?.secret)return fail(403,'등록된 인증앱으로 인증한 세션이 필요합니다.','MFA_REQUIRED');
    if(path==='/auth/mfa/disable'&&mandatory(s,u))return fail(409,'교사·운영자 추가 인증은 해제할 수 없습니다. 새 인증앱으로 변경하거나 복구 절차를 이용해 주세요.');
    if(!password(u,body.currentPassword,passwordOK)||!verifyApp(u,body.code,at))return bad(s,u,at);
    u.mfaFailures=null;
    if(path==='/auth/mfa/recovery-codes'){
      const codes=backups(u,at);revoke(s,u.id);issueSession(s,u,res,at,{verified:true});audit(s,u,at,'auth.mfa.codes.regenerate');return {ok:true,recoveryCodes:codes};
    }
    delete u.mfa;delete u.pendingMfa;delete u.deviceDraftKey;revoke(s,u.id);issueSession(s,u,res,at);audit(s,u,at,'auth.mfa.disable');return {ok:true};
  };
  const changePassword=({s,u,body,at,res,issueSession,passwordOK,passwordHash})=>{
    if(throttled(u,at))return fail(429,'인증 시도가 많습니다. 15분 뒤 다시 시도해 주세요.');
    if(!password(u,body.currentPassword,passwordOK))return bad(s,u,at,'현재 비밀번호를 확인해 주세요.');
    if(typeof body.newPassword!=='string'||body.newPassword.length<10||body.newPassword.length>128)return fail(400,'새 비밀번호는 10~128자여야 합니다.');
    if(body.newPassword===body.currentPassword)return fail(400,'현재 비밀번호와 다른 새 비밀번호를 입력해 주세요.');
    if(u.mfa?.secret&&!verifyApp(u,body.code,at))return bad(s,u,at);
    u.password=passwordHash(body.newPassword);u.mustChangePassword=false;u.revision++;u.mfaFailures=null;delete u.pendingMfa;delete u.deviceDraftKey;
    s.recoveryCodes=s.recoveryCodes.filter(r=>r.userId!==u.id);s.mfaRecoveries=(s.mfaRecoveries||[]).filter(r=>r.userId!==u.id);revoke(s,u.id);
    issueSession(s,u,res,at,{verified:!!u.mfa?.secret});audit(s,u,at,'account.password');return {ok:true};
  };
  const needsStepUp=(s,u,path,body)=>{
    if(u.role!=='teacher'||!u.isOwner||!u.mfa?.secret)return false;
    if(['/org/teachers','/org/guardian-links','/privacy/policies','/privacy/verifications','/audit/export','/audit/checkpoint','/audit/reviews'].includes(path)||/^\/privacy\/verifications\/[^/]+\/revoke$/.test(path))return true;
    const match=/^\/org\/accounts\/([^/]+)(?:\/(reset))?$/.exec(path);if(!match)return false;
    const target=s.users.find(v=>v.id===match[1]&&v.tenantId===u.tenantId);if(!target)return false;if(match[2])return true;
    return target.role==='teacher'&&(body.active!==target.active||typeof body.isOwner==='boolean'&&body.isOwner!==!!target.isOwner||Array.isArray(body.classIds)&&JSON.stringify([...body.classIds].sort())!==JSON.stringify([...(target.classIds||[])].sort()))||target.role==='student'&&body.classId&&body.classId!==target.classId;
  };
  const stepUp=({s,u,body,at,passwordOK})=>{
    if(throttled(u,at))return fail(429,'인증 시도가 많습니다. 15분 뒤 다시 시도해 주세요.');
    if(!password(u,body.currentPassword,passwordOK)||!verifyApp(u,body.mfaCode,at))return bad(s,u,at,'이 작업에는 현재 비밀번호와 새 인증앱 코드가 필요합니다.');
    u.mfaFailures=null;audit(s,u,at,'auth.stepup');return null;
  };
  const confirmAccount=({s,u,body,at,passwordOK})=>{
    if(throttled(u,at))return fail(429,'본인 확인 시도가 많습니다. 15분 뒤 다시 시도해 주세요.');
    if(!password(u,body.currentPassword,passwordOK)||u.mfa?.secret&&!verifyApp(u,body.mfaCode,at))return bad(s,u,at,'현재 비밀번호와 등록된 경우 새 인증앱 코드가 필요합니다.');
    u.mfaFailures=null;audit(s,u,at,'auth.rights.confirm');return null;
  };
  return {options,status,route,changePassword,needsStepUp,stepUp,confirmAccount,isVerified:(s,u,session,at)=>!!u.mfa?.secret&&stage(s,u,session,at)==='full',
    guard:(s,u,session,at)=>stage(s,u,session,at)==='full'?null:fail(403,'추가 인증을 완료한 뒤 학생 정보에 접근할 수 있습니다.','MFA_REQUIRED'),
    expire(s,at){s.mfaRecoveries=(s.mfaRecoveries||[]).filter(r=>r.expiresAt>at);for(const u of s.users)if(u.pendingMfa?.expiresAt<=at)delete u.pendingMfa;},
  };
}
