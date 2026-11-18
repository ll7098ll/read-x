// Isolated, in-memory software QA. No production account or student data.
import {createServer} from 'node:http';
import {createServer as createViteServer} from 'vite';
import react from '@vitejs/plugin-react';
import {fileURLToPath} from 'node:url';
import {createExamService} from '../server/exam-service.mjs';
const root=fileURLToPath(new URL('..',import.meta.url));
const service=createExamService({dbPath:':memory:',privacyMode:'synthetic',timer:false});
const vite=await createViteServer({root,configFile:false,plugins:[react()],server:{middlewareMode:true,hmr:false,fs:{deny:['.env','.env.*','**/server/**','**/.exam-data/**','**/.git/**']}}});
const server=createServer((req,res)=>req.url.startsWith('/api/exam/')?service.handler(req,res):vite.middlewares(req,res));
await new Promise(r=>server.listen(5196,'127.0.0.1',r));
const origin='http://127.0.0.1:5196',password='Pilot-Preview-2026!';let cookie='';
const call=async(path,body)=>{const r=await fetch(origin+'/api/exam'+path,{method:'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify(body)});if(r.headers.get('set-cookie'))cookie=r.headers.get('set-cookie').split(';')[0];if(!r.ok)throw Error(await r.text());return r.json();};
await call('/setup',{name:'가상 파일럿 교사',username:'pilot-teacher',password});
for(let n=0;n<22;n++)await call('/roster',{student:{name:`가상 파일럿 학생 ${n+1}`,username:'pilot-student-'+n,password}});
console.log(`Pilot fixture ready: ${origin} · synthetic memory only · PID ${process.pid}`);
for(const signal of ['SIGINT','SIGTERM'])process.once(signal,async()=>{await vite.close();server.closeAllConnections();server.close(()=>{service.close();process.exit(0);});});
