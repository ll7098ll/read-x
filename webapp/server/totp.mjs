import { createHmac, timingSafeEqual } from 'node:crypto';
const alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
export function encodeBase32(data) {
  let bits=0,value=0,result='';for(const byte of data){value=(value<<8)|byte;bits+=8;while(bits>=5){result+=alphabet[(value>>>(bits-5))&31];bits-=5;}}
  if(bits)result+=alphabet[(value<<(5-bits))&31];return result;
}
export function decodeBase32(secret) {
  if(typeof secret!=='string'||!/^[A-Z2-7]{16,128}$/.test(secret))throw Error('Invalid TOTP secret');
  let bits=0,value=0;const result=[];for(const char of secret){value=(value<<5)|alphabet.indexOf(char);bits+=5;if(bits>=8){result.push((value>>>(bits-8))&255);bits-=8;}}return Buffer.from(result);
}
export function totp(secret,at,{digits=6,algorithm='sha1',period=30}={}) {
  if(!Number.isSafeInteger(at)||at<0||![6,8].includes(digits)||!['sha1','sha256','sha512'].includes(algorithm)||period!==30)throw Error('Invalid TOTP parameters');
  const counter=Buffer.alloc(8);counter.writeBigUInt64BE(BigInt(Math.floor(at/1000/period)));
  const digest=createHmac(algorithm,decodeBase32(secret)).update(counter).digest(),offset=digest[digest.length-1]&15;
  return String((digest.readUInt32BE(offset)&0x7fffffff)%10**digits).padStart(digits,'0');
}
export function matchTotp(secret,code,at,lastCounter=-1) {
  if(typeof code!=='string'||!/^\d{6}$/.test(code))return null;
  const current=Math.floor(at/30000),given=Buffer.from(code);let matched=null;
  for(const counter of [current,current-1,current+1]){
    if(counter<0)continue;const expected=Buffer.from(totp(secret,counter*30000));
    const equal=timingSafeEqual(given,expected);if(matched===null&&equal&&counter>lastCounter)matched=counter;
  }
  return matched;
}
