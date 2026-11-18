// Public editorial metadata only; no passages, answers or scoring keys.
export const learningGrades=[1,2,3,4,5,6];
export const courseOrder=['words','evidence','connect','interpret','evaluate','integrate'];
export const courseNames={words:'뜻 익히기',evidence:'단서 짚기',connect:'관계 엮기',interpret:'의미 풀기',evaluate:'근거 따지기',integrate:'새롭게 엮기'};
export const gradeProfiles=Object.fromEntries(learningGrades.map(grade=>[grade,{
 grade,commonCount:grade<=2?6:12,branchCount:grade<=2?6:8,explanationCount:2,
 totalCount:grade<=2?14:22,estimatedMinutes:grade<=2?'15~20':'25~35',
 oralAllowed:grade<=2,choiceCount:grade<=2?3:4,
 explanationPrompt:grade<=2?'글을 보고 왜 그렇게 생각했는지 짧게 쓰거나 선생님에게 말해 주세요.':'두 가지 이상의 정보와 근거를 연결해 설명해 주세요.',
 editorialFocus:grade===1?'생활 낱말·짧은 문장·행동의 앞뒤':grade===2?'문장 연결·생활 규칙·간단한 조건':grade===3?'문단의 중심·비교·인과':grade===4?'문단 사이 관계·조건·예외':grade===5?'추상어·자료 비교·근거의 범위':'복합 조건·자료의 충돌·판단의 한계'
} ]));
export const courseLessonIds={
 1:['P22-G1-S1-01','P22-G1-S1-02','passage:G1-EXP-V1-1:001','P22-G1-S2-02','passage:G1-EXP-V1-2:001','passage:G1-EXP-V1-4:001','P22-G1-S2-01','passage:G1-EXP-V1-3:001','passage:G1-EXP-V2-2:001','passage:G1-EXP-V2-1:001','passage:G1-EXP-V3-1:001','passage:G1-EXP-V2-4:001','passage:G1-EXP-W2:001','passage:G1-EXP-V2-3:001','passage:G1-EXP-W4:001','passage:G1-EXP-V3-3:001','passage:G1-EXP-W1:001','passage:G1-EXP-W5:001'],
 2:['P22-G2-S1-02','passage:G2-EXP-V1-2:001','passage:G2-EXP-V1-4:001','P22-G2-S2-01','passage:G2-EXP-V1-1:001','passage:G2-EXP-V1-3:001','P22-G2-S1-01','passage:G2-EXP-V2-2:001','passage:G2-EXP-V2-3:001','passage:G2-EXP-V2-1:001','passage:G2-EXP-V3-2:001','passage:G2-EXP-V3-3:001','P22-G2-S2-02','passage:G2-EXP-V2-4:001','passage:G2-EXP-W4:001','passage:G2-EXP-V3-1:001','passage:G2-EXP-W1:001','passage:G2-EXP-W5:001'],
 3:['P22-G3-S2-01','P22-G3-S2-02','passage:G3-EXP-V1-2:001','P22-G3-S1-02','P22-B02-G3-M-02','passage:G3-EXP-V2-4:001','P22-G3-S1-01','passage:G3-EXP-V2-1:001','passage:G3-EXP-V3-1:001','passage:G3-EXP-V2-2:001','passage:G3-EXP-V3-3:001','P22-B02-G3-S-01','passage:G3-EXP-V2-3:001','passage:G3-EXP-V3-2:001','P22-B02-G3-S-02','passage:G3-EXP-W1:001','passage:G3-EXP-W2:001','passage:G3-EXP-W5:001'],
 4:['passage:G4-EXP-V2-2:001','passage:G4-EXP-V1-1:001','passage:G4-EXP-V1-3:001','P22-G4-S1-02','P22-B02-G4-M-01','passage:G4-EXP-V1-4:001','P22-G4-S1-01','P22-B02-G4-C-01','P22-B02-G4-C-02','P22-G4-S2-02','passage:G4-EXP-V2-1:001','passage:G4-EXP-V2-4:001','P22-G4-S2-01','P22-B02-G4-S-02','passage:G4-EXP-V3-2:001','passage:G4-EXP-W1:001','passage:G4-EXP-W2:001','passage:G4-EXP-W5:001'],
 5:['P22-G5-S1-01','passage:G5-EXP-V1-1:001','passage:G5-EXP-V1-3:001','P22-G5-S1-02','P22-B02-G5-M-01','passage:G5-EXP-V2-1:001','passage:G5-EXP-V1-2:001','P22-B02-G5-C-02','passage:G5-EXP-V2-4:001','passage:G5-EXP-V2-2:001','passage:G5-EXP-V2-3:001','passage:G5-EXP-V3-2:001','P22-G5-S2-01','P22-G5-S2-02','P22-B02-G5-S-02','passage:G5-EXP-W1:001','passage:G5-EXP-W2:001','passage:G5-EXP-W5:001'],
 6:['passage:G6-EXP-V1-1:001','passage:G6-EXP-V1-4:001','passage:G6-EXP-V2-1:001','P22-G6-S1-01','P22-B02-G6-M-01','passage:G6-EXP-V3-3:001','passage:G6-EXP-V1-2:001','P22-B02-G6-S-01','P22-B02-G6-C-01','passage:G6-EXP-V1-3:001','passage:G6-EXP-V2-2:001','P22-B02-G6-C-02','P22-G6-S1-02','passage:G6-EXP-V3-2:001','P22-B02-G6-S-02','P22-G6-S2-01','passage:G6-EXP-W1:001','passage:G6-EXP-W2:001']
};
export const firstCourseLessons=Object.fromEntries(learningGrades.map(g=>[g,Object.fromEntries(courseOrder.map((c,i)=>[c,'corpus-v2:'+courseLessonIds[g][i*3]]))]));
