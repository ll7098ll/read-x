import test from 'node:test';
import assert from 'node:assert/strict';
import { speakKoreanText } from '../src/utils/ttsEngine';

test('읽어주기는 외부 또는 기본 음성으로 자동 대체하지 않는다',()=>{
  const previous=globalThis.window,constructor=(globalThis as any).SpeechSynthesisUtterance;
  let spoken=0,failed=0,ended=0;
  try{
    (globalThis as any).window={speechSynthesis:{cancel(){},getVoices:()=>[{lang:'ko-KR',localService:false}],speak(){spoken++;}}};
    (globalThis as any).SpeechSynthesisUtterance=function(){};
    speakKoreanText('개인정보를 포함할 수 있는 텍스트',1,()=>ended++,()=>failed++);
    assert.equal(spoken,0);assert.equal(failed,1);assert.equal(ended,1);
  }finally{(globalThis as any).window=previous;(globalThis as any).SpeechSynthesisUtterance=constructor;}
});
test('읽어주기는 로컬 한국어 음성을 명시적으로 선택한다',()=>{
  const previous=globalThis.window,constructor=(globalThis as any).SpeechSynthesisUtterance;
  const voice={lang:'ko-KR',localService:true};let spoken:any;
  try{
    (globalThis as any).window={speechSynthesis:{cancel(){},getVoices:()=>[{lang:'ko-KR',localService:false},voice],speak(u:any){spoken=u;}}};
    (globalThis as any).SpeechSynthesisUtterance=function(text:string){this.text=text;};
    speakKoreanText('<b>학습 지문</b>');assert.equal(spoken.voice,voice);assert.equal(spoken.text,'학습 지문');
  }finally{(globalThis as any).window=previous;(globalThis as any).SpeechSynthesisUtterance=constructor;}
});
