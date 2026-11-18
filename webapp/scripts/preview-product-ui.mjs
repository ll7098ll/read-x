// Isolated visual QA: real UI/API with synthetic accounts and an in-memory database.
// No production account or stored database is read or changed.
import { createServer as createHttpServer } from 'node:http';
import { createServer as createViteServer } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath } from 'node:url';
import { createExamService } from '../server/exam-service.mjs';

const root=fileURLToPath(new URL('..',import.meta.url));
const service=createExamService({dbPath:':memory:',privacyMode:'synthetic',timer:false});
const vite=await createViteServer({root,configFile:false,plugins:[react()],server:{middlewareMode:true,hmr:false,fs:{deny:['.env','.env.*','**/server/**','**/.exam-data/**','**/.git/**']}}});
const server=createHttpServer((req,res)=>req.url.startsWith('/api/exam/')?service.handler(req,res):vite.middlewares(req,res));
await new Promise(resolve=>server.listen(5194,'127.0.0.1',resolve));
const origin='http://127.0.0.1:5194',password='Preview-Only-2026!';
const client=()=>{let cookie='';return async(path,body)=>{
  const res=await fetch(origin+'/api/exam'+path,{method:body===undefined?'GET':'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});
  if(res.headers.get('set-cookie'))cookie=res.headers.get('set-cookie').split(';')[0];
  const data=await res.json();if(!res.ok)throw Error(path+': '+JSON.stringify(data));return data;
};};
try {
  const teacher=client(),student=client();
  await teacher('/setup',{name:'미리보기 선생님',username:'ui-teacher',password,className:'생각이 자라는 반'});
  const one=await teacher('/roster',{student:{name:'미리보기 학생',username:'ui-student',password},parent:{name:'미리보기 보호자',username:'ui-parent',password}});
  const two=await teacher('/roster',{student:{name:'연습 학생',username:'ui-student-two',password}});
  await student('/login',{username:'ui-student',password});
  const lessons=(await teacher('/learning/catalog')).lessons.filter(l=>l.grade===5).slice(0,3);
  for(const [i,l] of lessons.entries()){
    const preview=await teacher('/learning/catalog/'+l.id);
    await teacher('/learning/approvals',{lessonId:l.id,contentHash:preview.contentHash,note:'화면 검증을 위한 합성 수업 자료입니다.',pilot:true});
    const {assignment}=await teacher('/learning/assignments',{lessonId:l.id,studentIds:[one.student.id,two.student.id],level:'standard',dueAt:Date.now()+7*86400000});
    if(i===2)continue;
    const current=await student(`/learning/assignments/${assignment.id}/start`,{}),run=structuredClone(current.run);
    for(const q of current.lesson.questions)run.responses[q.id]={choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'본문에서 조건이 달라지는 부분을 찾아 앞 문장과 연결했어요.',hintLevel:0,revealed:false,submissions:[{id:`preview-${i}-${q.id}`,choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'본문의 조건과 뒤에 나온 사례를 연결하면 이유를 설명할 수 있어요.',hintLevel:0}]};
    const saved=await student(`/learning/runs/${current.id}/save`,{revision:current.revision,mutationId:'preview-save-'+i,run,writing:'조건을 먼저 찾고 두 사례를 비교하니 글의 뜻이 더 잘 이해됐어요. 다음에는 다른 상황에도 적용해 보고 싶어요.'});
    const submitted=await student(`/learning/runs/${current.id}/submit`,{revision:saved.revision});
    if(i===0)await teacher(`/learning/runs/${current.id}/review`,{revision:submitted.revision,reviews:Object.fromEntries(current.lesson.questions.map(q=>[q.id,{outcome:'success',note:'글에서 찾은 근거와 자신의 생각을 잘 연결했어요.'}])),note:'조건이 달라지는 문장을 꼼꼼하게 찾았어요. 다음 읽기에서는 두 사례의 차이를 자기 말로 한 문장에 담아 보세요.',publish:true});
  }
  console.log('Synthetic UI preview ready: '+origin+'/#/teacher/home');
}catch(error){console.error(error);await vite.close();server.close();service.close();process.exit(1);}
for(const signal of ['SIGINT','SIGTERM'])process.once(signal,async()=>{await vite.close();server.close(()=>{service.close();process.exit(0);});});
