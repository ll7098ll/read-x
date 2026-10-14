import React, { useState } from 'react';
import masterDataRaw from './data/commercialMasterData.json';
import type { CommercialMasterData } from './types/courseware';
import { useCoursewareStore } from './store/useCoursewareStore';
import { resolveActiveGradeAndSlotData } from './services/firebaseDbService';
import { StudentHeader } from './components/layout/StudentHeader';
import { ParentHeader } from './components/layout/ParentHeader';
import { TeacherHeader } from './components/layout/TeacherHeader';
import { AdminHeader } from './components/layout/AdminHeader';
import { RoleGatewayModal } from './components/layout/RoleGatewayModal';
import { MainLandingPage } from './components/layout/MainLandingPage';
import { XRaySummaryHero } from './components/layout/XRaySummaryHero';
import { StudentJourneyHub } from './components/student/StudentJourneyHub';
import { AdaptiveClinicStudio } from './components/student/AdaptiveClinicStudio';
import { SplitScreenStudio } from './components/student/SplitScreenStudio';
import { CbtMockExamStudio } from './components/student/CbtMockExamStudio';
import { OnboardingCatModal } from './components/student/OnboardingCatModal';
import { ParentJourneyHub } from './components/parent/ParentJourneyHub';
import { TeacherJourneyHub } from './components/teacher/TeacherJourneyHub';
import { ItemBankAdminStudio } from './components/admin/ItemBankAdminStudio';

const masterData = masterDataRaw as unknown as CommercialMasterData;

export const App: React.FC = () => {
  const {
    activeRole,
    activeGradeIdx,
    activeSlotId,
    studentMode,
    customSlotsById,
    dynamicSubskillScores,
  } = useCoursewareStore();

  const [showRoleGateway, setShowRoleGateway] = useState<boolean>(false);
  const [showCatModal, setShowCatModal] = useState<boolean>(false);

  // Resolve active 16-slot package and common 6 remedial units for the selected grade
  const {
    activeGradeData,
    gradeSlots16,
    gradeCommon6,
  } = resolveActiveGradeAndSlotData(
    masterData,
    activeGradeIdx,
    activeSlotId,
    customSlotsById,
    dynamicSubskillScores
  );

  const totalDbSlots =
    (masterData.expository_slots_96?.length || 96) +
    (masterData.common_slots_36?.length || 36);

  if (activeRole === 'landing') {
    return (
      <>
        <MainLandingPage totalDbSlots={totalDbSlots} />
        <RoleGatewayModal
          isOpen={showRoleGateway}
          onClose={() => setShowRoleGateway(false)}
        />
      </>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-slate-100 text-slate-900">
      {/* 1. DEDICATED ROLE-SPECIFIC NAVIGATION HEADER */}
      {activeRole === 'student' && (
        <StudentHeader
          gradeData={activeGradeData}
          onOpenRoleGateway={() => setShowRoleGateway(true)}
          onOpenCatModal={() => setShowCatModal(true)}
        />
      )}
      {activeRole === 'parent' && (
        <ParentHeader
          gradeData={activeGradeData}
          onOpenRoleGateway={() => setShowRoleGateway(true)}
        />
      )}
      {activeRole === 'teacher' && (
        <TeacherHeader
          grades={masterData.grades_data}
          onOpenRoleGateway={() => setShowRoleGateway(true)}
        />
      )}
      {activeRole === 'admin' && (
        <AdminHeader
          totalDbSlots={totalDbSlots}
          onOpenRoleGateway={() => setShowRoleGateway(true)}
        />
      )}

      {/* Main Dedicated Workspace */}
      <main className="flex-1 max-w-[1600px] w-full mx-auto px-3 sm:px-5 py-4">
        {/* Show X-Ray Hero Summary ONLY in Student (clinic) view */}
        {activeRole === 'student' && studentMode === 'clinic' && (
          <XRaySummaryHero gradeData={activeGradeData} />
        )}

        {/* ROLE 1: DEDICATED STUDENT LEARNING JOURNEY */}
        {activeRole === 'student' && (
          <>
            {studentMode === 'portal' && (
              <StudentJourneyHub
                gradeData={activeGradeData}
                gradeSlots16={gradeSlots16}
              />
            )}
            {studentMode === 'clinic' && (
              <AdaptiveClinicStudio gradeData={activeGradeData} />
            )}
            {studentMode === 'studio' && (
              <SplitScreenStudio gradeData={activeGradeData} />
            )}
            {studentMode === 'cbt_exam' && (
              <CbtMockExamStudio
                gradeData={activeGradeData}
                gradeSlots16={gradeSlots16}
              />
            )}
            {(studentMode === 'onboarding_cat' || showCatModal) && (
              <OnboardingCatModal
                gradeData={activeGradeData}
                onClose={() => {
                  setShowCatModal(false);
                  useCoursewareStore.getState().setStudentMode('portal');
                }}
              />
            )}
          </>
        )}

        {/* ROLE 2: DEDICATED PARENT JOURNEY (TODAY'S ACTIVITY, X-RAY, TRENDS, TABLE TALK) */}
        {activeRole === 'parent' && (
          <ParentJourneyHub
            gradeData={activeGradeData}
            subskillMeta={masterData.subskill_16_meta}
          />
        )}

        {/* ROLE 3: DEDICATED TEACHER & ACADEMY JOURNEY (DIAGNOSIS, RESULTS, PRESCRIPTION, TRENDS, FULL REPORT) */}
        {activeRole === 'teacher' && (
          <TeacherJourneyHub data={masterData} />
        )}

        {/* ROLE 4: DEDICATED ACADEMY B2B OPERATIONS HUB & CMS */}
        {activeRole === 'admin' && (
          <ItemBankAdminStudio data={masterData} />
        )}
      </main>

      {/* Role Switcher Persona Gateway Modal */}
      <RoleGatewayModal
        isOpen={showRoleGateway}
        onClose={() => setShowRoleGateway(false)}
      />

      {/* Clean Light Footer */}
      <footer className="bg-white text-slate-500 text-xs py-3 px-5 border-t border-slate-200 mt-8 no-print">
        <div className="max-w-[1500px] mx-auto flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <b className="text-slate-900">ReadX-Ray Pro</b> · 
            <span className="text-slate-600">
              {activeRole === 'student'
                ? '👦 학생 (과제함 · 독서 풀이 · 진도)'
                : activeRole === 'parent'
                ? '👨‍👩‍👧 학부모 (오늘 자녀 활동 · 6D 진단 · 밥상머리 코칭)'
                : activeRole === 'teacher'
                ? '👩‍🏫 교사 (25명 관제 · 맞춤 처방 · 성장 통계)'
                : '🏢 학원장 (132슬롯 CMS · 라이선스 · 상담 성적표)'}
            </span>
          </div>
          <div className="flex items-center gap-3 text-[11px] text-slate-400">
            <span>2022 개정 초등 전 교과 132슬롯 마스터</span>
            <span>·</span>
            <span>KICE 6대 오답공학 (D1~D6)</span>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default App;
