// Sync the public synthetic preview only. No runtime databases or credentials.
import { cp, mkdir, readFile, writeFile } from 'node:fs/promises';
import { resolve, dirname, sep, basename } from 'node:path';
import { fileURLToPath } from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const app=resolve(root,'webapp'),site=resolve(root,'sites/readx-demo');
if(!site.startsWith(root+sep))throw Error('Site checkout must stay inside the workspace');
const hosting=JSON.parse(await readFile(resolve(site,'.openai/hosting.json'),'utf8'));
if(hosting.project_id!=='appgprj_6acf1dd19a488191b2cde437f8c4f903'||hosting.static?.directory!=='dist')throw Error('Unexpected Site identity or deployment type');
const allowed=path=>{const name=basename(path).toLowerCase();return !['.git','.exam-data','node_modules','.sites-runtime'].includes(name)&&!/^\.env(?:\.|$)/.test(name)&&!name.startsWith('.readx-backup-stage-')&&!/\.(?:sqlite(?:-wal|-shm)?|pem|key|(?:mfa|audit|data|backup|recovery)-keys\.json|recovery\.ndjson|active\.lock|write\.lock|maintenance\.lock|restore\.pending|readxbackup|readxaudit)(?:\.partial-.*)?$/.test(name);};
for(const name of ['src','public','scripts','shared','server','tests'])await cp(resolve(app,name),resolve(site,name),{recursive:true,filter:allowed});
for(const name of ['index.html','package-lock.json','postcss.config.js','tailwind.config.js','tsconfig.json','vite.config.ts'])await cp(resolve(app,name),resolve(site,name));
const pkg=JSON.parse(await readFile(resolve(app,'package.json'),'utf8'));
pkg.scripts['build:verified']=pkg.scripts.build;
pkg.scripts.build='node scripts/build-site-preview.mjs';
await writeFile(resolve(site,'package.json'),JSON.stringify(pkg,null,2)+'\n');
await writeFile(resolve(site,'scripts/build-site-preview.mjs'),`import { spawnSync } from 'node:child_process';\nconst result=spawnSync('npm run build:verified',{shell:true,stdio:'inherit',windowsHide:true,env:{...process.env,VITE_EXAM_MODE:'demo'}});\nprocess.exitCode=result.status??1;\n`);
for(const name of ['data/curriculum_2022/revisions','data/curriculum_2022/passage_drafts_batch_02.json','scripts/reading_workshop_template.html','outputs/01a138a0-43ff-7451-bf36-fcef9c677ac6/curriculum-library.html']){
  const dest=resolve(site,'content-sources',name);await mkdir(dirname(dest),{recursive:true});await cp(resolve(root,name),dest,{recursive:true,filter:allowed});
}
await writeFile(resolve(site,'.gitignore'),'node_modules/\ndist/\n*.tsbuildinfo\n.env\n.env.*\n.sites-runtime/\n.exam-data/\n*.sqlite\n*.sqlite-wal\n*.sqlite-shm\n*.mfa-keys.json\n*.audit-keys.json\n*.data-keys.json\n*.recovery-keys.json\n*.recovery.ndjson\n*.active.lock\n*.write.lock\n*.maintenance.lock\n*.restore.pending\n*.readxbackup\n*.readxaudit\n*.readxaudit.partial-*\n*.backup-keys.json\n.readx-backup-stage-*/\n*.readxbackup.partial-*\n');
console.log(JSON.stringify({project_id:hosting.project_id,checkout_path:site,mode:'public-synthetic-demo',runtimeDatabaseCopied:false}));
