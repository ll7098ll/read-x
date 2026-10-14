#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Comprehensive Publication-Grade Master Whitepaper & PRD HTML
Combines PRD_2022개정_교과개념_설명문_문해력_코스웨어.md + Google_Stitch_UIUX_Design_Prompt_Guide.md
into a unified, modern, interactive, publication-grade web application.
"""

import os
import sys
import markdown
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRD_PATH = os.path.join(BASE_DIR, "courseware", "PRD_2022개정_교과개념_설명문_문해력_코스웨어.md")
STITCH_PATH = os.path.join(BASE_DIR, "courseware", "Google_Stitch_UIUX_Design_Prompt_Guide.md")
OUT_ROOT_PATH = os.path.join(BASE_DIR, "courseware", "output", "courseware_prd_brief.html")
OUT_CW_PATH = os.path.join(BASE_DIR, "courseware", "output", "courseware_prd_brief.html")

def read_file(path):
    if not os.path.exists(path):
        print(f"Warning: {path} not found.")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def convert_md_to_html(md_text):
    md = markdown.Markdown(extensions=[
        'extra',
        'tables',
        'fenced_code',
        'toc',
        'nl2br'
    ])
    html = md.convert(md_text)
    return html

def main():
    print("Reading markdown sources...")
    prd_raw = read_file(PRD_PATH)
    stitch_raw = read_file(STITCH_PATH)

    print("Converting Markdown to HTML...")
    prd_html = convert_md_to_html(prd_raw)
    stitch_html = convert_md_to_html(stitch_raw)

    # Soup parsing and cleaning
    soup_prd = BeautifulSoup(prd_html, "html.parser")
    soup_stitch = BeautifulSoup(stitch_html, "html.parser")

    # Handle mermaid code blocks in soup
    for code_block in soup_prd.find_all("code", class_="language-mermaid"):
        pre = code_block.parent
        pre['class'] = pre.get('class', []) + ['mermaid']
        pre.string = code_block.get_text()

    for code_block in soup_stitch.find_all("code", class_="language-mermaid"):
        pre = code_block.parent
        pre['class'] = pre.get('class', []) + ['mermaid']
        pre.string = code_block.get_text()

    template = f"""<!DOCTYPE html>
<html lang="ko" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2022 개정 전교과 초등 수능형 문해력 코스웨어 종합 백서 & 마스터 PRD</title>
  
  <!-- Fonts -->
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&display=swap">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Mermaid.js for diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({{ 
      startOnLoad: true, 
      theme: 'neutral',
      themeVariables: {{
        primaryColor: '#e0e7ff',
        edgeColor: '#4f46e5',
        fontFamily: 'Pretendard, sans-serif'
      }}
    }});
  </script>

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#f0f7ff',
              100: '#e0effe',
              500: '#2563eb',
              600: '#1d4ed8',
              700: '#1e40af',
              900: '#0f172a'
            }},
            paper: '#fcfbf7'
          }},
          fontFamily: {{
            sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'system-ui', 'Roboto', 'sans-serif'],
            serif: ['Nanum Myeongjo', 'serif']
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      font-family: 'Pretendard', sans-serif;
      background-color: #f8fafc;
      color: #1e293b;
      line-height: 1.75;
    }}
    .prose-custom h1 {{
      font-size: 2.15rem;
      font-weight: 800;
      color: #0f172a;
      margin-top: 2.5rem;
      margin-bottom: 1.25rem;
      padding-bottom: 0.75rem;
      border-bottom: 3px solid #2563eb;
      letter-spacing: -0.025em;
    }}
    .prose-custom h2 {{
      font-size: 1.65rem;
      font-weight: 700;
      color: #1e293b;
      margin-top: 2.25rem;
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid #cbd5e1;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .prose-custom h3 {{
      font-size: 1.3rem;
      font-weight: 700;
      color: #334155;
      margin-top: 1.75rem;
      margin-bottom: 0.75rem;
    }}
    .prose-custom p {{
      margin-bottom: 1.15rem;
      font-size: 1.025rem;
    }}
    .prose-custom table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 1.25rem;
      margin-bottom: 1.75rem;
      font-size: 0.925rem;
      background-color: #ffffff;
      border-radius: 0.5rem;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .prose-custom th {{
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      padding: 0.85rem 1rem;
      border: 1px solid #e2e8f0;
      text-align: left;
    }}
    .prose-custom td {{
      padding: 0.75rem 1rem;
      border: 1px solid #e2e8f0;
      color: #334155;
      vertical-align: top;
    }}
    .prose-custom tr:nth-child(even) td {{
      background-color: #f8fafc;
    }}
    .prose-custom tr:hover td {{
      background-color: #f0fdf4;
    }}
    .prose-custom blockquote {{
      border-left: 4px solid #2563eb;
      background-color: #eff6ff;
      padding: 1rem 1.25rem;
      margin: 1.25rem 0;
      border-radius: 0 0.5rem 0.5rem 0;
      color: #1e3a8a;
      font-weight: 500;
    }}
    .prose-custom pre:not(.mermaid) {{
      background-color: #0f172a;
      color: #f8fafc;
      padding: 1.25rem;
      border-radius: 0.75rem;
      overflow-x: auto;
      font-size: 0.875rem;
      line-height: 1.6;
      margin-top: 1.25rem;
      margin-bottom: 1.5rem;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      border: 1px solid #334155;
    }}
    .prose-custom code:not(pre code) {{
      background-color: #e2e8f0;
      color: #0f172a;
      padding: 0.2rem 0.4rem;
      border-radius: 0.25rem;
      font-size: 0.875em;
      font-family: ui-monospace, monospace;
      font-weight: 600;
    }}
    .mermaid {{
      background-color: #ffffff;
      padding: 1.5rem;
      border-radius: 0.75rem;
      border: 1px solid #e2e8f0;
      margin: 1.5rem 0;
      box-shadow: 0 2px 4px rgba(0,0,0,0.02);
      text-align: center;
    }}
    @media print {{
      #sidebar, #top-bar {{ display: none; }}
      main {{ width: 100% !important; margin: 0 !important; padding: 0 !important; }}
      .prose-custom {{ max-width: 100% !important; }}
    }}
  </style>
</head>
<body class="bg-slate-50 min-h-screen flex flex-col">

  <!-- Top Global Header -->
  <header id="top-bar" class="sticky top-0 z-50 bg-slate-900 border-b border-slate-800 text-white px-6 py-3.5 shadow-md flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="w-9 h-9 rounded-lg bg-blue-600 flex items-center justify-center font-bold text-white text-lg shadow-sm">
        <i class="fa-solid fa-book-open-reader"></i>
      </div>
      <div>
        <h1 class="text-base font-bold text-white tracking-tight flex items-center gap-2">
          초등 수능형 문해력 「독립독자」 코스웨어 마스터 백서
          <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30">v4.1 Commercial Master</span>
        </h1>
        <p class="text-xs text-slate-400">2022 개정 9대 전 교과 설명문 100% 정합 · KICE 수능 5대 영역 직결 · 로컬 AI 비용 $0</p>
      </div>
    </div>

    <!-- Header Actions -->
    <div class="flex items-center gap-3">
      <div class="relative hidden md:block">
        <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-slate-400 text-xs"></i>
        <input type="text" id="docSearch" placeholder="문서 내 검색 (예: 알베도, 스캐폴딩)..." 
               class="bg-slate-800 text-xs text-slate-200 pl-8 pr-3 py-1.5 rounded-lg border border-slate-700 focus:outline-none focus:border-blue-500 w-64 transition">
      </div>
      <button onclick="window.print()" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg border border-slate-700 flex items-center gap-1.5 transition">
        <i class="fa-solid fa-print"></i> PDF/인쇄
      </button>
      <a href="#section-stitch" class="text-xs bg-blue-600 hover:bg-blue-500 text-white font-medium px-3.5 py-1.5 rounded-lg shadow-sm flex items-center gap-1.5 transition">
        <i class="fa-solid fa-palette"></i> 구글 스티치 UI 프롬프트
      </a>
    </div>
  </header>

  <!-- Main Container -->
  <div class="flex-1 max-w-[1720px] w-full mx-auto flex">
    
    <!-- Left Navigation Sidebar -->
    <aside id="sidebar" class="w-80 border-r border-slate-200 bg-white sticky top-[61px] h-[calc(100vh-61px)] overflow-y-auto p-5 shrink-0 hidden lg:block">
      <div class="mb-4">
        <h2 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">백서 목차 (Table of Contents)</h2>
        <div class="h-1 w-8 bg-blue-600 rounded"></div>
      </div>

      <nav class="space-y-1 text-xs font-medium text-slate-600">
        <div class="text-[11px] font-bold text-slate-400 uppercase pt-2 pb-1">Part 1. PRD 마스터 백서</div>
        <a href="#제-1-장-제품-비전-및-전-교과9대-교과-융합-교육공학-철학" class="block px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-700 transition flex items-center gap-2">
          <i class="fa-solid fa-compass w-4 text-slate-400"></i> 제 1 장. 제품 비전 & 교육공학
        </a>
        <a href="#제-2-장-2022-개정-9대-전-교과-학년학기별-설명문-커리큘럼-매트릭스" class="block px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-700 transition flex items-center gap-2">
          <i class="fa-solid fa-table-cells w-4 text-slate-400"></i> 제 2 장. 9대 전 교과 매트릭스
        </a>
        <a href="#제-3-장-9대-전-교과-특화-시각자료--svg-인터랙티브-도해조직자-명세" class="block px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-700 transition flex items-center gap-2">
          <i class="fa-solid fa-diagram-project w-4 text-slate-400"></i> 제 3 장. SVG 도해조직자
        </a>
        <a href="#제-4-장-학생학부모교사-3대-콘솔-전-교과-확장-스펙" class="block px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-700 transition flex items-center gap-2">
          <i class="fa-solid fa-users-viewfinder w-4 text-slate-400"></i> 제 4 장. 3대 콘솔 확장 스펙
        </a>
        <a href="#제-5-장-typescript-데이터-스키마-전-교과-완결-확장-typescoursewarets" class="block px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-700 transition flex items-center gap-2">
          <i class="fa-solid fa-code w-4 text-slate-400"></i> 제 5 장. TypeScript 데이터 스키마
        </a>
        <a href="#제-6-장-상용화-비즈니스-모델-및-시장-포지셔닝-go-to-market" class="block px-3 py-2 rounded-lg hover:bg-blue-50 hover:text-blue-700 transition flex items-center gap-2">
          <i class="fa-solid fa-chart-line w-4 text-slate-400"></i> 제 6 장. 상용화 BM & 로드맵
        </a>

        <div class="text-[11px] font-bold text-slate-400 uppercase pt-4 pb-1">Part 2. 구글 스티치 UI/UX 설계 가이드</div>
        <a href="#0-디자인-시스템-토큰-design-tokens--foundations" class="block px-3 py-2 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition flex items-center gap-2">
          <i class="fa-solid fa-swatchbook w-4 text-slate-400"></i> 디자인 시스템 토큰
        </a>
        <a href="#1-학생-전용-화면-상세-명세-student-views" class="block px-3 py-2 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition flex items-center gap-2">
          <i class="fa-solid fa-graduation-cap w-4 text-slate-400"></i> 👦 학생 전용 6대 화면
        </a>
        <a href="#2-학부모-안심-x-ray-리포트-화면-명세-parentreportview" class="block px-3 py-2 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition flex items-center gap-2">
          <i class="fa-solid fa-heart w-4 text-slate-400"></i> 👨‍👩‍👧 학부모 X-Ray 리포트
        </a>
        <a href="#3-교사--원장-클래스-콘솔-화면-명세-teacherconsoleview" class="block px-3 py-2 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition flex items-center gap-2">
          <i class="fa-solid fa-chalkboard-user w-4 text-slate-400"></i> 👩‍🏫 교사 클래스 콘솔
        </a>
        <a href="#4-2022-개정-전-교과-개념-정밀-삽화-및-인포그래픽-도식-uiux-명세" class="block px-3 py-2 rounded-lg hover:bg-indigo-50 hover:text-indigo-700 transition flex items-center gap-2">
          <i class="fa-solid fa-image w-4 text-slate-400"></i> 교과 정밀 삽화 & 도식
        </a>
      </nav>

      <!-- Key Stat Box in Sidebar -->
      <div class="mt-8 p-3.5 bg-slate-50 border border-slate-200 rounded-xl">
        <div class="text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-2">핵심 사양 요약</div>
        <div class="space-y-1.5 text-xs text-slate-600">
          <div class="flex justify-between"><span>교과 범위:</span><span class="font-bold text-blue-600">9대 전 교과</span></div>
          <div class="flex justify-between"><span>설명문 위계:</span><span class="font-bold text-blue-600">96개 마스터</span></div>
          <div class="flex justify-between"><span>스캐폴딩:</span><span class="font-bold text-emerald-600">5단계 자립 루프</span></div>
          <div class="flex justify-between"><span>서버 AI 비용:</span><span class="font-bold text-emerald-600">$0.00 / 학생</span></div>
          <div class="flex justify-between"><span>수능 연계:</span><span class="font-bold text-purple-600">5대 독서 전영역</span></div>
        </div>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="flex-1 p-6 lg:p-12 max-w-5xl overflow-hidden">
      
      <!-- Top Hero Banner Card -->
      <div class="bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 text-white rounded-2xl p-8 mb-10 shadow-lg border border-slate-800 relative overflow-hidden">
        <div class="absolute -right-10 -bottom-10 opacity-10 text-9xl text-white pointer-events-none">
          <i class="fa-solid fa-graduation-cap"></i>
        </div>
        <div class="relative z-10">
          <div class="inline-flex items-center gap-2 bg-blue-500/20 text-blue-300 text-xs font-semibold px-3 py-1 rounded-full border border-blue-500/30 mb-4">
            <i class="fa-solid fa-award"></i> 대한민국 최초 2022 개정 전 교과 융합 문해력 코스웨어
          </div>
          <h1 class="text-3xl lg:text-4xl font-extrabold tracking-tight mb-3 text-white">
            초등 전교과 개념 기반 수능형 문해력 코스웨어 종합 백서
          </h1>
          <p class="text-slate-300 text-sm lg:text-base max-w-3xl leading-relaxed mb-6 font-normal">
            진단받고(Diagnostic), 처방받고(Prescriptive), 멘토 시범으로 배우며(Modeling), 힌트를 스스로 소거하여(Fading), 
            마침내 수능 1등급 킬러 지문을 혼자 힘으로 뚫어내는 <strong>‘완전 독립 독자(Independent Reader)’</strong> 자립 엔지니어링 백서입니다.
          </p>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs pt-4 border-t border-slate-800/80">
            <div class="bg-slate-800/50 p-2.5 rounded-lg border border-slate-700/50">
              <div class="text-slate-400">적용 교과</div>
              <div class="font-bold text-white text-sm mt-0.5">국·수·사·과·도·실·음·미·체</div>
            </div>
            <div class="bg-slate-800/50 p-2.5 rounded-lg border border-slate-700/50">
              <div class="text-slate-400">수능 국어 직결</div>
              <div class="font-bold text-blue-300 text-sm mt-0.5">인문·사회·과학·기술·예술</div>
            </div>
            <div class="bg-slate-800/50 p-2.5 rounded-lg border border-slate-700/50">
              <div class="text-slate-400">학습 아키텍처</div>
              <div class="font-bold text-emerald-300 text-sm mt-0.5">GRR 4단계 점진적 자립</div>
            </div>
            <div class="bg-slate-800/50 p-2.5 rounded-lg border border-slate-700/50">
              <div class="text-slate-400">월간 AI API 비용</div>
              <div class="font-bold text-yellow-300 text-sm mt-0.5">$0.00 (온디바이스 AI)</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Part 1. Master PRD Whitepaper Body -->
      <article class="prose-custom bg-white p-8 lg:p-12 rounded-2xl shadow-sm border border-slate-200 mb-12">
        <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-blue-600 mb-2">
          <i class="fa-solid fa-file-lines"></i> Part 1. Commercial Product Requirements Document
        </div>
        {str(soup_prd)}
      </article>

      <!-- Part 2. Google Stitch UI/UX Design Spec Body -->
      <article id="section-stitch" class="prose-custom bg-white p-8 lg:p-12 rounded-2xl shadow-sm border border-slate-200 mb-12">
        <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-indigo-600 mb-2">
          <i class="fa-solid fa-palette"></i> Part 2. UI/UX Screen Architecture & Stitch Prompt Guide
        </div>
        {str(soup_stitch)}
      </article>

    </main>
  </div>

  <!-- Footer -->
  <footer class="bg-slate-900 border-t border-slate-800 text-slate-400 py-8 px-6 text-center text-xs">
    <div class="max-w-4xl mx-auto space-y-2">
      <div class="font-bold text-white text-sm">초등 수능형 문해력 「독립독자 (The Independent Reader)」 코스웨어</div>
      <p>본 백서는 2022 개정 교육과정 및 한국교육과정평가원(KICE) 수능 국어 영역 출제 원리에 입각하여 교육공학적으로 설계되었습니다.</p>
      <div class="text-slate-500 pt-2">© 2026 Literacy Courseware Engineering Lab. All Rights Reserved.</div>
    </div>
  </footer>

  <script>
    // Live Search in document
    const searchInput = document.getElementById('docSearch');
    if (searchInput) {{
      searchInput.addEventListener('input', function(e) {{
        const term = e.target.value.toLowerCase().trim();
        if (!term) return;
        const headings = document.querySelectorAll('main h1, main h2, main h3');
        for (const h of headings) {{
          if (h.textContent.toLowerCase().includes(term)) {{
            h.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            h.classList.add('bg-yellow-100', 'transition');
            setTimeout(() => h.classList.remove('bg-yellow-100'), 2000);
            break;
          }}
        }}
      }});
    }}
  </script>
</body>
</html>
"""

    print(f"Writing unified HTML to {OUT_ROOT_PATH}...")
    with open(OUT_ROOT_PATH, "w", encoding="utf-8") as f:
        f.write(template)

    print(f"Writing unified HTML to {OUT_CW_PATH}...")
    with open(OUT_CW_PATH, "w", encoding="utf-8") as f:
        f.write(template)

    file_size_kb = os.path.getsize(OUT_ROOT_PATH) / 1024
    print(f"Successfully generated Master Whitepaper HTML! File size: {file_size_kb:.1f} KB")

if __name__ == "__main__":
    main()
