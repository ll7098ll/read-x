// Shared by authorized live erasure and quarantined recovery replay.
// The caller owns the SQLite transaction and must separately preserve legal holds.
export const ownedTables=['learning_runs','learning_releases','learning_placements','learning_courses','pilot_runs'];
export function eraseOwned({db,state:s,tenantId,subjectId,tombstone,keepRequestId}){
 const belongs=v=>(!v.tenantId||v.tenantId===tenantId)&&v.studentId===subjectId;
 for(const key of ['attempts','followups','attendance','consultations','enrollments'])s[key]=(s[key]||[]).filter(v=>!belongs(v));
 for(const key of ['candidates','verifications','consents'])s.privacy[key]=s.privacy[key].filter(v=>v.tenantId!==tenantId||v.studentId!==subjectId&&v.parentId!==subjectId);
 for(const table of ownedTables)db.prepare(`DELETE FROM ${table} WHERE tenant_id=? AND json_extract(body,'$.studentId')=?`).run(tenantId,subjectId);
 for(const a of s.assignments.filter(a=>a.tenantId===tenantId))a.studentIds=a.studentIds.filter(id=>id!==subjectId);
 for(const table of ['learning_assignments','pilot_sessions'])for(const row of db.prepare(`SELECT id,body FROM ${table} WHERE tenant_id=?`).all(tenantId)){
  const a=JSON.parse(row.body);if(a.studentIds.includes(subjectId)){a.studentIds=a.studentIds.filter(id=>id!==subjectId);db.prepare(`UPDATE ${table} SET body=? WHERE id=? AND tenant_id=?`).run(JSON.stringify(a),row.id,tenantId);}
 }
 for(const row of db.prepare('SELECT id FROM privacy_requests WHERE tenant_id=? AND subject_id=? AND id<>?').all(tenantId,subjectId,keepRequestId)){
  db.prepare('DELETE FROM privacy_request_bundles WHERE tenant_id=? AND request_id=?').run(tenantId,row.id);db.prepare('DELETE FROM privacy_requests WHERE tenant_id=? AND id=?').run(tenantId,row.id);
 }
 const revoked=new Set([subjectId]);for(const u of s.users.filter(u=>u.tenantId===tenantId&&u.childIds.includes(subjectId))){u.childIds=u.childIds.filter(id=>id!==subjectId);u.revision++;delete u.deviceDraftKey;revoked.add(u.id);}
 for(const [id,session]of Object.entries(s.sessions))if(revoked.has(session.userId))delete s.sessions[id];
 s.recoveryCodes=(s.recoveryCodes||[]).filter(r=>r.userId!==subjectId);s.mfaRecoveries=(s.mfaRecoveries||[]).filter(r=>r.userId!==subjectId);
 const index=s.users.findIndex(u=>u.tenantId===tenantId&&u.id===subjectId);if(index<0)s.users.push(tombstone);else s.users[index]=tombstone;
}
