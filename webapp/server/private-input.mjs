import {createInterface} from 'node:readline/promises';
import {Writable} from 'node:stream';
export async function readPrivateJson() {
  // readline manages terminal editing, but its output sink never echoes input.
  const sink=new Writable({write(_chunk,_encoding,done){done();}}),controller=new AbortController();
  const rl=createInterface({input:process.stdin,output:sink,terminal:!!process.stdin.isTTY});let bytes=0;
  const limit=chunk=>{bytes+=Buffer.byteLength(chunk);if(bytes>8192)controller.abort();};process.stdin.on('data',limit);
  try{const line=await rl.question('',{signal:controller.signal});if(controller.signal.aborted||bytes>8192)throw Object.assign(Error('입력이 길이 제한을 넘었습니다.'),{name:'AbortError'});try{const value=JSON.parse(line);if(!value||Array.isArray(value)||typeof value!=='object')throw Error();return value;}catch{throw Error('입력한 JSON 형식을 확인해 주세요.');}}
  finally{process.stdin.removeListener('data',limit);rl.close();}
}
