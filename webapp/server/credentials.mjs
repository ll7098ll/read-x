import {randomBytes,scryptSync,timingSafeEqual} from 'node:crypto';
export const passwordHash=password=>{const salt=randomBytes(16).toString('hex');return `${salt}:${scryptSync(password,salt,32).toString('hex')}`;};
export const passwordOK=(password,stored)=>{
  if(typeof password!=='string'||password.length>128||typeof stored!=='string')return false;
  const parts=stored.split(':');if(parts.length!==2||!/^[a-f0-9]{32}$/i.test(parts[0])||!/^[a-f0-9]{64}$/i.test(parts[1]))return false;
  return timingSafeEqual(scryptSync(password,parts[0],32),Buffer.from(parts[1],'hex'));
};
