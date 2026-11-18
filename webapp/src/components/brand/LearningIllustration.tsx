import React from "react";

/** ReadX's illustrated menu vocabulary. Decorative artwork always has an adjacent text label. */
export function LearningIllustration({
  kind = "book",
  className = "",
}: {
  kind?: string;
  className?: string;
}) {
  const scene =
    (
      {
        today: "book",
        practice: "book",
        student: "book",
        library: "library",
        curriculum: "library",
        admin: "library",
        vocab: "library",
        teacher: "model",
        director: "target",
        parent: "grow",
        summary: "grow",
        records: "writing",
        reports: "grow",
        exams: "search",
        report: "grow",
        goals: "target",
        history: "writing",
        review: "writing",
        notes: "writing",
        class: "guided",
        conversation: "guided",
        start: "target",
        independent: "search",
        reflection: "grow",
      } as Record<string, string>
    )[kind] || kind;
  return (
    <svg
      className={`rx-menu-art ${className}`}
      viewBox="0 0 144 104"
      fill="none"
      aria-hidden="true"
      focusable="false"
    >
      <ellipse cx="73" cy="93" rx="51" ry="6" fill="#17324D" opacity=".08" />
      <path
        d="M20 48C20 17 52 6 80 13c29-8 47 13 44 41 9 31-25 44-54 38-29 5-57-13-50-44Z"
        fill={
          scene === "grow" || scene === "guided"
            ? "#DDF4EA"
            : scene === "writing" || scene === "target"
              ? "#FFF0BF"
              : "#E1F1FC"
        }
      />
      <g
        stroke="#17324D"
        strokeWidth="2.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        {(scene === "book" || scene === "model") && (
          <>
            <path d="m26 41 44 6 48-6v43l-48 7-44-7Z" fill="#1D4ED8" />
            <path
              d="M70 85c-13-9-25-11-43-8V31c18-3 30 0 43 9 13-9 25-12 43-9v46c-18-3-30-1-43 8Z"
              fill="#FFFFFF"
            />
            <path d="M70 40v45M37 45l22 6M37 56l22 6M37 67l14 4M81 48l22-5M81 59l22-5M81 70l15-3" />
            {scene === "model" ? (
              <>
                <path
                  d="M102 13c-10 0-15 12-8 19l3 6h11l3-6c7-7 2-19-9-19Z"
                  fill="#FACC15"
                />
                <path d="M98 43h9M102 5V2M120 14l5-3M85 13l-5-3" />
              </>
            ) : (
              <>
                <path d="m98 20 10-6v31l-10-5-9 7V22Z" fill="#10B981" />
                <path d="M21 20v10M16 25h10" stroke="#0284C7" />
              </>
            )}
          </>
        )}
        {scene === "target" && (
          <>
            <circle cx="67" cy="54" r="34" fill="#FFFFFF" />
            <circle cx="67" cy="54" r="23" fill="#BDEAF7" />
            <circle cx="67" cy="54" r="11" fill="#1D4ED8" />
            <path
              d="m68 53 34-32M102 21l-1-12 12 1 1 12-12-1Z"
              fill="#10B981"
            />
            <path d="M43 82l-6 11M90 82l6 11M119 49v12M113 55h12" />
          </>
        )}
        {scene === "guided" && (
          <>
            <path d="M23 23h64v41H50L36 75V64H23Z" fill="#FFFFFF" />
            <path d="M56 46h65v35h-12v13L95 81H56Z" fill="#38BDF8" />
            <path d="M35 37h36M35 48h14M69 59h36M69 69h24" />
            <circle cx="109" cy="22" r="10" fill="#FACC15" />
          </>
        )}
        {scene === "faded" && (
          <>
            <path d="M22 89V70h28V51h29V32h29V17h17" strokeWidth="6" />
            <path d="m38 35 25-15 22 8-25 17Z" fill="#38BDF8" />
            <path
              d="m60 45 3-25M60 45l-6 12 17-15M109 16V5l17 6-17 7"
              fill="#FACC15"
            />
            <path d="m85 63 10-5M76 77l8-5" stroke="#10B981" />
          </>
        )}
        {scene === "writing" && (
          <>
            <path d="M39 17h58l10 10v64H39Z" fill="#FFFFFF" />
            <path d="M97 17v12h10M31 30h15M31 45h15M31 60h15M31 75h15M54 38h29M54 50h20M54 72h29" />
            <path d="m86 66 27-38 9 7-28 38-14 8Z" fill="#FACC15" />
            <path d="m113 28 4-6c5-5 14 2 10 7l-5 6M86 66l8 7" fill="#10B981" />
          </>
        )}
        {scene === "search" && (
          <>
            <path d="M30 17h59l12 12v60H30Z" fill="#FFFFFF" />
            <path d="M89 17v14h12M42 33h27M42 45h17M42 73h23" />
            <circle cx="84" cy="56" r="23" fill="#BDEAF7" />
            <path d="m100 74 19 19" strokeWidth="9" />
            <path d="m74 55 7 7 14-16" stroke="#087C62" strokeWidth="4" />
          </>
        )}
        {scene === "transfer" && (
          <>
            <circle cx="77" cy="49" r="34" fill="#BDEAF7" />
            <ellipse cx="77" cy="49" rx="17" ry="34" />
            <path d="M44 49h66M50 31h53M48 67h55" />
            <path
              d="M19 62c12-3 21-1 30 5 9-6 17-8 29-5v30c-12-3-20-1-29 4-9-5-18-7-30-4Z"
              fill="#FFFFFF"
            />
            <path d="M49 67v29M111 9v13M105 15h12" />
            <path d="m102 65 25 8-16 9-9-17Z" fill="#FACC15" />
          </>
        )}
        {scene === "grow" && (
          <>
            <path
              d="M30 64c16-4 28 0 42 7 14-7 26-11 42-7v26c-16-4-28 0-42 7-14-7-26-11-42-7Z"
              fill="#FFFFFF"
            />
            <path d="M72 71v25M72 66V27" />
            <path
              d="M72 53C49 55 39 42 41 25c21-1 34 10 31 28Z"
              fill="#10B981"
            />
            <path
              d="M72 39c-1-17 11-28 29-25 2 18-11 27-29 25Z"
              fill="#38BDF8"
            />
            <path d="m52 37 20 16M88 25 72 39M115 39v12M109 45h12" />
            <circle cx="29" cy="18" r="5" fill="#FACC15" stroke="none" />
          </>
        )}
        {scene === "library" && (
          <>
            <path d="M24 84h99M28 26h20v56H28Z" fill="#38BDF8" />
            <path d="M51 18h23v64H51Z" fill="#FFFFFF" />
            <path d="m81 29 19-5 16 55-19 5Z" fill="#10B981" />
            <path d="M34 37h8M34 67h8M57 31h11M57 39h11M57 70h11M88 39l9-2M96 67l9-2" />
            <path d="M112 13v12M106 19h12" stroke="#B08010" />
          </>
        )}
      </g>
    </svg>
  );
}
