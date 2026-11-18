import { DirectorDemoHub } from "./components/admin/DirectorDemoHub";
import { CurriculumLibrary } from "./components/common/CurriculumLibrary";
import React, { useState, useEffect } from "react";
import { Palette, ArrowUpRight } from "lucide-react";
import { masterData, findLesson } from "./data/lessonCatalog";
import { DemoNotice } from "./components/common/DemoNotice";
import { BrandGuide } from "./components/common/DesignSystem";
import { ReadXBrand } from "./components/brand/ReadXBrand";
import { BrandKit } from "./components/brand/BrandKit";
import { BrandHeader } from "./components/layout/BrandHeader";
import { CommonFoundationStudio } from "./components/student/ClinicActivities";
import { useCoursewareStore } from "./store/useCoursewareStore";
import { resolveActiveGradeAndSlotData } from "./services/firebaseDbService";
import { MainLandingPage } from "./components/layout/MainLandingPage";
import { StudentJourneyHub } from "./components/student/StudentJourneyHub";
import { AdaptiveClinicStudio } from "./components/student/AdaptiveClinicStudio";
import { SplitScreenStudio } from "./components/student/SplitScreenStudio";
import { LearningJourneyStudio } from "./components/student/LearningJourneyStudio";
import { ProgressiveReadingStudio } from "./components/student/ProgressiveReadingStudio";
import { CorpusReadingStudio } from "./components/student/CorpusReadingStudio";
import { revisedLessonForSlot } from "./data/corpusReading";
import { JourneyContentStatus } from "./components/common/LearningEvidenceReport";
import { JOURNEY_SLOT } from "./data/learningJourney";
import { CbtMockExamStudio } from "./components/student/CbtMockExamStudio";
import { StudentAssessmentHub } from "./components/student/StudentAssessmentHub";
import { OnboardingCatModal } from "./components/student/OnboardingCatModal";
import { ParentJourneyHub } from "./components/parent/ParentJourneyHub";
import { TeacherJourneyHub } from "./components/teacher/TeacherJourneyHub";
import { ItemBankAdminStudio } from "./components/admin/ItemBankAdminStudio";
import type { RoleType, StudentModeType } from "./types/courseware";
import { ExamPortal } from "./components/exam/ExamPortal";
import { readExamRoute } from "./services/examNavigation";

/** Public demo navigation only. This does not authorize access to production data. */
function useDemoNavigation() {
  useEffect(() => {
    let restoring = false;
    const restore = () => {
      if (readExamRoute(window.location.hash).active) return;
      const [role, mode, encodedId] = window.location.hash
        .replace(/^#\//, "")
        .split("/");
      if (!["landing", "student", "parent", "teacher", "director", "admin"].includes(role))
        return;
      restoring = true;
      const s = useCoursewareStore.getState();
      if (role === "student") {
        let id = "";
        try {
          id = decodeURIComponent(encodedId || "");
        } catch {
          /* Invalid links return to the list. */
        }
        const lesson = id ? findLesson(id) : null;
        const validMode = [
          "portal",
          "studio",
          "progressive",
          "journey",
          "clinic",
          "common",
          "cbt_exam",
          "assessment",
        ].includes(mode)
          ? (mode as StudentModeType)
          : "portal";
        if (["progressive", "journey", "assessment"].includes(validMode)) s.setStudentMode(validMode);
        else if (lesson) s.selectGradeAndSlot(lesson.grade_num, id, validMode);
        else s.setStudentMode("portal");
      }
      s.setActiveRole(role as RoleType);
      restoring = false;
    };
    restore();
    const unsubscribe = useCoursewareStore.subscribe((s, prev) => {
      if (
        restoring || readExamRoute(window.location.hash).active ||
        (s.activeRole === prev.activeRole &&
          s.studentMode === prev.studentMode &&
          s.activeSlotId === prev.activeSlotId)
      )
        return;
      const hash =
        s.activeRole === "student"
          ? "#/student/" +
            s.studentMode +
            (s.activeSlotId ? "/" + encodeURIComponent(s.activeSlotId) : "")
          : "#/" + s.activeRole;
      if (window.location.hash !== hash)
        window.history.pushState(null, "", hash);
      window.scrollTo({ top: 0, behavior: "instant" as ScrollBehavior });
    });
    window.addEventListener("popstate", restore);
    window.addEventListener("hashchange", restore);
    return () => {
      unsubscribe();
      window.removeEventListener("popstate", restore);
      window.removeEventListener("hashchange", restore);
    };
  }, []);
}

export const App: React.FC = () => {
  const {
    activeRole,
    activeGradeIdx,
    activeSlotId,
    studentMode,
    customSlotsById,
    dynamicSubskillScores,
  } = useCoursewareStore();
  const [showGuide, setShowGuide] = useState(false);
  const [brandRoute, setBrandRoute] = useState(() => window.location.hash.startsWith('#/brand'));
  const [examRoute, setExamRoute] = useState(() => readExamRoute(window.location.hash));
  useEffect(() => {
    const update = () => {
      setExamRoute(readExamRoute(window.location.hash));
      setBrandRoute(window.location.hash.startsWith('#/brand'));
    };
    window.addEventListener('hashchange', update);
    window.addEventListener('popstate', update);
    return () => { window.removeEventListener('hashchange', update); window.removeEventListener('popstate', update); };
  }, []);
  useDemoNavigation();
  const { activeGradeData, gradeSlots16, activeCommonSlot, resolutionError } =
    resolveActiveGradeAndSlotData(
      masterData,
      activeGradeIdx,
      activeSlotId,
      customSlotsById,
      dynamicSubskillScores,
    );
  const totalDbSlots =
    (masterData.expository_slots_96?.length || 0) +
    (masterData.common_slots_36?.length || 0);
  const reading = activeRole === "student" && !["portal", "assessment"].includes(studentMode);
  const revisedLesson = !customSlotsById[activeGradeData.slot_id] ? revisedLessonForSlot(activeGradeData.slot_id) : undefined;
  if (brandRoute) return <div className="rx-app" data-brand="read-x-v3"><a className="rx-skip-link" href="#main-content" onClick={e=>{e.preventDefault();document.getElementById('main-content')?.focus();}}>본문으로 건너뛰기</a><BrandKit/></div>;
  return (
    <div
      className="rx-app"
      data-brand="read-x-v3"
      data-role={examRoute.active ? examRoute.role || "student" : activeRole}
      data-grade={activeGradeIdx + 1}
    >
      <a className="rx-skip-link" href="#main-content" onClick={e => { e.preventDefault(); document.getElementById("main-content")?.focus(); }}>
        본문으로 건너뛰기
      </a>
      {!examRoute.active && activeRole !== "landing" && <DemoNotice />}
      {examRoute.active ? <ExamPortal key={examRoute.role || 'student'} requestedRole={examRoute.role}/> : activeRole === "landing" ? (
        <MainLandingPage totalDbSlots={totalDbSlots} />
      ) : (
        <>
          <BrandHeader />
          <main
            id="main-content"
            tabIndex={-1}
            className={`rx-workspace ${reading ? "rx-workspace-reading" : ""}`}
          >
            {activeRole === "student" && (
              <>
                {studentMode === "portal" && (
                  <StudentJourneyHub
                    gradeData={activeGradeData}
                    gradeSlots16={gradeSlots16}
                  />
                )}
                {studentMode === "progressive" && <ProgressiveReadingStudio />}
                {studentMode === "journey" && <LearningJourneyStudio />}
                {studentMode === "assessment" && <StudentAssessmentHub />}
                {["clinic", "studio", "common"].includes(studentMode) &&
                  (resolutionError ? (
                    <section className="rx-surface rx-records" role="alert">
                      <h1>수업을 열 수 없어요</h1>
                      <p>{resolutionError}</p>
                      <button
                        className="rx-button rx-button-primary"
                        onClick={() =>
                          useCoursewareStore.getState().setStudentMode("portal")
                        }
                      >
                        학습 목록으로
                      </button>
                    </section>
                  ) : activeCommonSlot ? (
                    <div className="rx-legacy-learning">
                      <CommonFoundationStudio
                        key={activeCommonSlot.code}
                        data={activeCommonSlot}
                      />
                    </div>
                  ) : studentMode === "clinic" ? (
                    <div className="rx-legacy-learning">
                      <AdaptiveClinicStudio
                        key={activeGradeData.slot_id}
                        gradeData={activeGradeData}
                      />
                    </div>
                  ) : revisedLesson ? (
                    <CorpusReadingStudio key={revisedLesson.id} lesson={revisedLesson}/>
                  ) : activeGradeData.slot_id === JOURNEY_SLOT &&
                    !customSlotsById[JOURNEY_SLOT] ? (
                    <LearningJourneyStudio />
                  ) : (
                    <SplitScreenStudio
                      key={activeGradeData.slot_id}
                      gradeData={activeGradeData}
                    />
                  ))}
                {studentMode === "cbt_exam" && (
                  activeGradeData.grade_num >= 5 ? <StudentAssessmentHub /> :
                  <div className="rx-legacy-learning">
                    <CbtMockExamStudio
                      gradeData={activeGradeData}
                      gradeSlots16={gradeSlots16}
                    />
                  </div>
                )}
                {studentMode === "onboarding_cat" && (
                  <OnboardingCatModal
                    gradeData={activeGradeData}
                    onClose={() =>
                      useCoursewareStore.getState().setStudentMode("portal")
                    }
                  />
                )}
              </>
            )}
            {activeRole === "parent" && (
              <ParentJourneyHub
                gradeData={activeGradeData}
                subskillMeta={masterData.subskill_16_meta}
              />
            )}
            {activeRole === "teacher" && (
              <TeacherJourneyHub data={masterData} />
            )}
            {activeRole === "director" && <DirectorDemoHub />}
            {activeRole === "admin" && (
              <div className="rx-admin-workspace">
                <JourneyContentStatus />
                <details className="rx-admin-catalog">
                  <summary>교과 지문·교육과정 통합 자료실 열기</summary>
                  <CurriculumLibrary />
                </details>
                <ItemBankAdminStudio data={masterData} />
              </div>
            )}
          </main>
        </>
      )}
      {(examRoute.active || activeRole !== "landing") && <footer className="rx-footer no-print">
        <div className="rx-container">
          <div>
            <ReadXBrand />
            <p>읽는 방법을 배우는 문해력 코스웨어</p>
          </div>
          <button className="rx-text-link" onClick={() => setShowGuide(true)}>
            <Palette size={16} />
            Read X 디자인 가이드 <ArrowUpRight size={15} />
          </button>
        </div>
      </footer>}
      {showGuide && <BrandGuide onClose={() => setShowGuide(false)} />}
    </div>
  );
};
export default App;
