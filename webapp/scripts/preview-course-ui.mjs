// Ephemeral browser-test fixture only. Its clock endpoint is never installed in the app server.
import {createServer} from 'node:http';
import {createServer as createViteServer} from 'vite';
import react from '@vitejs/plugin-react';
import {fileURLToPath} from 'node:url';
import {createExamService} from '../server/exam-service.mjs';
const root=fileURLToPath(new URL('..',import.meta.url));
let at=Date.now()-14*86400000;
const service=createExamService({dbPath:':memory:',privacyMode:'synthetic',timer:false,now:()=>at});
const vite=await createViteServer({root,configFile:false,plugins:[react()],server:{middlewareMode:true,hmr:false,fs:{deny:['.env','.env.*','**/server/**','**/.exam-data/**','**/.git/**']}}});
const server=createServer(async(req,res)=>{
 if(req.url==='/__qa/advance'&&req.method==='POST'){let raw='';for await(const c of req)raw+=c;at+=JSON.parse(raw).days*86400000;res.setHeader('Content-Type','application/json');res.end(JSON.stringify({now:at}));return;}
 if(req.url.startsWith('/api/exam/'))return service.handler(req,res);
 vite.middlewares(req,res);
});
await new Promise(r=>server.listen(5195,'127.0.0.1',r));
let cookie='';const origin='http://127.0.0.1:5195';
const res=await fetch(origin+'/api/exam/setup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:'코스 검증 교사',username:'course-teacher',password:'Course-Preview-2026!'})});
cookie=res.headers.get('set-cookie').split(';')[0];if(!res.ok)throw Error(await res.text());
const roster=await fetch(origin+'/api/exam/roster',{method:'POST',headers:{'Content-Type':'application/json',Cookie:cookie,Origin:origin},body:JSON.stringify({student:{name:'코스 검증 학생',username:'course-student',password:'Course-Preview-2026!'}})});
if(!roster.ok)throw Error(await roster.text());
console.log(`Course UI fixture ready: ${origin}/#/teacher/classes`);
for(const sig of ['SIGINT','SIGTERM'])process.once(sig,async()=>{await vite.close();server.closeAllConnections();server.close(()=>{service.close();process.exit(0);});});
