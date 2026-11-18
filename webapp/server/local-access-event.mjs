import {randomUUID} from 'node:crypto';
import {createAccessLog} from './access-log.mjs';
// Call inside the same transaction as local account administration.
export function recordLocalAccess({db,dbPath,user,at,action}){
 const log=createAccessLog({db,dbPath});
 log.append({requestId:randomUUID(),tenantId:user.tenantId,at,actorId:'local-server-admin',actorRole:'server-administrator',method:'LOCAL',route:action,resourceId:user.id,category:'authentication',status:200,bytes:0,address:null,addressSource:'local-server',subjects:[user.id],records:1});
}
