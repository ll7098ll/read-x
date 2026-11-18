import React from 'react';
import { examApi, examDemo } from '../../services/examApi';
import { PublicPrivacyNotice } from '../admin/PrivacyPanel';

const value = (data: FormData, key: string) => String(data.get(key) || '').trim();
function Credentials({ prefix = '', title }: { prefix?: string; title: string }) {
  return <fieldset><legend>{title}</legend><div className="ex-fields">
    <label>이름<input name={`${prefix}name`} required maxLength={40} autoComplete="off"/></label>
    <label>아이디<input name={`${prefix}username`} required pattern="[a-zA-Z0-9._-]{3,40}" minLength={3} maxLength={40} autoCapitalize="none" autoComplete="off"/><small>영문·숫자·점·밑줄·하이픈 3~40자</small></label>
    <label>초기 비밀번호<input type="password" name={`${prefix}password`} required minLength={10} maxLength={128} autoComplete="new-password"/></label>
  </div></fieldset>;
}
export function AccountForm(props: { setup: boolean; busy: boolean; onSubmit: (body: Record<string, string>) => void }) {
  return <div className="garden-account">
    <aside className="garden-account-art" aria-label="ReadX 배움 안내">
      <div><p className="garden-eyebrow">ReadX 배움터</p><h2>반가워요.<br/>생각이 자라는 시간에<br/>함께해요.</h2><p>하나의 계정으로 읽기 수업부터<br/>배움의 기록까지 차근차근 이어가요.</p></div>
      <img src={`${import.meta.env.BASE_URL}brand/editorial/reading.webp`} width="1536" height="1024" alt=""/>
    </aside>
    <AccountFormContent {...props}/>
  </div>;
}
function AccountFormContent({ setup, busy, onSubmit }: { setup: boolean; busy: boolean; onSubmit: (body: Record<string, string>) => void }) {
  const [recover,setRecover]=React.useState(false),[error,setError]=React.useState(''),[done,setDone]=React.useState(false),[working,setWorking]=React.useState(false);
  if(recover) return <section className="ex-card"><h1>계정 비밀번호 복구</h1><p>학원에서 본인 확인 후 받은 일회용 코드를 입력하세요. 코드는 발급 후 15분 동안 사용할 수 있습니다.</p>{error&&<p role="alert" className="ex-error">{error}</p>}{done?<p role="status">비밀번호가 변경되었습니다. 새 비밀번호로 로그인해 주세요.</p>:<form onSubmit={async e=>{e.preventDefault();const f=new FormData(e.currentTarget);setWorking(true);setError('');try{await examApi('/recover',{username:value(f,'username'),code:value(f,'code'),newPassword:String(f.get('password')||'')});setDone(true);}catch(e){setError(e.message);}finally{setWorking(false);}}}><fieldset disabled={working}><label>아이디<input name="username" required autoComplete="username"/></label><label>복구 코드<input name="code" required maxLength={128} autoComplete="off"/></label><label>새 비밀번호<input type="password" name="password" required minLength={10} maxLength={128} autoComplete="new-password"/></label><button className="ex-primary">비밀번호 복구</button></fieldset></form>}<button onClick={()=>{setRecover(false);setError('');}}>로그인으로 돌아가기</button></section>;
  return <section className="ex-card"><h1>{setup ? '첫 교사 계정 만들기' : '학원 계정 로그인'}</h1>
    <p>{setup ? '서버 컴퓨터에서 첫 교사 계정과 반을 등록해 주세요. 학생과 보호자는 로그인 후 등록합니다.' : '선생님에게 받은 계정으로 로그인해 주세요. 배정과 리포트는 계정에 따라 표시됩니다.'}</p>
    <form onSubmit={e => { e.preventDefault(); const data = new FormData(e.currentTarget); onSubmit({ username: value(data, 'username'), password: String(data.get('password') || ''), ...(setup ? { name: value(data, 'name'), className: value(data, 'className') } : {}) }); }}>
      <fieldset disabled={busy}>{setup ? <><Credentials title="교사 정보"/><label>반 이름<input name="className" required maxLength={60}/></label></> : <div className="ex-fields"><label>아이디<input name="username" required autoComplete="username" autoCapitalize="none" maxLength={40}/></label><label>비밀번호<input name="password" type="password" required autoComplete="current-password" maxLength={128}/></label></div>}
      <button className="ex-primary" type="submit">{busy ? '확인 중…' : setup ? '교사 계정과 반 만들기' : '로그인'}</button></fieldset>
    </form>{!setup && !examDemo && <><button type="button" onClick={()=>setRecover(true)}>비밀번호를 잊었어요</button><p>학생은 학원의 보호자 확인과 최신 안내문 동의가 완료된 뒤 이용할 수 있습니다. 확인·동의를 진행할 보호자는 로그인 후 계정 설정을 열어 주세요.</p><PublicPrivacyNotice/></>}</section>;
}
export function RosterForm({ busy, onSubmit, classes=[], initialClassId='' }: { classes?: any[]; initialClassId?: string; busy: boolean; onSubmit: (body: unknown) => Promise<void> | void }) {
  const [parent, setParent] = React.useState(true);
  return <form onSubmit={async e => { e.preventDefault(); const form = e.currentTarget; const data = new FormData(form);
    const person = (prefix: string) => ({ name: value(data, `${prefix}name`), username: value(data, `${prefix}username`), password: String(data.get(`${prefix}password`) || '') });
    await onSubmit({ classId:value(data,'classId') || undefined, registrationReference:value(data,'registrationReference'), student: person('student-'), ...(parent ? { parent: person('parent-') } : {}) });
  }}><fieldset disabled={busy}>{!!classes.length && <label>등록 반<select name="classId" defaultValue={initialClassId}>{classes.filter(c=>c.active).map(c=><option key={c.id} value={c.id}>{c.name}</option>)}</select></label>}<Credentials prefix="student-" title="학생 등록"/>
    <label className="ex-check"><input type="checkbox" checked={parent} onChange={e => setParent(e.target.checked)}/> 연결 보호자 계정도 만들기</label>
    {parent && <Credentials prefix="parent-" title="연결 보호자"/>}
    <label>동의 전 등록 근거의 문서 관리 번호<input name="registrationReference" maxLength={300}/><small>개인정보 안내문에서 검토한 최소 등록 근거에 해당하는 별도 문서 참조를 입력하세요. 실제 이용 모드에서는 필수입니다.</small></label>
    <p className="ex-muted">등록 후 운영자가 법정대리인 확인을 기록하고, 보호자가 본인 비밀번호로 변경한 뒤 최신 안내문에 동의해야 학생이 이용할 수 있습니다. 보호자 확인·동의는 학원 운영 메뉴에서 진행합니다.</p>
    <button className="ex-primary" type="submit">{busy ? '등록 중…' : '학생·보호자 등록'}</button>
  </fieldset></form>;
}
