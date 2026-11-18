import {createHash} from 'node:crypto';
const hash=s=>createHash('sha256').update(s).digest('hex');
export function requiredRetained(db,id){
 const m=db.prepare('SELECT * FROM retained_personal_records WHERE id=?').get(id),b=db.prepare('SELECT payload FROM retained_personal_bodies WHERE id=?').get(id);if(!m||!b)throw Error('복구에 필요한 별도 보존 자료가 없습니다.');
 return {id,metadataHash:hash(m.payload),bodyHash:hash(b.payload),expiresAt:m.expires_at,revision:m.revision};
}
export function erasureRecoveryEvent(db,r,role){
 const x=r.execution;return {type:'erase_owned',tenantId:r.tenantId,subjectId:r.subjectId,role,jobId:x.jobId,requestId:r.id,requesterId:r.requesterId,at:x.at,execution:{kind:x.kind,jobId:x.jobId,scope:x.scope,at:x.at,planHash:x.planHash,groups:x.groups,archiveIds:x.archiveIds,residuals:Object.fromEntries(Object.entries(x.residuals).map(([k,v])=>[k,{until:v.until}])),liveVerification:true,mediaAndBackupsVerified:false},required:x.archiveIds.map(id=>requiredRetained(db,id))};
}
