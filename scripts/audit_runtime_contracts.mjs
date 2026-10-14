// Render probes of existing components and bundled data. Does not alter application sources.
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const webapp = path.join(root, 'webapp');
const require = createRequire(path.join(webapp, 'package.json'));
const esbuild = require('esbuild');
const out = path.join(root, 'output', 'audit');
await fs.mkdir(out, { recursive: true });
const probe = `
import React from 'react';
import {renderToStaticMarkup} from 'react-dom/server';
import data from './src/data/commercialMasterData.json';
import {resolveActiveGradeAndSlotData,validateSlotPackage} from './src/services/firebaseDbService';
import {AdaptiveClinicStudio} from './src/components/student/AdaptiveClinicStudio';
import {EBSRQuestionCard} from './src/components/tei/EBSRQuestionCard';
import {GraphicOrganizerBuilder} from './src/components/tei/GraphicOrganizerBuilder';
import {WritingWorkbench} from './src/components/tei/WritingWorkbench';
import {InlineClozeBuilder} from './src/components/tei/InlineClozeBuilder';
const results=[];
let reactWarnings=0;
const oldError=console.error;
console.error=()=>{reactWarnings++;};
for (const slot of data.expository_slots_96) {
  const {activeGradeData}=resolveActiveGradeAndSlotData(data,slot.grade_num-1,slot.slot_id,{});
  const drill=slot.prescription_clinic.step1_2_drill;
  const probes=[
    ['clinic',AdaptiveClinicStudio,{gradeData:activeGradeData}],
    ['ebsr',EBSRQuestionCard,{data:slot.commercial.ebsr_question}],
    ['organizer',GraphicOrganizerBuilder,{data:slot.commercial.graphic_organizer}],
    ['writing',WritingWorkbench,{data:slot.commercial.writing_workbench}],
    ['cloze',InlineClozeBuilder,{promptTitle:drill.think_aloud_prompt,sentences:drill.cloze_sentences,blanks:drill.blanks}],
  ];
  const row={slotId:slot.slot_id,grade:slot.grade_num,probes:{},cmsValidation:validateSlotPackage(slot)};
  for(const [name,Component,props] of probes){
    try{renderToStaticMarkup(React.createElement(Component,props));row.probes[name]={ok:true};}
    catch(e){row.probes[name]={ok:false,error:e.message};}
  }
  results.push(row);
}
console.error=oldError;
const failureCounts={};
for(const row of results)for(const [name,r] of Object.entries(row.probes))if(!r.ok)failureCounts[name]=(failureCounts[name]||0)+1;
const cmsPassButRenderFail=results.filter(row=>row.cmsValidation.isValid&&Object.values(row.probes).some(r=>!r.ok)).map(r=>r.slotId);
module.exports={scope:'96 slots x 5 component initial server renders; no browser interaction or educational validation',failureCounts,reactWarnings,cmsPassButRenderFail,results};
`;
const built = await esbuild.build({
  stdin: { contents: probe, resolveDir: webapp, sourcefile: 'audit-probe.tsx', loader: 'tsx' },
  bundle: true, platform: 'node', format: 'cjs', write: false, logLevel: 'silent',
  define: { 'import.meta.env': '{}' },
});
const probePath = path.join(out, 'runtime-probe.generated.cjs');
await fs.writeFile(probePath, built.outputFiles[0].contents);
const result = require(probePath);
await fs.unlink(probePath);
await fs.writeFile(path.join(out, 'runtime-contracts.json'), JSON.stringify(result, null, 2));
const appBuild = await esbuild.build({
  entryPoints: [path.join(webapp, 'src/main.tsx')], bundle: true, platform: 'browser',
  write: false, metafile: true, logLevel: 'silent', outdir: path.join(out, 'unused-build'),
  define: { 'process.env.NODE_ENV': '"production"' }, minify: true,
});
await fs.writeFile(path.join(out, 'import-graph.json'), JSON.stringify(appBuild.metafile, null, 2));
const contributed = new Set(Object.values(appBuild.metafile.outputs).flatMap(o => Object.entries(o.inputs).filter(([k,v])=>v.bytesInOutput>0).map(([k])=>k.replaceAll('\\\\','/'))));
const zeroContribution = Object.keys(appBuild.metafile.inputs).filter(k=>k.includes('webapp/src/')&&!contributed.has(k.replaceAll('\\\\','/')));
console.log(JSON.stringify({failureCounts: result.failureCounts, cmsPassButRenderFail: result.cmsPassButRenderFail.length,zeroContribution},null,2));
