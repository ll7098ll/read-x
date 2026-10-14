#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Ultimate Master Whitepaper & Product Requirements Document (PRD) HTML
[ReadX (리드엑스) - 2022 개정 전교과 설명문 수능형 문해력 코스웨어 완전판 명세서]

Key Features:
1. Brand: ReadX (리드엑스) / ReadX-Ray Pro
2. Pure Expository (100% 비문학 설명문 특화, 2022 개정 9대 전 교과)
3. Reading Process & Cognitive Scaffolding (Think-Aloud, 4단계 점진적 어노테이션)
4. AI Hype Toned Down: Deterministic Rule Engine + Kiwi-wasm + $0 On-Device Assist (Chrome Gemini Nano)
5. 24 Micro-Screens across 4 Stakeholders (Student 9, Parent 5, Teacher 5, Academy Director 5) with ASCII Wireframes & Google Stitch Prompts
6. 7 Curriculum Concept Schematics (Music, Art, PE, Moral, Practical Arts, Science, Social Studies)
7. Full Hierarchical Detailed TOC (Sidebar Accordion & In-Page Directory) with Instant Search
8. Interactive Lightbox Zoom Modal for all diagrams, wireframes, and schematics
"""

import os
import sys
import re
import markdown
from bs4 import BeautifulSoup
import shutil

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = r"C:\Users\user\.gemini\antigravity\brain\ccc89a7b-44b3-4691-b4f5-ff3f3a741723"

MASTER_SECTIONS = [
    {
        "part_id": "part-cw-prd",
        "part_badge": "플래그십 마스터 PRD v6.0",
        "part_title": "Part 1. [플래그십 마스터 PRD] 2022 개정 9대 전 교과 설명문 문해력 코스웨어 「ReadX」 제품요구서",
        "file": os.path.join(BASE_DIR, "courseware", "PRD_2022개정_교과개념_설명문_문해력_코스웨어.md"),
        "icon": "fa-layer-group",
        "color": "indigo",
        "desc": "설명문 목표분석 ➔ Why 시장위기 & 담백한 AI설계 ➔ 과정독서 ➔ 24개 화면 요약 ➔ X-Ray 수식 ➔ $0 로컬 AI 소스코드 ➔ GTM"
    },
    {
        "part_id": "part-cw-stitch",
        "part_badge": "UI/UX & 구글 스티치",
        "part_title": "Part 2. [UI/UX 완전판] 구글 스티치 프롬프트 가이드 & 4대 주체 24대 마이크로 화면 와이어프레임",
        "file": os.path.join(BASE_DIR, "courseware", "Google_Stitch_UIUX_Design_Prompt_Guide.md"),
        "icon": "fa-palette",
        "color": "violet",
        "desc": "학생 9종 · 학부모 5종 · 교사 5종 · 학원장 5종 총 24개 화면 와이어프레임 & 고해상도 스티치 프롬프트 & 7대 교과 개념 도식"
    },
    {
        "part_id": "part-cw-tei",
        "part_badge": "7대 TEI 엔진 & 공학 규격",
        "part_title": "Part 3. [상용화 엔지니어링 규격] 글로벌 표준 7대 TEI 인터랙티브 문항 엔진 · 독서 툴바 · 웹앱 아키텍처 & QA",
        "file": os.path.join(BASE_DIR, "courseware", "PRD_문해력_코스웨어_상용화_마스터.md"),
        "icon": "fa-cube",
        "color": "blue",
        "desc": "Hot Text, EBSR, Cloze Builder, 도해조직자, CBT 실전 모의고사, Split-Screen 독서 도구 7종, 폴더 구조 & 출시 기준"
    }
]

def read_file(path):
    if not os.path.exists(path):
        print(f"Warning: File not found: {path}")
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

def slugify(text):
    clean = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', clean)

def process_section_html(html_str, part_idx):
    soup = BeautifulSoup(html_str, "html.parser")
    
    # 1. Convert language-mermaid blocks
    for code_block in soup.find_all("code", class_="language-mermaid"):
        pre = code_block.parent
        pre['class'] = ['mermaid', 'zoomable-target']
        pre.string = code_block.get_text()

    # 2. Add IDs to Headings and collect hierarchical TOC
    toc_tree = []
    current_chapter = None

    for heading in soup.find_all(["h1", "h2", "h3"]):
        h_text = heading.get_text().strip()
        if not h_text:
            continue
        
        # Generate anchor ID
        h_id = f"p{part_idx}-{heading.name}-{slugify(h_text)[:30]}"
        heading['id'] = h_id
        heading['class'] = heading.get('class', []) + ['scroll-mt-24']

        level = int(heading.name[1]) # 1, 2, 3
        item = {
            "id": h_id,
            "title": h_text,
            "level": level,
            "children": []
        }

        if level == 1:
            toc_tree.append(item)
            current_chapter = item
        elif level == 2:
            if current_chapter:
                current_chapter["children"].append(item)
            else:
                toc_tree.append(item)
        elif level == 3:
            if current_chapter and current_chapter["children"]:
                current_chapter["children"][-1]["children"].append(item)
            elif current_chapter:
                current_chapter["children"].append(item)
            else:
                toc_tree.append(item)

    # 3. Wrap pre blocks (ASCII art & wireframes) with zoom trigger
    for pre in soup.find_all("pre"):
        if 'mermaid' in pre.get('class', []):
            continue
        text = pre.get_text()
        # If it looks like ASCII wireframe (contains box drawing characters)
        if any(c in text for c in ['┌', '│', '└', '├', '─', '═', '║', '╔']):
            pre['class'] = pre.get('class', []) + ['ascii-wireframe', 'zoomable-target']

    return str(soup), toc_tree

def main():
    print("=" * 80)
    print("Building Ultimate Master Whitepaper & PRD HTML for ReadX (리드엑스)")
    print("=" * 80)

    sections_rendered = []
    all_parts_toc = []
    total_raw_bytes = 0

    for idx, sec in enumerate(MASTER_SECTIONS):
        file_path = sec["file"]
        raw_text = read_file(file_path)
        sz = len(raw_text.encode('utf-8'))
        total_raw_bytes += sz
        print(f"[{idx+1}/{len(MASTER_SECTIONS)}] Processing: {sec['part_badge']} ({sz/1024:.1f} KB) -> {os.path.basename(file_path)}")

        html_body = convert_md_to_html(raw_text)
        cleaned_html, toc_tree = process_section_html(html_body, idx+1)
        all_parts_toc.append({
            "part_info": sec,
            "tree": toc_tree
        })

        # Build Section Container
        sections_rendered.append(f"""
          <section id="{sec['part_id']}" class="scroll-mt-24 bg-white rounded-3xl shadow-sm border border-slate-200/90 p-6 lg:p-12 mb-12 relative overflow-hidden">
            <!-- Section Header Banner -->
            <div class="flex flex-wrap items-center justify-between gap-3 pb-6 mb-8 border-b border-slate-100">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-2xl bg-blue-50 text-blue-600 border border-blue-200 flex items-center justify-center text-xl font-bold shadow-sm">
                  <i class="fa-solid {sec['icon']}"></i>
                </div>
                <div>
                  <div class="flex items-center gap-2">
                    <span class="text-[11px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800 border border-blue-200">
                      {sec['part_badge']}
                    </span>
                    <span class="text-xs text-slate-400 hidden sm:inline">{sec['desc']}</span>
                  </div>
                  <h2 class="text-xl lg:text-2xl font-black text-slate-900 mt-1 tracking-tight">
                    {sec['part_title']}
                  </h2>
                </div>
              </div>
              <div class="text-xs text-slate-400 font-mono flex items-center gap-1.5 bg-slate-50 px-3 py-1.5 rounded-lg border border-slate-200">
                <i class="fa-solid fa-file-code text-blue-500"></i> {os.path.basename(file_path)}
              </div>
            </div>

            <!-- Section Content Body -->
            <div class="prose-custom max-w-none">
              {cleaned_html}
            </div>
          </section>
        """)

    print(f"\nTotal raw markdown processed: {total_raw_bytes / 1024:.1f} KB across {len(MASTER_SECTIONS)} master documents.")

    # Build Multi-level Hierarchical Sidebar TOC HTML
    sidebar_nav_items = []
    in_page_toc_items = []

    for p_idx, part_data in enumerate(all_parts_toc):
        sec = part_data["part_info"]
        tree = part_data["tree"]

        # Sidebar Part header
        sub_items_html = []
        in_page_sub_items = []

        for h1 in tree:
            h2_items_html = []
            in_page_h2_items = []
            for h2 in h1.get("children", []):
                h3_items_html = []
                for h3 in h2.get("children", []):
                    clean_h3 = h3["title"][:40] + ("..." if len(h3["title"]) > 40 else "")
                    h3_items_html.append(f"""
                      <a href="#{h3['id']}" class="toc-link block py-1 pl-6 pr-2 text-[11px] text-slate-500 hover:text-blue-600 truncate transition">
                        • {clean_h3}
                      </a>
                    """)
                h3_rendered = "\n".join(h3_items_html) if h3_items_html else ""
                
                clean_h2 = h2["title"][:38] + ("..." if len(h2["title"]) > 38 else "")
                h2_items_html.append(f"""
                  <div class="space-y-0.5">
                    <a href="#{h2['id']}" class="toc-link block py-1 pl-3 pr-2 text-xs font-medium text-slate-600 hover:text-blue-700 hover:bg-slate-50 rounded-lg truncate transition">
                      <span class="text-slate-400 mr-1">▸</span> {clean_h2}
                    </a>
                    {h3_rendered}
                  </div>
                """)
                in_page_h2_items.append(f"""
                  <li class="text-xs text-slate-600">
                    <a href="#{h2['id']}" class="hover:text-blue-600 hover:underline">{h2['title']}</a>
                  </li>
                """)

            h2_rendered = "\n".join(h2_items_html) if h2_items_html else ""
            clean_h1 = h1["title"][:35] + ("..." if len(h1["title"]) > 35 else "")

            sub_items_html.append(f"""
              <div class="toc-group mt-1">
                <a href="#{h1['id']}" class="toc-link flex items-center justify-between py-1.5 px-2 rounded-lg text-xs font-bold text-slate-800 hover:bg-blue-50 hover:text-blue-700 transition">
                  <span class="truncate">{clean_h1}</span>
                  <i class="fa-solid fa-chevron-right text-[9px] text-slate-400"></i>
                </a>
                <div class="pl-2 border-l border-slate-200 ml-2 space-y-0.5 mt-0.5">
                  {h2_rendered}
                </div>
              </div>
            """)

            in_page_sub_items.append(f"""
              <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-xs">
                <a href="#{h1['id']}" class="font-bold text-sm text-slate-900 hover:text-blue-600 flex items-center gap-1.5">
                  <i class="fa-solid fa-bookmark text-blue-500 text-xs"></i> {h1['title']}
                </a>
                <ul class="mt-2 space-y-1 pl-4 list-disc marker:text-blue-400">
                  {"".join(in_page_h2_items)}
                </ul>
              </div>
            """)

        all_sub_rendered = "\n".join(sub_items_html)

        sidebar_nav_items.append(f"""
          <div class="part-accordion mb-4 bg-slate-50/70 border border-slate-200 rounded-2xl p-2.5">
            <a href="#{sec['part_id']}" class="flex items-center gap-2.5 px-2 py-1.5 rounded-xl text-xs font-black text-slate-900 hover:text-blue-700 transition">
              <span class="w-6 h-6 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs shrink-0 shadow-xs">
                <i class="fa-solid {sec['icon']}"></i>
              </span>
              <div class="truncate">
                <div class="text-[10px] font-bold uppercase text-blue-600 tracking-wider">{sec['part_badge']}</div>
                <div class="truncate font-extrabold text-slate-800">{sec['part_title'].split('] ')[-1]}</div>
              </div>
            </a>
            <div class="mt-1 space-y-0.5">
              {all_sub_rendered}
            </div>
          </div>
        """)

        in_page_toc_items.append(f"""
          <div class="mb-6">
            <div class="flex items-center gap-2 mb-3">
              <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-100 text-blue-800 border border-blue-200">
                {sec['part_badge']}
              </span>
              <h3 class="text-base font-bold text-slate-800">{sec['part_title']}</h3>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
              {"".join(in_page_sub_items)}
            </div>
          </div>
        """)

    full_sidebar_nav_html = "\n".join(sidebar_nav_items)
    full_in_page_toc_html = "\n".join(in_page_toc_items)
    full_sections_html = "\n".join(sections_rendered)

    html_document = f"""<!DOCTYPE html>
<html lang="ko" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ReadX (리드엑스) - 2022 개정 전교과 설명문 수능형 문해력 코스웨어 종합 마스터 백서 & PRD</title>
  
  <!-- Fonts -->
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Mermaid.js for diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({{ 
      startOnLoad: true, 
      theme: 'neutral',
      themeVariables: {{
        primaryColor: '#e0e7ff',
        edgeColor: '#3b82f6',
        fontFamily: 'Pretendard, sans-serif',
        fontSize: '13px'
      }}
    }});
  </script>

  <style>
    body {{
      font-family: 'Pretendard', sans-serif;
      background-color: #f8fafc;
      color: #1e293b;
      line-height: 1.85;
      letter-spacing: -0.015em;
    }}
    .prose-custom h1 {{
      font-size: 2rem;
      font-weight: 800;
      color: #0f172a;
      margin-top: 2.5rem;
      margin-bottom: 1.25rem;
      padding-bottom: 0.6rem;
      border-bottom: 2px solid #2563eb;
      letter-spacing: -0.025em;
    }}
    .prose-custom h2 {{
      font-size: 1.55rem;
      font-weight: 700;
      color: #1e293b;
      margin-top: 2.25rem;
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid #cbd5e1;
    }}
    .prose-custom h3 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #334155;
      margin-top: 1.75rem;
      margin-bottom: 0.75rem;
    }}
    .prose-custom p {{
      margin-bottom: 1.15rem;
      font-size: 1.015rem;
    }}
    .prose-custom table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 1.25rem;
      margin-bottom: 2rem;
      font-size: 0.9rem;
      background-color: #ffffff;
      border-radius: 0.75rem;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      border: 1px solid #e2e8f0;
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
    
    /* Code and ASCII wireframe styling */
    .prose-custom pre:not(.mermaid) {{
      background-color: #0f172a;
      color: #f8fafc;
      padding: 1.25rem;
      border-radius: 0.85rem;
      overflow-x: auto;
      font-size: 0.84rem;
      line-height: 1.55;
      margin-top: 1.25rem;
      margin-bottom: 1.5rem;
      font-family: 'JetBrains Mono', monospace;
      border: 1px solid #334155;
      position: relative;
    }}
    .prose-custom pre.ascii-wireframe {{
      background-color: #090d16;
      border: 1.5px solid #2563eb;
      color: #e2e8f0;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
    }}
    .prose-custom code:not(pre code) {{
      background-color: #e2e8f0;
      color: #0f172a;
      padding: 0.2rem 0.45rem;
      border-radius: 0.25rem;
      font-size: 0.875em;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
    }}
    .mermaid {{
      background-color: #ffffff;
      padding: 1.5rem;
      border-radius: 0.85rem;
      border: 1px solid #e2e8f0;
      margin: 1.5rem 0;
      box-shadow: 0 2px 4px rgba(0,0,0,0.02);
      text-align: center;
      overflow-x: auto;
      position: relative;
    }}

    /* Zoom Trigger Button on pre and mermaid */
    .zoom-container-wrap {{
      position: relative;
    }}
    .zoom-btn-overlay {{
      position: absolute;
      top: 10px;
      right: 12px;
      z-index: 10;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(4px);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
      opacity: 0.85;
    }}
    .zoom-btn-overlay:hover {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
      opacity: 1;
      transform: translateY(-1px);
    }}

    /* Active ScrollSpy Link */
    .toc-link.active {{
      color: #1d4ed8 !important;
      font-weight: 800 !important;
      background-color: #eff6ff !important;
    }}

    @media print {{
      #sidebar, #top-bar, #interactive-simulator, #zoomModal {{ display: none !important; }}
      main {{ width: 100% !important; margin: 0 !important; padding: 0 !important; }}
      section {{ break-inside: avoid; border: none !important; box-shadow: none !important; }}
    }}
  </style>
</head>
<body class="bg-slate-50 min-h-screen flex flex-col antialiased">

  <!-- Top Global Sticky Bar -->
  <header id="top-bar" class="sticky top-0 z-50 bg-slate-900 border-b border-slate-800 text-white px-5 py-3 shadow-md flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-sky-500 flex items-center justify-center font-black text-white text-base shadow-sm ring-1 ring-white/20">
        <span>℞</span>
      </div>
      <div>
        <h1 class="text-base font-extrabold text-white tracking-tight flex items-center gap-2">
          <span>ReadX (리드엑스)</span>
          <span class="text-xs font-normal text-slate-300 hidden md:inline">│ 2022 개정 전교과 설명문 수능형 문해력 코스웨어</span>
          <span class="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-blue-500/25 text-blue-300 border border-blue-400/30">
            v6.0 Ultimate Edition
          </span>
        </h1>
        <p class="text-[11px] text-slate-400">
          설명문 100% 특화 · 2022 개정 9대 전 교과 직결 · 과정 독서(Process) · 4대 주체 24개 화면 · 월 $0 온디바이스 AI
        </p>
      </div>
    </div>

    <!-- Actions -->
    <div class="flex items-center gap-2.5">
      <div class="relative hidden lg:block">
        <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-slate-400 text-xs"></i>
        <input type="text" id="docSearch" placeholder="통합 문서 검색 (예: 알베도, 스캐폴딩, 24개 화면)..." 
               class="bg-slate-800 text-xs text-slate-200 pl-8 pr-3 py-1.5 rounded-lg border border-slate-700 focus:outline-none focus:border-blue-500 w-64 transition">
      </div>
      <button onclick="window.print()" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 px-3 py-1.5 rounded-lg border border-slate-700 flex items-center gap-1.5 transition">
        <i class="fa-solid fa-print"></i> 인쇄/PDF
      </button>
      <a href="#interactive-simulator" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-medium px-3.5 py-1.5 rounded-lg shadow-sm flex items-center gap-1.5 transition">
        <i class="fa-solid fa-wand-magic-sparkles"></i> 4단계 어노테이션 체험
      </a>
      <a href="#part-cw-stitch" class="text-xs bg-indigo-600 hover:bg-indigo-500 text-white font-medium px-3.5 py-1.5 rounded-lg shadow-sm flex items-center gap-1.5 transition">
        <i class="fa-solid fa-palette"></i> 24대 화면 스티치 가이드
      </a>
    </div>
  </header>

  <!-- Main View Container -->
  <div class="flex-1 max-w-[1800px] w-full mx-auto flex">
    
    <!-- Left Hierarchical Navigation Sidebar -->
    <aside id="sidebar" class="w-88 border-r border-slate-200 bg-white sticky top-[57px] h-[calc(100vh-57px)] overflow-y-auto p-4 shrink-0 hidden xl:block shadow-sm">
      <div class="mb-3 pb-3 border-b border-slate-100">
        <div class="flex items-center justify-between">
          <h2 class="text-xs font-bold uppercase tracking-wider text-slate-500">마스터 백서 계층형 상세 목차</h2>
          <span class="text-[10px] font-mono bg-blue-50 text-blue-700 px-2 py-0.5 rounded-full font-bold">ReadX Pro</span>
        </div>
        <div class="relative mt-2">
          <i class="fa-solid fa-filter absolute left-2.5 top-2 text-slate-400 text-[10px]"></i>
          <input type="text" id="tocFilter" placeholder="목차 빠른 필터링..." 
                 class="w-full bg-slate-50 text-xs text-slate-700 pl-7 pr-2.5 py-1.5 rounded-lg border border-slate-200 focus:outline-none focus:border-blue-500 transition">
        </div>
      </div>

      <!-- Rendered Multi-level Sidebar Tree -->
      <nav id="sidebar-nav-tree" class="space-y-2">
        {full_sidebar_nav_html}
      </nav>

      <!-- Sidebar Specs Summary -->
      <div class="mt-6 p-3.5 bg-slate-50 border border-slate-200 rounded-2xl text-xs text-slate-600 space-y-1.5">
        <div class="font-bold text-slate-800 text-[11px] uppercase tracking-wider mb-2 flex items-center gap-1.5">
          <i class="fa-solid fa-shield-heart text-blue-600"></i> ReadX 핵심 공학 지표
        </div>
        <div class="flex justify-between"><span>브랜드명:</span><span class="font-bold text-blue-600">ReadX (리드엑스)</span></div>
        <div class="flex justify-between"><span>핵심 장르:</span><span class="font-bold text-slate-900">설명문 100% 특화</span></div>
        <div class="flex justify-between"><span>교과 연계:</span><span class="font-bold text-slate-900">2022 개정 9대 전 교과</span></div>
        <div class="flex justify-between"><span>수능 연계:</span><span class="font-bold text-purple-600">비문학 5대 전 영역</span></div>
        <div class="flex justify-between"><span>독서 모형:</span><span class="font-bold text-emerald-600">과정 독서 (GRR)</span></div>
        <div class="flex justify-between"><span>어노테이션:</span><span class="font-bold text-amber-600">4단계 점진적 소거</span></div>
        <div class="flex justify-between"><span>정밀진단:</span><span class="font-bold text-indigo-600">6차원 X-Ray 투시</span></div>
        <div class="flex justify-between"><span>정밀처방:</span><span class="font-bold text-rose-600">3단계 클리닉 + 백신</span></div>
        <div class="flex justify-between"><span>AI 인프라:</span><span class="font-bold text-emerald-600">월 $0 (온디바이스 로컬)</span></div>
        <div class="flex justify-between"><span>영업이익률:</span><span class="font-bold text-blue-700">85% 이상 실현</span></div>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="flex-1 p-5 lg:p-10 max-w-5xl xl:max-w-6xl mx-auto overflow-hidden">
      
      <!-- Grand Hero Banner -->
      <div class="bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white rounded-3xl p-8 lg:p-12 mb-8 shadow-xl border border-slate-800 relative overflow-hidden">
        <div class="absolute -right-12 -bottom-12 opacity-10 text-[180px] text-white pointer-events-none">
          <i class="fa-solid fa-microscope"></i>
        </div>
        
        <div class="relative z-10">
          <div class="inline-flex items-center gap-2 bg-blue-500/20 text-blue-300 text-xs font-bold px-3.5 py-1.5 rounded-full border border-blue-500/30 mb-5">
            <span class="font-black text-amber-400">℞ ReadX Pro</span> 대한민국 최초 2022 개정 전 교과 개념 기반 설명문 100% 수능형 문해력 코스웨어
          </div>
          
          <h1 class="text-3xl lg:text-4xl xl:text-5xl font-black tracking-tight mb-4 text-white leading-tight">
            초등 전교과 설명문 수능형 문해력 코스웨어<br class="hidden sm:inline" />
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-blue-300 to-indigo-300">
              「ReadX (리드엑스)」
            </span> 상용화 마스터 백서 & PRD
          </h1>
          
          <p class="text-slate-300 text-sm lg:text-base max-w-4xl leading-relaxed mb-6 font-normal">
            문제를 푸는 결과(Product)가 아니라, <strong>글의 골격과 논리적 인과를 파악해 나가는 '읽는 과정(Reading Process)'을 배우는 코스웨어</strong>입니다.<br/>
            과장된 생성형 AI 만능론과 고비용 클라우드 호출을 배제하고, 
            <strong>결정론적 규칙 엔진과 형태소 분석 기반의 신뢰성 높은 인지 비계(Scaffolding)</strong>를 제공합니다.<br/>
            <strong>2022 개정 9대 전 교과(국·수·사·과·도·실·음·미·체) 핵심 개념을 설명문 100%로 집대성</strong>하여
            수능 국어 비문학 킬러 지문을 스스로 뚫어내는 진정한 자립 독자를 완성합니다.
          </p>

          <!-- 6-Metric Highlights Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 text-xs pt-6 border-t border-slate-800/80">
            <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800">
              <div class="text-slate-400 text-[11px]">핵심 타깃 장르</div>
              <div class="font-bold text-white text-sm mt-0.5">설명문 100%</div>
              <div class="text-[10px] text-blue-400">비문학 독서 특화</div>
            </div>
            <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800">
              <div class="text-slate-400 text-[11px]">2022 개정 교과</div>
              <div class="font-bold text-sky-300 text-sm mt-0.5">9대 전 교과</div>
              <div class="text-[10px] text-slate-400">국수사과도실음미체</div>
            </div>
            <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800">
              <div class="text-slate-400 text-[11px]">수능 연계 출제</div>
              <div class="font-bold text-purple-300 text-sm mt-0.5">5대 독서 영역</div>
              <div class="text-[10px] text-slate-400">인문·사회·과학·기술·예술</div>
            </div>
            <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800">
              <div class="text-slate-400 text-[11px]">핵심 교육공학</div>
              <div class="font-bold text-emerald-300 text-sm mt-0.5">과정 중심 GRR</div>
              <div class="text-[10px] text-slate-400">시범 ➔ 힌트 ➔ 완전자립</div>
            </div>
            <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800">
              <div class="text-slate-400 text-[11px]">정밀 진단 & 처방</div>
              <div class="font-bold text-pink-300 text-sm mt-0.5">6차원 X-Ray</div>
              <div class="text-[10px] text-slate-400">D1~D6 수능 오답 백신</div>
            </div>
            <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800">
              <div class="text-slate-400 text-[11px]">서버 AI 토큰 비용</div>
              <div class="font-bold text-yellow-300 text-sm mt-0.5">월 $0.00</div>
              <div class="text-[10px] text-emerald-400">온디바이스 로컬 AI</div>
            </div>
          </div>
        </div>
      </div>

      <!-- In-Page Hierarchical TOC Box (Expandable) -->
      <div class="bg-white rounded-3xl shadow-sm border border-slate-200 p-6 lg:p-8 mb-8">
        <div class="flex items-center justify-between mb-4 pb-3 border-b border-slate-100">
          <div class="flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-sm">
              <i class="fa-solid fa-list-check"></i>
            </div>
            <div>
              <h2 class="text-lg font-black text-slate-900">ReadX 마스터 백서 전체 통합 목차 (Full Directory)</h2>
              <p class="text-xs text-slate-500">목차 항목을 클릭하면 해당 절 및 화면 상세 규격으로 즉시 부드럽게 스크롤됩니다.</p>
            </div>
          </div>
          <button onclick="toggleInPageToc()" id="btn-toggle-inpage-toc" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1.5">
            <i class="fa-solid fa-chevron-up" id="icon-toggle-toc"></i> 목차 접기/펼치기
          </button>
        </div>

        <div id="inpage-toc-body" class="space-y-6">
          {full_in_page_toc_html}
        </div>
      </div>

      <!-- Live Interactive Scaffolding Simulator Box -->
      <div id="interactive-simulator" class="bg-white rounded-3xl shadow-md border-2 border-blue-500/30 p-6 lg:p-8 mb-12">
        <div class="flex flex-wrap items-center justify-between gap-4 pb-4 mb-6 border-b border-slate-200">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-lg">
              <i class="fa-solid fa-wand-magic-sparkles"></i>
            </div>
            <div>
              <span class="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200">
                LIVE INTERACTIVE DEMO
              </span>
              <h3 class="text-lg font-bold text-slate-900 mt-0.5">
                점진적 어노테이션 노출(Progressive Annotation) 4단계 라이브 체험
              </h3>
            </div>
          </div>
          <div class="text-xs text-slate-500">
            버튼을 클릭하여 본문이 <strong>[클린 모드]</strong>에서 <strong>[3단계 전문가 첨삭 노트]</strong>로 진화하는 과정을 체험하세요.
          </div>
        </div>

        <!-- Mode Buttons -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-6">
          <button onclick="setScaffoldLevel(0)" id="btn-scaffold-0" class="py-2.5 px-3 rounded-xl text-xs font-bold border transition flex items-center justify-center gap-2 bg-slate-900 text-white border-slate-900 shadow-sm">
            <i class="fa-solid fa-file"></i> 0. 클린 리딩 모드
          </button>
          <button onclick="setScaffoldLevel(1)" id="btn-scaffold-1" class="py-2.5 px-3 rounded-xl text-xs font-bold border transition flex items-center justify-center gap-2 bg-white text-slate-700 border-slate-300 hover:bg-slate-50">
            <i class="fa-solid fa-comment-dots text-amber-500"></i> 1. 멈춤 자가 질문
          </button>
          <button onclick="setScaffoldLevel(2)" id="btn-scaffold-2" class="py-2.5 px-3 rounded-xl text-xs font-bold border transition flex items-center justify-center gap-2 bg-white text-slate-700 border-slate-300 hover:bg-slate-50">
            <i class="fa-solid fa-brain text-blue-500"></i> 2. 사고구술 빈칸
          </button>
          <button onclick="setScaffoldLevel(3)" id="btn-scaffold-3" class="py-2.5 px-3 rounded-xl text-xs font-bold border transition flex items-center justify-center gap-2 bg-white text-slate-700 border-slate-300 hover:bg-slate-50">
            <i class="fa-solid fa-highlighter text-emerald-500"></i> 3. 2층 첨삭 노트 개방
          </button>
        </div>

        <!-- Interactive Split Screen Preview -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 bg-[#FCFBF7] p-6 rounded-2xl border border-slate-200">
          
          <!-- Left: Passage Reader (7 Cols) -->
          <div class="lg:col-span-7 bg-white p-6 rounded-xl border border-slate-200 shadow-sm relative">
            <div class="flex items-center justify-between text-xs text-slate-400 mb-4 pb-2 border-b border-slate-100">
              <span class="font-bold text-slate-700 flex items-center gap-1.5">
                <i class="fa-solid fa-book-open text-blue-600"></i> 초등 6학년 과학 [지구 열수지 균형과 알베도]
              </span>
              <span id="scaffold-badge" class="px-2 py-0.5 rounded bg-slate-100 text-slate-600 font-bold">
                클린 모드 (비계 없음)
              </span>
            </div>

            <div class="space-y-4 text-slate-800 text-sm leading-relaxed" style="line-height: 2.0;">
              <p id="para-1">
                <span class="inline-block px-1.5 py-0.5 rounded bg-slate-100 text-slate-500 text-xs font-mono font-bold mr-1">[1문단]</span>
                지구 표면의 얼음과 눈은 햇빛을 거울처럼 반사하는 능력이 뛰어납니다. 이를 <span id="term-albedo" class="font-medium">'알베도(반사율)'</span>라고 부릅니다. 눈으로 덮인 북극 빙하의 알베도는 약 80~90%에 달하여 태양 복사 에너지를 대부분 우주로 다시 튕겨냅니다.
              </p>

              <!-- Level 1 Wing Note (Hidden initially) -->
              <div id="wing-note-1" class="hidden p-3 rounded-lg bg-amber-50 border-l-4 border-amber-500 text-xs text-amber-900 my-2">
                <div class="font-bold flex items-center gap-1 mb-1">
                  <i class="fa-solid fa-lightbulb text-amber-500"></i> 💭 문단 멈춤 생각 질문
                </div>
                빙하는 태양열을 어떻게 하나요? 그리고 바다는 얼음과 비교할 때 열을 어떻게 다룰지 다음 문단에서 찾아보세요!
              </div>

              <p id="para-2">
                <span class="inline-block px-1.5 py-0.5 rounded bg-slate-100 text-slate-500 text-xs font-mono font-bold mr-1">[2문단]</span>
                <span id="discourse-marker" class="font-medium">반면에</span> <span id="evidence-sentence">짙은 색의 바다는 태양 복사열의 90% 이상을 그대로 흡수합니다.</span> 그런데 지구온난화로 빙하가 녹아 바다가 드러나면, 지표면의 알베도가 급격히 낮아져 지구가 흡수하는 열이 폭발적으로 늘어납니다. 그 결과 기온이 더욱 상승하여 남은 빙하마저 더 빠르게 녹이는 연쇄적인 양(+)의 피드백 루프가 형성됩니다.
              </p>

              <!-- Level 3 Annotation Card (Hidden initially) -->
              <div id="expert-card-3" class="hidden p-3.5 rounded-lg bg-emerald-50 border border-emerald-200 text-xs text-emerald-950 mt-4 space-y-1.5">
                <div class="font-bold flex items-center gap-1.5 text-emerald-800">
                  <i class="fa-solid fa-graduation-cap text-emerald-600"></i> ✅ 전문가 2층 첨삭 노트 해설
                </div>
                <div>• <strong>담화 구조</strong>: 얼음(반사 90%) vs 바다(흡수 90%)의 <strong>[비교·대조]</strong> + 빙하 감소➔열 흡수➔온도 상승 <strong>[다단계 연쇄 인과]</strong></div>
                <div>• <strong>수능 출제 포인트</strong>: "알베도가 감소할수록 흡수 열량이 증가한다"는 반비례 관계를 수능 물리·지구과학 킬러 선지로 직결!</div>
              </div>
            </div>
          </div>

          <!-- Right: Interactive Workspace (5 Cols) -->
          <div class="lg:col-span-5 bg-white p-6 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-xs text-slate-400 mb-3 pb-2 border-b border-slate-100">
                <span class="font-bold text-slate-700">🧩 인지 워크스페이스 & 선지</span>
                <span id="step-indicator" class="font-bold text-blue-600">Step 1. 단서 포착</span>
              </div>

              <!-- Question Box -->
              <div class="mb-4">
                <div class="text-xs font-bold text-slate-500 mb-1">Q. KICE 수능형 인과 추론 문항</div>
                <div class="text-xs font-bold text-slate-800 leading-snug">
                  위 글을 바탕으로 북극 빙하가 녹았을 때 나타나는 변화로 가장 적절한 것은?
                </div>
              </div>

              <!-- Options -->
              <div class="space-y-2 text-xs">
                <div id="opt-1" class="p-2.5 rounded-lg border border-slate-200 bg-slate-50 text-slate-700 cursor-pointer hover:border-slate-300 transition">
                  ① 바다의 알베도가 높아져 태양 복사열 반사량이 증가한다.
                  <div id="trap-d1" class="hidden text-[11px] font-bold text-rose-600 mt-1">
                    🚨 [D1 인과 역전 함정]: 알베도는 높아지는 것이 아니라 낮아집니다!
                  </div>
                </div>
                <div id="opt-2" class="p-2.5 rounded-lg border border-slate-200 bg-slate-50 text-slate-700 cursor-pointer hover:border-slate-300 transition">
                  ② 지표면의 열 흡수가 증가하여 기온 상승이 더욱 가속화된다. (정답)
                </div>
                <div id="opt-3" class="p-2.5 rounded-lg border border-slate-200 bg-slate-50 text-slate-700 cursor-pointer hover:border-slate-300 transition">
                  ③ 태양 복사열 흡수량이 늘어나도 남은 빙하의 융해 속도는 변함없다.
                </div>
              </div>

              <!-- Cloze Builder (Level 2+) -->
              <div id="cloze-box" class="hidden mt-4 p-3 bg-blue-50 border border-blue-200 rounded-xl text-xs text-blue-900">
                <div class="font-bold mb-1.5 flex items-center gap-1">
                  <i class="fa-solid fa-brain text-blue-600"></i> 사고구술 인과 고리 조립
                </div>
                <div class="p-2 bg-white rounded border border-blue-100 font-mono text-[11px]">
                  [빙하 감소] ➔ [알베도 <span class="bg-blue-100 text-blue-800 font-bold px-1 rounded">감소</span>] ➔ [열 흡수 <span class="bg-blue-100 text-blue-800 font-bold px-1 rounded">증가</span>]
                </div>
              </div>
            </div>

            <!-- Bottom Status Indicator -->
            <div id="scaffold-status-desc" class="mt-4 pt-3 border-t border-slate-100 text-xs text-slate-500">
              현재 <strong>클린 리딩 모드</strong>입니다. 학생은 스스로 지문을 읽고 순수한 인지력으로 답을 도출합니다.
            </div>
          </div>

        </div>
      </div>

      <!-- Rendered Master Sections -->
      {full_sections_html}

    </main>
  </div>

  <!-- Interactive Diagram & Schematic Lightbox Zoom Modal -->
  <div id="zoomModal" class="fixed inset-0 z-[100] bg-slate-950/85 backdrop-blur-md hidden flex flex-col justify-between p-4 lg:p-8 transition-opacity duration-300">
    <!-- Modal Header Controls -->
    <div class="flex items-center justify-between pb-3 border-b border-slate-800 text-white shrink-0">
      <div class="flex items-center gap-3">
        <span class="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center text-sm font-bold">
          <i class="fa-solid fa-magnifying-glass-plus"></i>
        </span>
        <div>
          <h4 id="zoomModalTitle" class="text-sm lg:text-base font-extrabold text-white">도식 및 화면 와이어프레임 상세 확대 뷰</h4>
          <span class="text-[11px] text-slate-400">마우스 휠로 확대/축소하거나 마우스 드래그로 화면을 이동할 수 있습니다. (단축키: Esc로 닫기)</span>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <span id="zoomLevelDisplay" class="text-xs font-mono font-bold bg-slate-800 px-2.5 py-1 rounded text-sky-300 border border-slate-700">100%</span>
        <button onclick="changeZoom(0.15)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-white border border-slate-700 transition">
          <i class="fa-solid fa-plus"></i> 확대
        </button>
        <button onclick="changeZoom(-0.15)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-white border border-slate-700 transition">
          <i class="fa-solid fa-minus"></i> 축소
        </button>
        <button onclick="resetZoom()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-white border border-slate-700 transition">
          <i class="fa-solid fa-arrows-rotate"></i> 초기화
        </button>
        <button onclick="closeZoomModal()" class="px-3.5 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-xs text-white font-bold transition ml-2">
          <i class="fa-solid fa-xmark"></i> 닫기 (Esc)
        </button>
      </div>
    </div>

    <!-- Modal Content Canvas Container (Scrollable / Draggable) -->
    <div id="zoomModalViewport" class="flex-1 overflow-auto p-4 flex items-center justify-center cursor-grab active:cursor-grabbing select-none">
      <div id="zoomModalCanvas" class="transition-transform duration-150 origin-center bg-slate-900 p-6 rounded-2xl border border-slate-700 shadow-2xl max-w-full">
        <!-- Injected content goes here -->
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="bg-slate-950 border-t border-slate-800 text-slate-400 py-12 px-6 text-center text-xs">
    <div class="max-w-4xl mx-auto space-y-3">
      <div class="font-bold text-white text-base">
        초등 2022 개정 전교과 설명문 수능형 문해력 코스웨어 「ReadX (리드엑스)」
      </div>
      <p class="text-slate-400 max-w-2xl mx-auto leading-relaxed">
        본 마스터 백서는 2022 개정 교육과정 및 한국교육과정평가원(KICE) 수능 국어 영역 출제 원리에 입각하여 교육공학적으로 설계된 
        대한민국 초등 국어·전교과 문해력 교육의 표준 공학 자산입니다.
      </p>
      <div class="flex items-center justify-center gap-4 text-slate-500 pt-2 text-[11px]">
        <span>ReadX (리드엑스)</span>
        <span>•</span>
        <span>설명문 100% 특화</span>
        <span>•</span>
        <span>9대 전 교과 96개 마스터 위계</span>
        <span>•</span>
        <span>월 API 비용 $0 온디바이스 로컬 AI</span>
        <span>•</span>
        <span>GRR 과정 중심 독서</span>
      </div>
      <div class="text-slate-600 pt-2">
        © 2026 ReadX Literacy Courseware Engineering Lab. 100% Pure Expository Courseware Master Architecture.
      </div>
    </div>
  </footer>

  <!-- Interactive Scripts -->
  <script>
    // In-Page TOC Toggle
    function toggleInPageToc() {{
      const body = document.getElementById('inpage-toc-body');
      const icon = document.getElementById('icon-toggle-toc');
      if (body.classList.contains('hidden')) {{
        body.classList.remove('hidden');
        icon.className = 'fa-solid fa-chevron-up';
      }} else {{
        body.classList.add('hidden');
        icon.className = 'fa-solid fa-chevron-down';
      }}
    }}

    // Live Search in document
    const searchInput = document.getElementById('docSearch');
    if (searchInput) {{
      searchInput.addEventListener('input', function(e) {{
        const term = e.target.value.toLowerCase().trim();
        if (!term || term.length < 2) return;
        const matches = document.querySelectorAll('main h1, main h2, main h3, main th, main strong');
        for (const el of matches) {{
          if (el.textContent.toLowerCase().includes(term)) {{
            el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            el.classList.add('bg-yellow-200', 'text-slate-900', 'rounded', 'px-1', 'transition');
            setTimeout(() => {{
              el.classList.remove('bg-yellow-200', 'text-slate-900', 'rounded', 'px-1');
            }}, 2500);
            break;
          }}
        }}
      }});
    }}

    // Sidebar TOC Real-time Filter
    const tocFilterInput = document.getElementById('tocFilter');
    if (tocFilterInput) {{
      tocFilterInput.addEventListener('input', function(e) {{
        const term = e.target.value.toLowerCase().trim();
        const links = document.querySelectorAll('#sidebar-nav-tree .toc-link');
        links.forEach(link => {{
          const text = link.textContent.toLowerCase();
          const parent = link.closest('.toc-group, .part-accordion');
          if (!term || text.includes(term)) {{
            link.style.display = '';
            if (parent) parent.style.display = '';
          }} else {{
            link.style.display = 'none';
          }}
        }});
      }});
    }}

    // Scaffolding Simulator State Machine
    function setScaffoldLevel(level) {{
      for (let i = 0; i <= 3; i++) {{
        const btn = document.getElementById('btn-scaffold-' + i);
        if (i === level) {{
          btn.className = "py-2.5 px-3 rounded-xl text-xs font-bold border transition flex items-center justify-center gap-2 bg-slate-900 text-white border-slate-900 shadow-sm";
        }} else {{
          btn.className = "py-2.5 px-3 rounded-xl text-xs font-bold border transition flex items-center justify-center gap-2 bg-white text-slate-700 border-slate-300 hover:bg-slate-50";
        }}
      }}

      const badge = document.getElementById('scaffold-badge');
      const wingNote = document.getElementById('wing-note-1');
      const expertCard = document.getElementById('expert-card-3');
      const clozeBox = document.getElementById('cloze-box');
      const evidence = document.getElementById('evidence-sentence');
      const discourse = document.getElementById('discourse-marker');
      const termAlbedo = document.getElementById('term-albedo');
      const opt1 = document.getElementById('opt-1');
      const opt2 = document.getElementById('opt-2');
      const trapD1 = document.getElementById('trap-d1');
      const statusDesc = document.getElementById('scaffold-status-desc');
      const stepIndicator = document.getElementById('step-indicator');

      evidence.className = "font-medium";
      discourse.className = "font-medium";
      termAlbedo.className = "font-medium";
      wingNote.classList.add('hidden');
      expertCard.classList.add('hidden');
      clozeBox.classList.add('hidden');
      trapD1.classList.add('hidden');
      opt1.classList.remove('line-through', 'opacity-50', 'bg-rose-50', 'border-rose-300');
      opt2.classList.remove('bg-emerald-50', 'border-emerald-300', 'font-bold');

      if (level === 0) {{
        badge.textContent = "0. 클린 리딩 모드 (비계 없음)";
        badge.className = "px-2 py-0.5 rounded bg-slate-100 text-slate-600 font-bold";
        stepIndicator.textContent = "Step 1. 단서 포착";
        statusDesc.innerHTML = "현재 <strong>클린 리딩 모드</strong>입니다. 첨삭 힌트 없이 순수한 자기 힘으로 글을 읽습니다.";
      }} else if (level === 1) {{
        badge.textContent = "1단계: 멈춤 자가 질문 발동";
        badge.className = "px-2 py-0.5 rounded bg-amber-100 text-amber-800 font-bold";
        wingNote.classList.remove('hidden');
        stepIndicator.textContent = "메타인지 질문 모니터링";
        statusDesc.innerHTML = "학생이 망설이거나 질문을 요청하여 <strong>문단별 멈춤 자가 질문</strong>이 날개에 노출되었습니다.";
      }} else if (level === 2) {{
        badge.textContent = "2단계: 사고구술 빈칸 + 단서 스포트라이트";
        badge.className = "px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold";
        wingNote.classList.remove('hidden');
        clozeBox.classList.remove('hidden');
        evidence.className = "bg-amber-200 text-slate-900 px-1 py-0.5 rounded font-bold ring-2 ring-amber-400";
        trapD1.classList.remove('hidden');
        opt1.classList.add('bg-rose-50', 'border-rose-300');
        stepIndicator.textContent = "Step 2. 인과 고리 조립";
        statusDesc.innerHTML = "1차 오답 발생! 본문 근거 문장이 <strong>노란색 펄스 스포트라이트</strong>되고, 우측에 <strong>D1 함정 경보</strong>와 <strong>사고구술 빈칸</strong>이 열렸습니다.";
      }} else if (level === 3) {{
        badge.textContent = "3단계: 2층 첨삭 노트 완전 개방";
        badge.className = "px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-bold";
        wingNote.classList.remove('hidden');
        clozeBox.classList.remove('hidden');
        expertCard.classList.remove('hidden');
        evidence.className = "bg-amber-200 text-slate-900 px-1 py-0.5 rounded font-bold";
        discourse.className = "bg-purple-100 text-purple-800 px-1 py-0.5 rounded font-bold border border-purple-300";
        termAlbedo.className = "border-b-2 border-dashed border-blue-500 text-blue-700 font-bold";
        opt1.classList.add('line-through', 'opacity-50');
        opt2.classList.add('bg-emerald-50', 'border-emerald-300', 'font-bold');
        stepIndicator.textContent = "Step 3. 정답 공식 확정";
        statusDesc.innerHTML = "2차 오답 후 <strong>2층 첨삭 노트가 완전 개방</strong>되었습니다. 오답 선지에 취소선이 그어지고 정답의 인과 도출 공식이 명쾌하게 확인됩니다.";
      }}
    }}

    // Lightbox Zoom Modal Implementation
    let currentScale = 1.0;
    const modal = document.getElementById('zoomModal');
    const modalCanvas = document.getElementById('zoomModalCanvas');
    const zoomLevelDisplay = document.getElementById('zoomLevelDisplay');

    function openZoomModal(targetElement, titleText) {{
      const clone = targetElement.cloneNode(true);
      // Remove any embedded zoom button from clone
      const overlayBtn = clone.querySelector('.zoom-btn-overlay');
      if (overlayBtn) overlayBtn.remove();
      
      modalCanvas.innerHTML = '';
      modalCanvas.appendChild(clone);
      
      document.getElementById('zoomModalTitle').textContent = titleText || "도식 및 화면 와이어프레임 상세 확대 뷰";
      currentScale = 1.0;
      updateZoomTransform();
      
      modal.classList.remove('hidden');
      document.body.style.overflow = 'hidden';
    }}

    function closeZoomModal() {{
      modal.classList.add('hidden');
      document.body.style.overflow = '';
      modalCanvas.innerHTML = '';
    }}

    function changeZoom(delta) {{
      currentScale = Math.min(Math.max(currentScale + delta, 0.5), 3.0);
      updateZoomTransform();
    }}

    function resetZoom() {{
      currentScale = 1.0;
      updateZoomTransform();
    }}

    function updateZoomTransform() {{
      modalCanvas.style.transform = `scale(${{currentScale}})`;
      zoomLevelDisplay.textContent = Math.round(currentScale * 100) + '%';
    }}

    // Keyboard ESC to close
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape' && !modal.classList.contains('hidden')) {{
        closeZoomModal();
      }}
    }});

    // Auto-inject zoom buttons to all wireframes and diagrams
    document.addEventListener('DOMContentLoaded', () => {{
      const targets = document.querySelectorAll('.ascii-wireframe, .mermaid');
      targets.forEach((el, index) => {{
        // Wrap container if needed
        const wrapper = document.createElement('div');
        wrapper.className = 'zoom-container-wrap';
        el.parentNode.insertBefore(wrapper, el);
        wrapper.appendChild(el);

        const btn = document.createElement('button');
        btn.className = 'zoom-btn-overlay';
        btn.innerHTML = '<i class="fa-solid fa-expand"></i> 크게 확대';
        
        // Find nearest heading for title
        let prev = wrapper.previousElementSibling;
        let title = "도식 및 와이어프레임 상세 뷰";
        while (prev) {{
          if (['H1', 'H2', 'H3', 'H4'].includes(prev.tagName)) {{
            title = prev.textContent.trim();
            break;
          }}
          prev = prev.previousElementSibling;
        }}

        btn.onclick = (e) => {{
          e.stopPropagation();
          openZoomModal(el, title);
        }};
        wrapper.appendChild(btn);

        // Double click to zoom
        el.addEventListener('dblclick', () => {{
          openZoomModal(el, title);
        }});
      }});
    }});
  </script>
</body>
</html>
"""

    out_paths = [
        os.path.join(BASE_DIR, "courseware_master_whitepaper_prd.html"),
        os.path.join(BASE_DIR, "courseware", "courseware_master_whitepaper_prd.html")
    ]

    for p in out_paths:
        print(f"Writing grand mega master HTML to: {p}")
        with open(p, "w", encoding="utf-8") as f:
            f.write(html_document)

    # Copy to artifact directory
    if os.path.exists(ARTIFACT_DIR):
        artifact_out = os.path.join(ARTIFACT_DIR, "courseware_master_whitepaper_prd.html")
        print(f"Copying to artifact directory: {artifact_out}")
        shutil.copyfile(out_paths[0], artifact_out)

    final_size_kb = os.path.getsize(out_paths[0]) / 1024
    print("=" * 80)
    print(f"Successfully generated Ultimate Grand Master Whitepaper HTML for ReadX!")
    print(f"Final Compiled HTML Size: {final_size_kb:.1f} KB")
    print("=" * 80)

if __name__ == "__main__":
    main()
