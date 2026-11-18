import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const outputDir=path.join(root,'outputs','01a138a0-43ff-7451-bf36-fcef9c677ac6');
const read=async name=>JSON.parse(await fs.readFile(path.join(root,'data','curriculum_2022',name),'utf8'));
const [reg,std,corpus,queue]=await Promise.all(['curriculum_registry.json','achievement_standards.json','passage_corpus.json','passage_writing_queue.json'].map(read));
const passageEnd=corpus.passages.length+5;
const wb=Workbook.create();
const sheets=Object.fromEntries(['현황','학기별지도','개념원장','성취기준','지문목록'].map(n=>[n,wb.worksheets.add(n)]));
const col=n=>String.fromCharCode(65+n);
const green='#173F43', pale='#EAF2ED', amber='#FFF3D6', ink='#24343B';
function base(sheet,title,note,widths,last){
  sheet.showGridLines=false; sheet.tabColor=green;
  const range=sheet.getRange(`A1:${col(widths.length-1)}${last}`);
  range.format.font={name:'Malgun Gothic',size:11,color:ink};
  range.format.verticalAlignment='center'; range.format.wrapText=true;
  widths.forEach((w,i)=>sheet.getRange(`${col(i)}1:${col(i)}${last}`).format.columnWidthPx=w);
  sheet.getRange('A1').values=[[title]];
  sheet.getRange('A1').format.font={name:'Malgun Gothic',size:20,bold:true,color:green};
  sheet.getRange(`A1:${col(widths.length-1)}1`).format.rowHeightPx=42;
  sheet.getRange(`A1:${col(widths.length-1)}1`).format.wrapText=false;
  sheet.getRange('A2').values=[[note]];
  sheet.getRange(`A2:${col(widths.length-1)}2`).format.wrapText=false;
  sheet.getRange(`A2:${col(widths.length-1)}2`).format.rowHeightPx=30;
  sheet.getRange('A2').format.font={size:10,color:'#67766E'};
}
function dataSheet(name,title,note,headers,rows,widths,tableName){
  const s=sheets[name],end=rows.length+5;
  base(s,title,note,widths,end);
  s.getRange(`A5:${col(headers.length-1)}${end}`).values=[headers,...rows];
  const t=s.tables.add(`A5:${col(headers.length-1)}${end}`,true,tableName);t.style='TableStyleMedium4';
  s.getRange(`A5:${col(headers.length-1)}5`).format={fill:green,font:{bold:true,color:'#FFFFFF'},rowHeightPx:38};
  rows.forEach((r,i)=>{
    let lines=Math.max(...r.map((v,c)=>Math.ceil(String(v??'').length/Math.max(5,Math.floor(widths[c]/11)))));
    s.getRange(`A${i+6}:${col(headers.length-1)}${i+6}`).format.rowHeightPx=Math.max(42,lines*19+14);
  });
  s.freezePanes.freezeRows(5);
  return s;
}
const purpose={guided_practice:'함께 배우기',transfer_check:'새 글에서 확인',legacy_unclassified:'기존 용도 미분류'};
const placements=Object.fromEntries(reg.placements.map(p=>[p.id,p]));
dataSheet('학기별지도','학년·학기별 교과 개념 지도','24개 묶음은 출판사 단원 목차 확인, 6개는 통합 주제 확인, 66개는 편집 배치안. 개별 개념의 대응은 검수 전입니다.',
 ['학년','학기','교과','단원 또는 편집 묶음','개념·기능 후보','배치 확인 상태','관련 기준 묶음','개념 수','출처'],
 reg.placements.map(p=>[p.grade,p.semester,p.subject,p.units,p.conceptNames.join(' · '),p.placementStatus,p.relatedStandardIds.join(', '),p.conceptIds.length,reg.sources[p.placementSourceId].url]),
 [60,60,110,260,460,200,280,72,340],'SemesterMap');
dataSheet('개념원장','교과 개념·기능 후보와 집필 현황','같은 교과의 동일 명칭을 하나로 묶은 편집 후보입니다. 공식 개념 총수나 학년 간 난도 동일성을 뜻하지 않습니다.',
 ['개념 ID','교과','개념·기능 후보','학기 배치 후보','집필 상태','신규 초안 ID','개념 대응 검수','검토 메모'],
 queue.map(q=>[q.conceptId,q.subject,q.conceptName,q.candidatePlacementIds.map(id=>`${placements[id].grade}-${placements[id].semester}`).join(', '),q.writingState==='not_started'?'집필 전':'초안 검수 전',q.existingNewDraftIds.join(', '),'성취기준 개별 대응 검수 전','']),
 [170,110,245,120,130,220,230,320],'ConceptInventory');
sheets['개념원장'].getRange(`H6:H${queue.length+5}`).format.fill='#FFFBE8';
dataSheet('성취기준','2022-33호 초등 성취기준 원장','사회·음악 일부개정 대조 전. 수식 객체·표 배열은 추출에서 빠질 수 있으므로 원본 HWP를 확인합니다.',
 ['코드','교과','학년군','영역','성취기준 추출문','원문 파일 ID','추출문 행','학기 묶음 연결 상태'],
 std.map(s=>[s.id,s.subject,s.gradeBand.join('~'),s.area,s.statement,s.sourceId,s.sourceLine,reg.unmappedStandardIds.includes(s.id)?'미연결':'관련 묶음 연결']),
 [125,105,72,190,590,190,90,170],'AchievementStandards');
sheets['성취기준'].getRange('A3').values=[[reg.sources.MOE.url]];
sheets['성취기준'].getRange('A3:H3').format.wrapText=false;
for(let i=0;i<std.length;i++)if(reg.unmappedStandardIds.includes(std[i].id))sheets['성취기준'].getRange(`H${i+6}`).format.fill=amber;
dataSheet('지문목록','신규·기존 지문 목록','원문은 전체 자료실에서, 2차 집필의 진단 문항·사고 활동·관찰 기록은 수업자료 HTML에서 확인합니다.',
 ['지문 ID','학년','학기','교과','제목','구분','용도','목표 계열 ID','글자 수','검수 상태','개념 소재','2차 진단문항 수','검토 메모'],
 corpus.passages.map(p=>[p.id,p.grade,p.semester??'미확인',p.subject,p.title,p.origin,purpose[p.purpose],p.goalIds.join(', '),p.charCount,p.editorialReview?'자체 검토·교사 검수 전':'검수 전',p.conceptNames.join(', '),p.diagnostic?.items.length??0,'']),
 [225,58,78,105,350,105,170,160,85,180,230,130,300],'PassageIndex');
sheets['지문목록'].getRange(`M6:M${passageEnd}`).format.fill='#FFFBE8';

const s=sheets['현황'];
base(s,'교과 개념과 읽기 지문 제작 현황','초등 1~6학년 · 2026.10.14 작성 · 학원·공부방용 콘텐츠 편집 원장',[200,105,155,115,190,115,200,115],37);
s.getRange('A4:H4').values=[['개념·기능 후보',null,'성취기준',null,'신규 지문',null,'기존 지문',null]];
s.getRange('B4').formulas=[[`=COUNTA('개념원장'!A6:A${queue.length+5})`]];
s.getRange('D4').formulas=[[`=COUNTA('성취기준'!A6:A${std.length+5})`]];
s.getRange('F4').formulas=[[`=COUNTIFS('지문목록'!F6:F${passageEnd},"신규 집필")`]];
s.getRange('H4').formulas=[[`=COUNTIFS('지문목록'!F6:F${passageEnd},"기존 자료")`]];
s.getRange('A4:H4').format.fill=pale;s.getRange('A4:H4').format.rowHeightPx=54;
['B4','D4','F4','H4'].forEach(a=>s.getRange(a).format.font={size:22,bold:true,color:green});
s.getRange('A6:H6').values=[['학기 묶음',null,'배치 미연결 기준',null,'총 지문',null,'판매용 검수 완료',null]];
s.getRange('B6').formulas=[[`=COUNTA('학기별지도'!A6:A101)`]];
s.getRange('D6').formulas=[[`=COUNTIFS('성취기준'!H6:H616,"미연결")`]];
s.getRange('F6').formulas=[['=SUM(F4,H4)']];
s.getRange('H6').formulas=[[`=COUNTIFS('지문목록'!J6:J${passageEnd},"검수 완료")`]];
s.getRange('A6:H6').format.rowHeightPx=44;
s.getRange('A8').values=[['826개는 개념·기능 후보이며 지문 수가 아닙니다. 판매용으로 승인된 지문은 아직 없습니다.']];
s.getRange('A8:H8').format.wrapText=false;s.getRange('A8:H8').format.rowHeightPx=30;s.getRange('A8:H8').format.fill=amber;
s.getRange('A10:H10').values=[['학년','학기','교과 묶음 수','개념 배치 수','신규 초안 수','함께 배우기','새 글에서 확인','승인 지문 수']];
s.getRange('A10:H10').format={fill:green,font:{bold:true,color:'#FFFFFF'},rowHeightPx:36};
for(let g=1;g<=6;g++)for(let t=1;t<=2;t++){
 const r=9+g*2+t-1;
 s.getRange(`A${r}:B${r}`).values=[[g,t]];
 s.getRange(`C${r}:H${r}`).formulas=[[
  `=COUNTIFS('학기별지도'!A$6:A$101,A${r},'학기별지도'!B$6:B$101,B${r})`,
  `=SUMIFS('학기별지도'!H$6:H$101,'학기별지도'!A$6:A$101,A${r},'학기별지도'!B$6:B$101,B${r})`,
  `=COUNTIFS('지문목록'!B$6:B$${passageEnd},A${r},'지문목록'!C$6:C$${passageEnd},B${r},'지문목록'!F$6:F$${passageEnd},"신규 집필")`,
  `=COUNTIFS('지문목록'!B$6:B$${passageEnd},A${r},'지문목록'!C$6:C$${passageEnd},B${r},'지문목록'!G$6:G$${passageEnd},"함께 배우기")`,
  `=COUNTIFS('지문목록'!B$6:B$${passageEnd},A${r},'지문목록'!C$6:C$${passageEnd},B${r},'지문목록'!G$6:G$${passageEnd},"새 글에서 확인")`,
  `=COUNTIFS('지문목록'!B$6:B$${passageEnd},A${r},'지문목록'!C$6:C$${passageEnd},B${r},'지문목록'!J$6:J$${passageEnd},"검수 완료")`
 ]];
 if(g%2===1)s.getRange(`A${r}:H${r}`).format.fill='#F1F5F2';
 s.getRange(`A${r}:H${r}`).format.rowHeightPx=30;
}
s.getRange('A24').values=[['개념 배치 수는 학기 간 중복을 포함합니다. 신규 글 2편은 같은 목표 계열을 서로 다른 소재에서 다룹니다.']];
s.getRange('A26').values=[['확인된 단원 배치: 수학·사회·과학 3~6학년 24개 묶음. 통합교과 1학년의 6개 묶음은 주제 배치만 확인.']];
s.getRange('A28').values=[['나머지 66개 묶음은 편집안입니다. 국가 성취기준의 학년군과 교과서의 학년·학기 배치를 구분합니다.']];
s.getRange('A30').values=[['후속 검수: 일부개정 원문 대조 → 학기·개념 대응 확인 → 지문 사실·난도·세부목표 검수 → 학생 반응 보정.']];
s.getRange('A32').values=[['검토 메모는 개념원장·지문목록의 옅은 노란색 칸에 남길 수 있습니다.']];
s.getRange('A34').values=[['이 파일은 현재 데이터의 검토용 스냅샷입니다. 메모는 프로젝트 JSON에 자동 저장되지 않습니다.']];
for(const row of [24,26,28,30,32,34]){s.getRange(`A${row}:H${row}`).format.wrapText=false;s.getRange(`A${row}:H${row}`).format.rowHeightPx=30;}
s.freezePanes.freezeRows(10);
wb.recalculate();
const check=await wb.inspect({kind:'table',range:'현황!A4:H22',include:'values,formulas',tableMaxRows:19,tableMaxCols:8,maxChars:9500});
await fs.writeFile(path.join(outputDir,'workbook-inspection.ndjson'),check.ndjson);
const vals=s.getRange('A4:H6').values;
if(vals[0][1]!==reg.concepts.length||vals[0][3]!==std.length||vals[0][5]!==corpus.counts.newDrafts||vals[0][7]!==corpus.counts.legacyDrafts||vals[2][1]!==reg.placements.length||vals[2][3]!==reg.unmappedStandardIds.length||vals[2][5]!==corpus.passages.length||vals[2][7]!==0)throw Error('Summary formulas failed: '+JSON.stringify(vals));
for(let r=11;r<=22;r++){const g=Math.floor((r-11)/2)+1,t=(r-11)%2+1;const drafts=corpus.passages.filter(p=>p.origin==='신규 집필'&&p.grade===g&&p.semester===t);const expected=[drafts.length,drafts.filter(p=>p.purpose==='guided_practice').length,drafts.filter(p=>p.purpose==='transfer_check').length,0];const v=s.getRange(`E${r}:H${r}`).values[0];if(v.join(',')!==expected.join(','))throw Error(`Grade-semester formula mismatch: ${r}`);}
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:20},maxChars:2500});
console.log(errors.ndjson);
for(const [name,range]of [['현황','A1:H34'],['학기별지도','A1:F9'],['개념원장','A1:H10'],['성취기준','A1:H10'],['지문목록','E28:M34']]){
 const preview=await wb.render({sheetName:name,range,scale:1,format:'png'});
 await fs.writeFile(path.join(outputDir,`preview-${name}.png`),new Uint8Array(await preview.arrayBuffer()));
}
const xlsx=await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(path.join(outputDir,process.argv[2]||'교과개념_학기별지도_지문원장.xlsx'));
console.log(JSON.stringify({sheets:Object.keys(sheets),concepts:queue.length,standards:std.length,passages:corpus.passages.length,formulaChecks:'passed'}));
