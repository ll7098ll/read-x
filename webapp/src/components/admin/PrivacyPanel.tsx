import React, { useEffect, useRef, useState } from 'react';
import { examApi } from '../../services/examApi';
import type { ExamUser } from '../../types/exam';
import {SensitiveActionFields,sensitiveProof} from '../exam/SensitiveActionFields';

const labels: Record<string,string> = { verification_pending:'법정대리인 확인 대기', policy_pending:'안내문 게시 대기', consent_pending:'보호자 동의 대기', granted:'이용 동의 완료', policy_changed:'변경 안내문 동의 대기', withdrawn:'동의 철회', synthetic:'가상 자료 검증용' };
const fields: Record<string,string> = { version:'안내문 버전', operatorLegalName:'개인정보 처리 사업자명', privacyContact:'개인정보 담당자·문의 연락처', purpose:'필수 수집·이용 목적', items:'필수 수집 항목', retention:'보유기간과 파기 기준', refusal:'동의 거부 권리와 거부 시 영향', childNotice:'어린이가 이해할 수 있는 안내', guardianNotice:'법정대리인 확인 방법과 동의·철회 방법', enrollmentBasisReference:'동의 전 최소 등록의 처리 근거·검토 문서 참조', reviewReference:'안내문·확인 절차 검토 문서 참조' };
const val = (f:FormData,k:string) => String(f.get(k)||'').trim();
const when = (at:number) => new Date(at).toLocaleString('ko-KR',{timeZone:'Asia/Seoul'});

export function PolicyNotice({ policy:p }: {policy:any}) {
  return <article className="ex-card"><h3>개인정보 안내 · {p.version}</h3>
    {['operatorLegalName','privacyContact','purpose','items','retention','refusal','childNotice','guardianNotice'].map(k=><div key={k}><h4>{fields[k]}</h4><p style={{whiteSpace:'pre-wrap'}}>{p[k]}</p></div>)}
    {p.optional.map((v:any)=><section key={v.id}><h4>선택 · {v.title}</h4><p>목적: {v.purpose}</p><p>항목: {v.items}</p><p>보유기간: {v.retention}</p><p>거부 권리와 영향: {v.refusal}</p></section>)}
  </article>;
}

export function PublicPrivacyNotice() {
  const [policies,setPolicies]=useState<any[]|null>(null),[error,setError]=useState('');
  return <details className="ex-card" onToggle={e=>{if(e.currentTarget.open && policies===null)void examApi('/privacy/notice').then(d=>setPolicies(d.policies)).catch(e=>setError(e.message));}}><summary>개인정보 안내문 확인</summary>
    {error&&<p role="alert">{error}</p>}{policies?.length===0&&<p>학원의 개인정보 안내문이 아직 게시되지 않았습니다. 학원에 문의해 주세요.</p>}{policies?.map(p=><PolicyNotice key={p.id} policy={p}/>)}</details>;
}

export function PrivacyPanel({user,people,onChanged}: {user:ExamUser;people:any[];onChanged:()=>Promise<unknown>}) {
  const [data,setData]=useState<any>(null),[busy,setBusy]=useState(false),[error,setError]=useState(''),[message,setMessage]=useState('');
  const [optional,setOptional]=useState<string[]>([]);
  const pending=useRef(new Map<string,string>());
  const refresh=async()=>setData(await examApi('/privacy/dashboard'));
  useEffect(()=>{void refresh().catch(e=>setError(e.message));},[user.id]);
  useEffect(()=>{setOptional(data?.policy?.optional.map(v=>v.id)||[]);},[data?.policy?.id]);
  const act=async(path:string,body:any,success:string,proof?:FormData)=>{if(busy)return;setBusy(true);setError('');setMessage('');const key=path+JSON.stringify(body);if(['/privacy/consents','/privacy/withdraw'].includes(path)){if(!pending.current.has(key))pending.current.set(key,crypto.randomUUID());body={...body,requestId:pending.current.get(key)};}try{await examApi(path,proof?{...body,...sensitiveProof(proof)}:body);pending.current.delete(key);await refresh();await onChanged();setMessage(success);}catch(e){setError(e.message);}finally{setBusy(false);}};
  if(!data)return <section className="ex-card"><h2>보호자 확인·동의</h2>{error?<p role="alert">{error}</p>:<p>이력을 불러오는 중입니다.</p>}</section>;
  const students=people.filter(v=>v.role==='student'),parents=people.filter(v=>v.role==='parent');
  return <section className="ex-card"><h2>보호자 확인·동의</h2>{error&&<p className="ex-error" role="alert">{error}</p>}{message&&<p className="ex-success" role="status">{message}</p>}
    {data.mode==='synthetic'?<p>가상 자료 검증 모드입니다. 이 자료와 계정으로 실제 개인정보 동의를 받을 수 없습니다.</p>:<>
      {user.role==='teacher'&&<><p>학생 등록만으로 동의가 완료되지 않습니다. 법정대리인 확인과 보호자의 최신 안내문 동의가 완료되어야 학생이 이용할 수 있습니다.</p><ul>{data.students.map(s=><li key={s.id}>{s.name} · {labels[s.consentStatus]||'확인 필요'}</li>)}</ul></>}
      {user.isOwner&&<>
        <details><summary>나중에 연결할 보호자 계정 등록</summary><p>학생만 먼저 등록했거나 형제·자매를 연결할 보호자 계정이 없을 때 등록하세요. 계정 등록 후에도 법정대리인 확인과 동의가 필요합니다.</p><form onSubmit={async e=>{e.preventDefault();const f=new FormData(e.currentTarget);await act('/org/parents',{name:val(f,'name'),username:val(f,'username'),password:String(f.get('password')||''),registrationReference:val(f,'registrationReference')},'보호자 계정을 등록했습니다. 본인 확인 후 계정 정보를 안전하게 전달해 주세요.');}}><fieldset disabled={busy}><label>보호자 이름<input name="name" required maxLength={40}/></label><label>보호자 아이디<input name="username" required pattern="[a-zA-Z0-9._-]{3,40}" maxLength={40} autoComplete="off"/></label><label>초기 비밀번호<input name="password" type="password" required minLength={10} maxLength={128} autoComplete="new-password"/></label><label>계정 등록 근거의 문서 관리 번호<input name="registrationReference" required maxLength={300}/></label><button>보호자 계정 등록</button></fieldset></form></details>
        <details><summary>개인정보 안내문 게시·변경</summary><p>실제 운영 내용과 확인 절차를 검토한 문서를 게시하세요. 새 버전을 게시하면 기존 학생도 다시 동의할 때까지 이용이 중지됩니다. 게시된 버전과 동의 이력은 보존됩니다.</p>
          <form key={data.policy?.id||'new'} onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act('/privacy/policies',{previousPolicyId:data.policy?.id||null,...Object.fromEntries(Object.keys(fields).map(k=>[k,val(f,k)])),optional:optional.map(id=>Object.fromEntries(['id','title','purpose','items','retention','refusal'].map(k=>[k,k==='id'?id:val(f,id+'-'+k)]))),reviewed:f.has('reviewed')},'안내문을 게시했습니다. 기존 동의가 있으면 최신 버전의 동의를 다시 받아야 합니다.',f);}}><fieldset disabled={busy}>
            {Object.entries(fields).map(([k,label])=><label key={k}>{label}{['version','operatorLegalName','privacyContact'].includes(k)?<input name={k} required maxLength={200} defaultValue={k==='version'?'':data.policy?.[k]||''}/>:<textarea name={k} required maxLength={3000} defaultValue={data.policy?.[k]||''}/>}</label>)}
            <p>선택 동의는 필수 수집과 분리하여 작성하세요. 결제·문자·외부 AI 서비스는 별도 검토 후 연결합니다.</p>
            {optional.map(id=><fieldset key={id}><legend>선택 동의 항목</legend>{['title','purpose','items','retention','refusal'].map(k=><label key={k}>{{title:'제목',purpose:'목적',items:'항목',retention:'보유기간',refusal:'거부 권리와 영향'}[k]}<textarea name={id+'-'+k} required maxLength={2000} defaultValue={data.policy?.optional.find(v=>v.id===id)?.[k]||''}/></label>)}<button type="button" onClick={()=>setOptional(old=>old.filter(v=>v!==id))}>선택 항목 제거</button></fieldset>)}
            <button type="button" disabled={optional.length>=10} onClick={()=>setOptional(old=>[...old,'option_'+crypto.randomUUID().slice(0,8)])}>선택 동의 항목 추가</button>
            <label className="ex-check"><input type="checkbox" name="reviewed" required/> 실제 운영 내용, 사전 등록 근거와 법정대리인 확인 절차를 검토했습니다.</label><SensitiveActionFields user={user}/><button>새 버전 게시</button>
          </fieldset></form>
        </details>
        <details><summary>법정대리인 확인 기록</summary><p>학원에서 실제 확인을 마친 뒤 기록하세요. 신분증·주민등록번호·가족관계 서류를 이 화면에 입력하거나 붙여 넣지 마세요. 별도 보관 문서의 관리 번호만 기록합니다.</p>
          <form onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget),studentId=val(f,'studentId');void act('/privacy/verifications',{studentId,parentId:val(f,'parentId'),method:val(f,'method'),reference:val(f,'reference'),reason:val(f,'reason'),previousVerificationId:data.verifications.filter(v=>v.studentId===studentId&&!v.revokedAt).at(-1)?.id||null,confirmed:f.has('confirmed')},'법정대리인 확인을 기록했습니다. 보호자는 비밀번호 변경 후 안내문에 동의할 수 있습니다.',f);}}><fieldset disabled={busy}><label>학생<select name="studentId" required><option value="">학생 선택</option>{students.map(v=><option key={v.id} value={v.id}>{v.name}</option>)}</select></label><label>법정대리인 계정<select name="parentId" required><option value="">보호자 선택</option>{parents.map(v=><option key={v.id} value={v.id}>{v.name} · {v.username}</option>)}</select></label><label>실제 확인 방법<select name="method"><option value="in_person">대면 확인</option><option value="signed_document">서면 문서 확인</option></select></label><label>별도 보관 확인 문서 관리 번호<input name="reference" required maxLength={300}/></label><label>확인 사유<input name="reason" required maxLength={500}/></label><label className="ex-check"><input type="checkbox" name="confirmed" required/> 본인과 법정대리인 관계를 학원의 검토된 절차로 확인했습니다.</label><SensitiveActionFields user={user}/><button>확인 기록 저장</button></fieldset></form>
          {data.verifications.filter(v=>!v.revokedAt).map(v=><form key={v.id} onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act(`/privacy/verifications/${v.id}/revoke`,{reason:val(f,'reason')},'확인을 해제했습니다. 학생 이용과 보호자의 학습정보 접근이 중지됩니다.',f);}}><p>{students.find(s=>s.id===v.studentId)?.name} · {parents.find(p=>p.id===v.parentId)?.name} · {when(v.at)}</p><label>연결 해제 사유<input name="reason" required maxLength={500}/></label><SensitiveActionFields user={user}/><button disabled={busy}>확인·연결 해제</button></form>)}
        </details>
      </>}
      {data.policy?<PolicyNotice policy={data.policy}/>:<p>학원에서 개인정보 안내문을 게시한 뒤 동의를 진행할 수 있습니다.</p>}
      {user.role==='parent'&&<>
        {data.mustChangePassword&&<p role="status">동의 전에 위에서 초기 비밀번호를 본인 비밀번호로 변경해 주세요.</p>}
        {!data.students.length&&<p>법정대리인 확인이 완료된 자녀가 없습니다. 학원에 확인 절차를 문의해 주세요.</p>}
        {data.students.map(s=><section key={s.id}><h3>{s.name} · {labels[s.consentStatus]||'확인 필요'}</h3>
          {data.policy&&<form key={s.id+':'+data.policy.id+':'+s.consentStatus} onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);void act('/privacy/consents',{studentId:s.id,policyId:data.policy.id,policyHash:data.policy.contentHash,required:f.has('required'),optional:Object.fromEntries(data.policy.optional.map(v=>[v.id,val(f,'optional-'+v.id)==='yes']))},'동의 선택을 저장했습니다.');}}><fieldset disabled={busy||data.mustChangePassword}>
            <label className="ex-check"><input name="required" type="checkbox" required/> 안내문을 확인했으며 자녀의 필수 개인정보 수집·이용에 동의합니다.</label>
            {data.policy.optional.map(v=><label key={v.id}>선택 · {v.title}<select name={'optional-'+v.id} required defaultValue=""><option value="" disabled>동의 여부 선택</option><option value="no">동의하지 않음</option><option value="yes">동의함</option></select></label>)}
            <button>동의 선택 저장</button></fieldset></form>}
          <form onSubmit={e=>{e.preventDefault();if(window.confirm('필수 수집·이용 동의를 철회하면 학생의 이용과 자녀 리포트 접근이 중지됩니다. 철회할까요?'))void act('/privacy/withdraw',{studentId:s.id},'동의를 철회했습니다. 학생 이용과 학습정보 접근을 중지했습니다. 기록 삭제·보관은 학원에 문의해 주세요.');}}><button disabled={busy}>필수 동의 철회·이용 중지</button></form>
        </section>)}
      </>}
      <details><summary>기록된 동의·철회 이력 {data.consents.length}건</summary>{data.consents.slice().reverse().map(c=><article key={c.id}><p>{c.studentName} · {when(c.at)} · {c.action==='withdraw'?'필수 동의 철회':'동의 선택 저장'} · 안내문 {c.policy?.version||'미게시'}</p>{c.action==='grant'&&<ul>{Object.entries(c.optional).map(([key,v])=><li key={key}>{c.policy?.optional.find(item=>item.id===key)?.title||key} · {v?'동의':'동의하지 않음'}</li>)}</ul>}{c.policy&&<details><summary>당시 안내문</summary><PolicyNotice policy={c.policy}/></details>}</article>)}</details>
    </>}
  </section>;
}
