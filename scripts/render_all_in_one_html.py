# -*- coding: utf-8 -*-
"""
초등 1~6학년 설명문 수능형 문해력 코스웨어 올인원(All-in-One) HTML 렌더러
- courseware/data/unified_courseware_master_data.json + expository_courseware_hierarchy.json 로드
- [탭 1] AI 정밀 X-Ray 진단(어디가·왜·어떻게 부족한지 6차원 전수 진단) ➔ 1:1 맞춤형 처방 클리닉 ➔ 실전 수능 대비 문제
- [탭 2] 1~6학년 프로토타입 전 학년 지문·시각자료·Step 1·2·3 비교 뷰
- [탭 3] 학년별 지문 정량·어휘 복잡도(Track 2) & KICE 수능 스케일링·6대 오답 공식(Track 3) 설계 표준
- [탭 4] 설명문 96개 + 공통기초 36개 마스터 위계 탐색기
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

with open(os.path.join(DATA_DIR, "unified_courseware_master_data.json"), "r", encoding="utf-8") as f:
    MASTER_BUNDLE = json.load(f)

with open(os.path.join(DATA_DIR, "expository_courseware_hierarchy.json"), "r", encoding="utf-8") as f:
    HIERARCHY_DATA = json.load(f)

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI 초등 설명문(Expository) 수능형 문해력 코스웨어 — 정밀 X-Ray 진단 · 맞춤형 처방 · 실전 수능 통합본</title>
  <style>
    :root {
      --navy: #0F172A;
      --blue: #1D4ED8;
      --blue-soft: #EFF6FF;
      --green: #16A34A;
      --green-soft: #DCFCE7;
      --red: #DC2626;
      --red-soft: #FEE2E2;
      --amber: #D97706;
      --amber-soft: #FEF3C7;
      --purple: #6D28D9;
      --purple-soft: #F5F3FF;
      --bg: #F1F5F9;
      --card: #FFFFFF;
      --border: #CBD5E1;
      --text: #0F172A;
      --muted: #475569;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Pretendard', 'Malgun Gothic', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }

    /* Top Global Header */
    .top-bar {
      background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
      color: #fff;
      padding: 15px 26px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.24);
    }
    .brand-title {
      font-size: 1.24rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 9px;
    }
    .brand-pill {
      background: #38BDF8;
      color: #0F172A;
      font-size: 0.73rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 99px;
    }
    .brand-sub { font-size: 0.8rem; color: #93C5FD; margin-top: 2px; }
    .main-nav { display: flex; gap: 7px; flex-wrap: wrap; }
    .main-tab-btn {
      background: rgba(255,255,255,0.11);
      color: #E2E8F0;
      border: 1px solid rgba(255,255,255,0.22);
      padding: 8px 13px;
      border-radius: 8px;
      font-size: 0.83rem;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.16s;
    }
    .main-tab-btn:hover { background: rgba(255,255,255,0.22); }
    .main-tab-btn.active {
      background: #FACC15;
      color: #0F172A;
      border-color: #FACC15;
      box-shadow: 0 2px 10px rgba(250, 204, 21, 0.35);
    }

    /* Grade / Persona Strip */
    .grade-selector-strip {
      background: #1E293B;
      padding: 10px 26px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      border-bottom: 1px solid #334155;
    }
    .grade-btn-group { display: flex; gap: 7px; flex-wrap: wrap; }
    .grade-pill-btn {
      background: rgba(255,255,255,0.08);
      color: #CBD5E1;
      border: 1px solid rgba(255,255,255,0.18);
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 0.81rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.16s;
    }
    .grade-pill-btn:hover { background: rgba(255,255,255,0.18); color: #fff; }
    .grade-pill-btn.active {
      background: #38BDF8;
      color: #0F172A;
      border-color: #38BDF8;
      font-weight: 800;
    }

    /* 3-Stage Stepper */
    .loop-stepper {
      background: #FFFFFF;
      border-bottom: 2px solid var(--border);
      padding: 11px 26px;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 2px 8px rgba(15,23,42,0.06);
    }
    .stage-step {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 16px;
      border-radius: 11px;
      border: 2px solid #E2E8F0;
      background: #F8FAFC;
      cursor: pointer;
      transition: all 0.18s;
      min-width: 250px;
    }
    .stage-step:hover { border-color: #93C5FD; }
    .stage-step.active {
      border-color: var(--blue);
      background: var(--blue-soft);
      box-shadow: 0 4px 12px rgba(29, 78, 216, 0.12);
    }
    .stage-step.done { border-color: var(--green); background: var(--green-soft); }
    .stage-num {
      width: 30px; height: 30px; border-radius: 50%;
      background: #CBD5E1; color: #1E293B;
      font-weight: 800; font-size: 0.9rem;
      display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .stage-step.active .stage-num { background: var(--blue); color: #fff; }
    .stage-step.done .stage-num { background: var(--green); color: #fff; }
    .stage-info-title { font-size: 0.9rem; font-weight: 800; color: #0F172A; }
    .stage-info-sub { font-size: 0.74rem; color: var(--muted); }
    .stage-arrow { font-size: 1.2rem; color: #94A3B8; font-weight: 800; }

    .main-view { display: none; }
    .main-view.active { display: block; }
    .main-wrap { max-width: 1560px; margin: 0 auto; padding: 18px 26px 60px; }

    /* X-Ray Top Summary Banner */
    .xray-hero {
      background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
      color: #fff;
      border-radius: 14px;
      padding: 18px 22px;
      margin-bottom: 18px;
      border: 1px solid #334155;
      box-shadow: 0 6px 18px rgba(15,23,42,0.14);
    }
    .xray-hero-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255,255,255,0.15);
    }
    .xray-where-how {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-top: 12px;
    }
    @media (max-width: 980px) {
      .xray-where-how { grid-template-columns: 1fr; }
    }
    .wh-box {
      background: rgba(255,255,255,0.07);
      border-left: 4px solid #F87171;
      padding: 11px 14px;
      border-radius: 8px;
      font-size: 0.85rem;
    }
    .wh-box.how { border-left-color: #38BDF8; }
    .wh-title {
      font-weight: 800;
      font-size: 0.82rem;
      color: #FCA5A5;
      margin-bottom: 4px;
      display: block;
    }
    .wh-box.how .wh-title { color: #7DD3FC; }

    /* Cards & Grids */
    .grid-2 {
      display: grid;
      grid-template-columns: 1.02fr 1fr;
      gap: 18px;
      align-items: start;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      align-items: start;
    }
    @media (max-width: 1180px) {
      .grid-2, .grid-3 { grid-template-columns: 1fr; }
    }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 13px;
      padding: 18px;
      box-shadow: 0 2px 6px rgba(15,23,42,0.04);
      margin-bottom: 16px;
    }
    .card-title {
      font-size: 1rem;
      font-weight: 800;
      color: var(--navy);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      border-bottom: 2px solid #F1F5F9;
      padding-bottom: 8px;
    }
    .badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 800;
    }
    .badge-blue { background: #DBEAFE; color: #1E40AF; }
    .badge-red { background: #FEE2E2; color: #991B1B; }
    .badge-green { background: #DCFCE7; color: #166534; }
    .badge-amber { background: #FEF3C7; color: #92400E; }
    .badge-purple { background: #EDE9FE; color: #5B21B6; }

    /* 16 Sub-skill X-Ray Heatmap Grid */
    .subskill-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-bottom: 12px;
    }
    @media (max-width: 780px) {
      .subskill-grid { grid-template-columns: repeat(2, 1fr); }
    }
    .sk-cell {
      padding: 9px 10px;
      border-radius: 9px;
      border: 1px solid #CBD5E1;
      cursor: pointer;
      transition: all 0.15s;
      font-size: 0.78rem;
    }
    .sk-cell:hover { transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0,0,0,0.08); }
    .sk-cell.critical {
      background: #FEF2F2;
      border: 2px solid #DC2626;
      color: #7F1D1D;
    }
    .sk-cell.fragile {
      background: #FFFBEB;
      border: 1.5px solid #F59E0B;
      color: #78350F;
    }
    .sk-cell.mastered {
      background: #F0FDF4;
      border: 1px solid #86EFAC;
      color: #14532D;
    }
    .sk-code { font-weight: 900; font-size: 0.82rem; display: flex; justify-content: space-between; }
    .sk-name { font-weight: 700; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .sk-detail-box {
      background: #F8FAFC;
      border: 1px solid #94A3B8;
      border-left: 5px solid #DC2626;
      border-radius: 8px;
      padding: 10px 13px;
      font-size: 0.84rem;
    }

    /* Progress Bars */
    .score-row { margin-bottom: 10px; }
    .score-head {
      display: flex;
      justify-content: space-between;
      font-size: 0.83rem;
      font-weight: 700;
      margin-bottom: 3px;
    }
    .bar-bg { height: 9px; background: #E2E8F0; border-radius: 99px; overflow: hidden; }
    .bar-fill { height: 100%; border-radius: 99px; }
    .bar-fill.good { background: #16A34A; }
    .bar-fill.warn { background: #D97706; }
    .bar-fill.danger { background: #DC2626; }
    .score-comment { font-size: 0.76rem; color: var(--muted); margin-top: 2px; }

    /* Structure 6-Grid */
    .struct-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .struct-box {
      padding: 8px 10px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #F8FAFC;
      font-size: 0.79rem;
    }
    .struct-box.danger { background: #FEF2F2; border-color: #FCA5A5; }

    /* Passage & Interactive Diagnostic Options */
    .passage-box {
      background: #FCFBF7;
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      padding: 15px 17px;
      font-size: 0.94rem;
      line-height: 1.8;
      margin-bottom: 12px;
    }
    .passage-box p { margin-bottom: 9px; text-indent: 0.5em; }
    .cue-span { border-radius: 4px; padding: 1px 3px; transition: all 0.2s; }
    .cue-span.active { background: #FEF08A; border-bottom: 2px solid #CA8A04; font-weight: 700; }

    .diag-q-card {
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 11px;
      background: #F8FAFC;
    }
    .diag-opt {
      padding: 8px 11px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #fff;
      margin-top: 6px;
      font-size: 0.85rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      transition: all 0.14s;
    }
    .diag-opt:hover { border-color: #2563EB; background: #EFF6FF; }
    .diag-opt.wrong-picked {
      background: #FEF2F2;
      border: 2px solid #DC2626;
      color: #991B1B;
      font-weight: 700;
    }
    .diag-opt.correct-ans {
      background: #F0FDF4;
      border: 2px solid #16A34A;
      color: #166534;
      font-weight: 700;
    }

    /* Dick & Carey & Trap Grid */
    .dc-meter {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 9px;
      margin: 9px 0;
    }
    .dc-box {
      padding: 10px;
      border-radius: 9px;
      border: 1px solid #CBD5E1;
      text-align: center;
      background: #F8FAFC;
    }
    .dc-box.bottleneck { background: #FEF2F2; border: 2px solid #DC2626; }
    .dc-val { font-size: 1.2rem; font-weight: 800; margin-top: 2px; }

    .trap-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 7px; }
    .trap-item {
      padding: 7px 10px;
      border-radius: 8px;
      border: 1px solid #E2E8F0;
      background: #F8FAFC;
      font-size: 0.79rem;
    }
    .trap-item.high-risk { background: #FFF1F2; border-color: #FDA4AF; }

    .bt-chain { display: flex; flex-direction: column; gap: 7px; }
    .bt-node {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #F8FAFC;
      font-size: 0.83rem;
    }
    .bt-node.review { background: #FFFBEB; border: 2px solid #F59E0B; }
    .bt-node.target { background: #EFF6FF; border: 2px solid #2563EB; }

    /* Prescription Stage */
    .rx-banner {
      background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
      color: #fff;
      padding: 15px 20px;
      border-radius: 12px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .rx-cue {
      background: #FEF08A;
      border-bottom: 2px dashed #CA8A04;
      padding: 1px 5px;
      border-radius: 4px;
      font-weight: 800;
      cursor: pointer;
    }
    .rx-cue.active { background: #FDE047; outline: 2px solid #EA580C; }
    .cloze-select {
      padding: 5px 9px;
      border: 2px solid #2563EB;
      border-radius: 6px;
      font-weight: 800;
      color: #1E40AF;
      background: #EFF6FF;
      cursor: pointer;
    }
    .vaccine-card {
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 10px;
      background: #F8FAFC;
    }
    .ox-btn {
      padding: 6px 13px;
      border-radius: 6px;
      border: 1px solid #94A3B8;
      background: #fff;
      font-weight: 800;
      cursor: pointer;
      margin-right: 6px;
    }
    .ox-btn.done-ok { background: #16A34A; color: #fff; border-color: #16A34A; }
    .ox-btn.done-no { background: #DC2626; color: #fff; border-color: #DC2626; }

    /* Stage 3 Real CSAT */
    .csat-q-box {
      border: 1px solid #CBD5E1;
      border-radius: 11px;
      padding: 15px;
      margin-bottom: 14px;
      background: #fff;
    }
    .bogi-box {
      background: #F8FAFC;
      border: 1px solid #94A3B8;
      border-radius: 8px;
      padding: 10px 13px;
      margin: 9px 0;
      font-size: 0.85rem;
      white-space: pre-line;
    }
    .csat-opt-btn {
      width: 100%;
      text-align: left;
      padding: 9px 12px;
      margin-top: 6px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #fff;
      font-size: 0.87rem;
      cursor: pointer;
      display: flex;
      gap: 8px;
      align-items: flex-start;
    }
    .csat-opt-btn:hover { background: #F1F5F9; border-color: #64748B; }
    .csat-opt-btn.correct { background: #DCFCE7; border: 2px solid #16A34A; color: #14532D; font-weight: 700; }
    .csat-opt-btn.wrong { background: #FEE2E2; border: 2px solid #DC2626; color: #7F1D1D; }
    .opt-feedback {
      display: none;
      margin-top: 6px;
      padding: 8px 11px;
      border-radius: 8px;
      font-size: 0.82rem;
      background: #F8FAFC;
      border-left: 4px solid #2563EB;
    }
    .cta-btn {
      background: var(--blue);
      color: #fff;
      border: none;
      padding: 10px 18px;
      border-radius: 9px;
      font-weight: 800;
      font-size: 0.88rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      box-shadow: 0 4px 12px rgba(29, 78, 216, 0.2);
    }
    .cta-btn:hover { background: #1E40AF; }
    .growth-banner {
      background: linear-gradient(135deg, #065F46 0%, #059669 100%);
      color: #fff;
      padding: 15px 18px;
      border-radius: 11px;
      margin-top: 12px;
      display: none;
    }
    .growth-banner.show { display: block; }
    .vocab-bar {
      display: flex;
      gap: 7px;
      flex-wrap: wrap;
      margin-top: 9px;
      padding-top: 9px;
      border-top: 1px dashed #CBD5E1;
    }
    .vocab-chip {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 7px;
      padding: 4px 9px;
      font-size: 0.78rem;
    }
    .vocab-chip b { color: #1E40AF; }

    /* Tables */
    .std-table { width: 100%; border-collapse: collapse; font-size: 0.84rem; background: #fff; }
    .std-table th, .std-table td { border: 1px solid #CBD5E1; padding: 8px 10px; text-align: left; vertical-align: top; }
    .std-table th { background: #1E293B; color: #fff; font-weight: 700; }
    .std-table tr:nth-child(even) { background: #F8FAFC; }
    .filter-bar {
      display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 14px;
      background: #fff; padding: 12px; border-radius: 10px; border: 1px solid var(--border);
    }
    .filter-bar select, .filter-bar input {
      padding: 7px 11px; border: 1px solid #CBD5E1; border-radius: 6px; font-size: 0.86rem;
    }
  </style>
</head>
<body>

  <!-- Global Top Header -->
  <header class="top-bar">
    <div>
      <div class="brand-title">
        <span>🔬 AI 초등 설명문(Expository) 수능형 문해력 코스웨어</span>
        <span class="brand-pill">정밀 X-Ray 진단 + 맞춤형 처방 + 실전 수능 + 프로토타입 완전 통합</span>
      </div>
      <div class="brand-sub">
        ‘어디가·왜·어떻게 부족한지’ 16개 하위기능·6대 구조·어휘·통사·병목 전수 진단 ➔ 1:1 맞춤 처방 클리닉 ➔ KICE 실전 수능 대비
      </div>
    </div>
    <nav class="main-nav">
      <button class="main-tab-btn active" id="mtab-btn-1" onclick="switchMainView(1)">
        🎯 정밀 진단(X-Ray) ➔ 맞춤 처방 ➔ 실전 수능
      </button>
      <button class="main-tab-btn" id="mtab-btn-2" onclick="switchMainView(2)">
        📚 1~6학년 프로토타입 전 단원 비교뷰
      </button>
      <button class="main-tab-btn" id="mtab-btn-3" onclick="switchMainView(3)">
        📐 지문 복잡도·어휘 & 수능 문항 설계 표준
      </button>
      <button class="main-tab-btn" id="mtab-btn-4" onclick="switchMainView(4)">
        🗂️ 설명문 96개 + 공통기초 36개 위계 탐색기
      </button>
    </nav>
  </header>

  <!-- ====================================================================== -->
  <!-- VIEW 1: 정밀 X-Ray 진단 ➔ 1:1 맞춤형 처방 ➔ 실전 수능 대비 (핵심 루프) -->
  <!-- ====================================================================== -->
  <div id="main-view-1" class="main-view active">
    <div class="grade-selector-strip">
      <div style="color:#93C5FD; font-size:0.82rem; font-weight:800;">
        👦👧 진단·처방할 학년별 학습자 페르소나 선택 (초1 ~ 초6 전 학년):
      </div>
      <div class="grade-btn-group" id="persona-btn-group"></div>
    </div>

    <nav class="loop-stepper">
      <div class="stage-step active" id="step-nav-1" onclick="goStage(1)">
        <div class="stage-num">1</div>
        <div>
          <div class="stage-info-title">① 현재 상태 정밀 진단 (X-Ray)</div>
          <div class="stage-info-sub">16하위기능 · 어휘/통사 · 6대구조 · 인지병목 · 오답함정 · 역추적</div>
        </div>
      </div>
      <div class="stage-arrow">➔</div>
      <div class="stage-step" id="step-nav-2" onclick="goStage(2)">
        <div class="stage-num">2</div>
        <div>
          <div class="stage-info-title">② 1:1 맞춤형 처방 클리닉</div>
          <div class="stage-info-sub">선행 결손 징검다리 복습 · 단서·사고구술 조립 · 오답 함정 백신</div>
        </div>
      </div>
      <div class="stage-arrow">➔</div>
      <div class="stage-step" id="step-nav-3" onclick="goStage(3)">
        <div class="stage-num">3</div>
        <div>
          <div class="stage-info-title">③ 실전 수능 대비 문제 & 프로토타입</div>
          <div class="stage-info-sub">교과 개념 지문 · 단서 포착 미션 · KICE 실전 문항 · 성취도 리포트</div>
        </div>
      </div>
    </nav>

    <main class="main-wrap" id="app-workspace"></main>
  </div>

  <!-- ====================================================================== -->
  <!-- VIEW 2: 1~6학년 프로토타입 전 단원 한눈에 비교 뷰 -->
  <!-- ====================================================================== -->
  <div id="main-view-2" class="main-view">
    <main class="main-wrap" id="prototype-gallery-wrap"></main>
  </div>

  <!-- ====================================================================== -->
  <!-- VIEW 3: 지문 복잡도·어휘 등급 & 수능 문항 스케일링 설계 표준 -->
  <!-- ====================================================================== -->
  <div id="main-view-3" class="main-view">
    <main class="main-wrap">
      <div class="card">
        <div class="card-title">
          <span>📏 [Track 2 표준] 초등 1~6학년 설명문 지문 정량·정성 복잡도 규격표</span>
          <span class="badge badge-blue">KReaD · 김광해 어휘 등급 · 2022 개정 교육과정 반영</span>
        </div>
        <table class="std-table">
          <thead>
            <tr>
              <th>학년 (학년군)</th>
              <th>KReaD 지수</th>
              <th>문단 수 / 문장 수</th>
              <th>글자 수 (공백 포함)</th>
              <th>어절 수 (문장당 평균)</th>
              <th>어휘 등급 배합 (Tier 1 : Tier 2 : Tier 3)</th>
              <th>시각 매체 자료 복잡도</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>1학년</b> (초저)</td>
              <td>800 ~ 890</td>
              <td>1문단 (3~5문장)</td>
              <td>100 ~ 180자</td>
              <td>25~45어절 (5~7어절)</td>
              <td><b>90% : 7% : 3%</b> (김광해 1등급 일상어 중심)</td>
              <td>직관적 삽화 · 부위별 명칭 선 잇기 그림</td>
            </tr>
            <tr>
              <td><b>2학년</b> (초저)</td>
              <td>900 ~ 990</td>
              <td>2문단 (5~7문장)</td>
              <td>200 ~ 300자</td>
              <td>50~75어절 (7~8어절)</td>
              <td><b>85% : 10% : 5%</b> (순서·이유 담화표지 도입)</td>
              <td>3~4단계 과정 화살표 그림 · 1차원 간단한 표</td>
            </tr>
            <tr>
              <td><b>3학년</b> (초중)</td>
              <td>1000 ~ 1090</td>
              <td>3문단 (8~11문장)</td>
              <td>320 ~ 450자</td>
              <td>80~110어절 (8~10어절)</td>
              <td><b>78% : 15% : 7%</b> (김광해 2등급 · 다의어·개념어)</td>
              <td>2차원 비교표(행×열) · 기초 구조도</td>
            </tr>
            <tr>
              <td><b>4학년</b> (초중)</td>
              <td>1100 ~ 1190</td>
              <td>3~4문단 (11~15문장)</td>
              <td>450 ~ 600자</td>
              <td>110~150어절 (9~11어절)</td>
              <td><b>72% : 18% : 10%</b> (비례·증감 사고 도구어)</td>
              <td>막대그래프 · 꺾은선그래프 (시계열 추세)</td>
            </tr>
            <tr>
              <td><b>5학년</b> (초고)</td>
              <td>1200 ~ 1290</td>
              <td>4~5문단 (14~18문장)</td>
              <td>600 ~ 750자</td>
              <td>150~190어절 (10~12어절)</td>
              <td><b>65% : 22% : 13%</b> (김광해 3등급 · 한자 개념어)</td>
              <td>원그래프·띠그래프(비율) · 다중 비교표</td>
            </tr>
            <tr>
              <td><b>6학년</b> (초고)</td>
              <td>1300 ~ 1390</td>
              <td>5~6문단 (17~22문장)</td>
              <td>750 ~ 950자</td>
              <td>190~240어절 (11~13어절)</td>
              <td><b>60% : 25% : 15%</b> (중등 브릿지 전문 개념어)</td>
              <td>복합 통계 그래프 · 연쇄 인과(되먹임) 모식도</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card">
        <div class="card-title">
          <span>🎯 [Track 3 표준] 한국교육과정평가원(KICE) 수능형 문항 학년군별 스케일링 & 매력적 오답 6대 공식</span>
          <span class="badge badge-purple">독서(비문학) V1~V3 + 화법과 작문 W1~W5</span>
        </div>
        <table class="std-table" style="margin-bottom:16px;">
          <thead>
            <tr>
              <th>스케일링 요소</th>
              <th>초저 (1~2학년군: 수능 입문기)</th>
              <th>초중 (3~4학년군: 수능 기본기)</th>
              <th>초고 (5~6학년군: 수능 실전기)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>선지 구성 수</b></td>
              <td><b>3지선다</b> (정답 1 + 매력적 오답 2)</td>
              <td><b>4지선다</b> (정답 1 + 매력적 오답 3)</td>
              <td><b>5지선다</b> (평가원 수능 동일 규격)</td>
            </tr>
            <tr>
              <td><b>발문(Stem) 스타일</b></td>
              <td>친화형 의문문 (“윗글의 내용과 <u>같은/다른</u> 것은 무엇인가요?”)</td>
              <td>수능 기본형 (“윗글을 읽고 알 수 있는 내용으로 가장 <u>알맞은</u> 것은?”)</td>
              <td>수능 실전형 (“윗글에 대한 이해로 적절하지 <u>않은</u> 것은?”, “&lt;보기&gt;를 바탕으로 추론한 것은?”)</td>
            </tr>
            <tr>
              <td><b>&lt;보기&gt; 박스 설계</b></td>
              <td>일상 경험·동물 관찰 짧은 상황 (2문장)</td>
              <td>교과서 탐구 실험 조건·단일 표/그래프</td>
              <td>복합 실험·편향된 매체 글·학생 작문 초고 (㉠~㉤ 퇴고)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  </div>

  <!-- ====================================================================== -->
  <!-- VIEW 4: 설명문 96개 + 공통기초 36개 마스터 위계 탐색기 -->
  <!-- ====================================================================== -->
  <div id="main-view-4" class="main-view">
    <main class="main-wrap">
      <div class="card">
        <div class="card-title">
          <span>🗂️ `8_설명문_1_6학년` (96개) & `4_공통기초_1_6학년` (36개) 마스터 위계 탐색기</span>
          <span class="badge badge-green">학년 클릭 시 해당 학년 정밀 진단(X-Ray) 화면으로 즉시 이동</span>
        </div>
        <div class="filter-bar">
          <select id="f-sheet" onchange="renderHierarchyTable()">
            <option value="expository">8_설명문_1_6학년 (96개 목표)</option>
            <option value="common">4_공통기초_1_6학년 (36개 목표)</option>
          </select>
          <select id="f-grade" onchange="renderHierarchyTable()">
            <option value="ALL">전체 학년 (1~6학년)</option>
            <option value="1학년">1학년</option>
            <option value="2학년">2학년</option>
            <option value="3학년">3학년</option>
            <option value="4학년">4학년</option>
            <option value="5학년">5학년</option>
            <option value="6학년">6학년</option>
          </select>
          <select id="f-domain" onchange="renderHierarchyTable()">
            <option value="ALL">전체 영역 (V1·V2·V3·W)</option>
            <option value="사실적">1. 사실적 이해 (V1)</option>
            <option value="추론적">2. 추론적 이해 (V2)</option>
            <option value="비판적">3. 비판적 이해 (V3)</option>
            <option value="표현">4. 표현하기/쓰기 (W)</option>
          </select>
          <input type="text" id="f-keyword" placeholder="하위기능명, Dick&Carey, Mager 목표 검색..." oninput="renderHierarchyTable()" style="flex:1; min-width:220px;" />
        </div>
        <div id="hierarchy-table-wrap"></div>
      </div>
    </main>
  </div>

  <script>
    const MASTER_BUNDLE = __MASTER_BUNDLE_JSON__;
    const SUBSKILL_META = MASTER_BUNDLE.subskill_16_meta;
    const GRADES_DATA = MASTER_BUNDLE.grades_data;
    const HIERARCHY_DATA = __HIERARCHY_JSON__;

    let currentIdx = 4; // 기본: 초5 김민준 (상단에서 초1~초6 모두 선택 가능)
    let currentStage = 1; // 1: 정밀 진단 X-Ray, 2: 맞춤형 처방, 3: 실전 수능 & 프로토타입
    let selectedSubskillIdx = 1; // 16대 하위기능 중 클릭된 셀 인덱스
    let showCueHighlight = false;

    function switchMainView(viewNo) {
      [1, 2, 3, 4].forEach(n => {
        document.getElementById(`mtab-btn-${n}`).classList.toggle('active', n === viewNo);
        document.getElementById(`main-view-${n}`).classList.toggle('active', n === viewNo);
      });
    }

    function renderPersonaBar() {
      const bar = document.getElementById('persona-btn-group');
      bar.innerHTML = GRADES_DATA.map((g, idx) => `
        <button class="grade-pill-btn ${idx === currentIdx ? 'active' : ''}" onclick="selectGradePersona(${idx})">
          ${g.persona_label}
        </button>
      `).join('');
    }

    function selectGradePersona(idx) {
      currentIdx = idx;
      currentStage = 1;
      showCueHighlight = false;
      // 가장 점수가 낮은(critical) 하위기능을 기본 선택
      const skList = GRADES_DATA[idx].xray_overview.subskill_matrix;
      const minIdx = skList.reduce((best, cur, i) => cur.score < skList[best].score ? i : best, 0);
      selectedSubskillIdx = minIdx;

      renderPersonaBar();
      updateStageStepper();
      renderWorkspace();
    }

    function goStage(stageNo) {
      currentStage = stageNo;
      updateStageStepper();
      renderWorkspace();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function updateStageStepper() {
      for (let i = 1; i <= 3; i++) {
        const el = document.getElementById(`step-nav-${i}`);
        el.classList.remove('active', 'done');
        if (i === currentStage) el.classList.add('active');
        else if (i < currentStage) el.classList.add('done');
      }
    }

    function selectSubskillCell(sIdx) {
      selectedSubskillIdx = sIdx;
      renderWorkspace();
    }

    function simulateDiagChoice(qIdx, optNo) {
      const p = GRADES_DATA[currentIdx];
      p.diagnostic_test.questions[qIdx].student_selected = optNo;
      renderWorkspace();
    }

    function togglePassageCues() {
      showCueHighlight = !showCueHighlight;
      document.querySelectorAll('.cue-span').forEach(el => {
        el.classList.toggle('active', showCueHighlight);
      });
      const btn = document.getElementById('cue-toggle-btn');
      if (btn) {
        btn.innerHTML = showCueHighlight ? '💡 Step 1 단서 포착 하이라이팅 (ON)' : '🔍 Step 1 본문 단서 포착 하이라이팅 켜기';
      }
    }

    function renderWorkspace() {
      const p = GRADES_DATA[currentIdx];
      const xr = p.xray_overview;
      const dr = p.diagnosis_report;
      const ws = document.getElementById('app-workspace');

      // Top X-Ray Summary Banner (Always visible so the user knows who this student is and where/how they struggle)
      const xrayHeroHtml = `
        <div class="xray-hero">
          <div class="xray-hero-top">
            <div style="display:flex; align-items:center; gap:12px;">
              <div style="background:#38BDF8; color:#0F172A; font-weight:900; padding:8px 13px; border-radius:10px; font-size:1rem;">
                ${p.grade}
              </div>
              <div>
                <div style="font-size:1.12rem; font-weight:800;">
                  ${p.persona_label}
                  <span class="badge badge-blue" style="margin-left:6px;">집중 타깃: ${p.slot_id} (${p.layer})</span>
                  <span class="badge badge-amber" style="margin-left:4px;">종합 ${xr.overall_score}점 (${xr.percentile})</span>
                </div>
                <div style="font-size:0.8rem; color:#CBD5E1; margin-top:2px;">
                  교과 연계 단원: <b>${p.curriculum_concept.subject} — ${p.curriculum_concept.unit} (${p.curriculum_concept.concept})</b>
                </div>
              </div>
            </div>
            <div style="text-align:right; font-size:0.81rem; background:rgba(255,255,255,0.08); padding:7px 12px; border-radius:8px;">
              <div>현재 읽기 지수: <b style="color:#F87171;">KReaD ${p.complexity_metrics.current_kread}</b></div>
              <div>학년 권장 목표: <b style="color:#38BDF8;">KReaD ${p.complexity_metrics.kread_target}</b></div>
            </div>
          </div>
          <div class="xray-where-how">
            <div class="wh-box">
              <span class="wh-title">📍 [어디가 부족한가? — 결손 위치(Where) 정밀 진단]</span>
              ${xr.where_summary}
            </div>
            <div class="wh-box how">
              <span class="wh-title">🧠 [왜·어떻게 틀리는가? — 인지 병목·오답 메커니즘(How) 진단]</span>
              ${xr.how_summary}
            </div>
          </div>
        </div>
      `;

      // =====================================================================
      // STAGE 1: 현재 상태 정밀 진단 X-RAY 대시보드 (6차원 전수 진단)
      // =====================================================================
      if (currentStage === 1) {
        const dt = p.diagnostic_test;
        const activeSk = xr.subskill_matrix[selectedSubskillIdx];
        const activeMeta = SUBSKILL_META.find(m => m.code === activeSk.code) || {name: activeSk.code, domain: '', desc: ''};

        ws.innerHTML = `
          ${xrayHeroHtml}

          <!-- Row 1: 16 Sub-skill Full X-Ray Matrix + Vocab/Syntax/Structure Diagnosis -->
          <div class="grid-2">
            <!-- Left: 16 Expository Sub-skills Full X-Ray Map + Mini Diagnostic Simulator -->
            <div>
              <div class="card">
                <div class="card-title">
                  <span>🔬 [진단 차원 ①] 설명문 16대 하위기능(V1-1 ~ W5) 전수 X-Ray 히트맵</span>
                  <span class="badge badge-red">셀 클릭 시 결손 원인 상세 표시</span>
                </div>
                <div style="display:flex; gap:10px; font-size:0.76rem; font-weight:700; margin-bottom:8px; color:#475569;">
                  <span>🔴 심각 결손·처방 시급 (50점↓)</span>
                  <span>🟡 불안정·보강 필요 (51~69점)</span>
                  <span>🟢 마스터·안정 (70점↑)</span>
                </div>
                <div class="subskill-grid">
                  ${xr.subskill_matrix.map((sk, sIdx) => {
                    const meta = SUBSKILL_META.find(m => m.code === sk.code) || {name: sk.code};
                    const activeBorder = (sIdx === selectedSubskillIdx) ? 'outline: 3px solid #1D4ED8;' : '';
                    const icon = sk.state === 'critical' ? '🔴' : (sk.state === 'fragile' ? '🟡' : '🟢');
                    return `
                      <div class="sk-cell ${sk.state}" style="${activeBorder}" onclick="selectSubskillCell(${sIdx})">
                        <div class="sk-code">
                          <span>${icon} ${sk.code}</span>
                          <span>${sk.score}점</span>
                        </div>
                        <div class="sk-name">${meta.name}</div>
                      </div>
                    `;
                  }).join('')}
                </div>
                <div class="sk-detail-box">
                  <div style="font-weight:800; color:#0F172A; margin-bottom:3px;">
                    🔎 선택된 하위기능 정밀 진단: <span style="color:#1D4ED8;">[${activeSk.code}] ${activeMeta.name}</span>
                    <span class="badge ${activeSk.state === 'critical' ? 'badge-red' : (activeSk.state === 'fragile' ? 'badge-amber' : 'badge-green')}" style="margin-left:6px;">
                      성취도 ${activeSk.score}점
                    </span>
                  </div>
                  <div style="font-size:0.78rem; color:#64748B; margin-bottom:4px;">• 평가 기준: ${activeMeta.desc}</div>
                  <div style="font-weight:700; color:${activeSk.state === 'critical' ? '#991B1B' : '#1E293B'};">
                    👉 <b>학생 진단 소견:</b> ${activeSk.why}
                  </div>
                </div>
              </div>

              <!-- Mini Diagnostic Test & Live Choice Trap Simulator -->
              <div class="card">
                <div class="card-title">
                  <span>📝 [진단 차원 ②] 미니 진단 지문 & 실시간 오답 함정(D1~D6) 시뮬레이터</span>
                  <span class="badge badge-blue">선지를 직접 클릭해 다른 오답 패턴도 테스트 가능</span>
                </div>
                <div style="font-weight:800; color:#1E40AF; margin-bottom:6px; font-size:0.93rem;">
                  ${dt.passage_title} <span style="font-weight:500; font-size:0.78rem; color:#64748B;">(${dt.passage_spec})</span>
                </div>
                <div class="passage-box">
                  ${dt.paragraphs.map(para => `<p>${para}</p>`).join('')}
                </div>

                ${dt.questions.map((q, qIdx) => {
                  const pickedOpt = q.options.find(o => o.no === q.student_selected) || q.options[0];
                  return `
                    <div class="diag-q-card">
                      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:5px; flex-wrap:wrap; gap:6px;">
                        <span class="badge badge-purple">측정 위계: ${q.target_code} (${q.target_skill})</span>
                        <span class="badge ${pickedOpt.is_correct ? 'badge-green' : 'badge-red'}">
                          ${pickedOpt.is_correct ? '⭕ 현재 선택: 정답 도달' : '❌ 현재 선택(' + pickedOpt.no + '번): ' + pickedOpt.trap}
                        </span>
                      </div>
                      <div style="font-weight:800; font-size:0.89rem; margin-bottom:6px;">
                        진단 문항 ${q.q_no}. ${q.stem}
                      </div>
                      ${q.options.map(opt => {
                        let cls = '';
                        let badgeHtml = '';
                        if (opt.no === q.student_selected && !opt.is_correct) {
                          cls = 'wrong-picked';
                          badgeHtml = `<span class="badge badge-red">선택된 오답 · ${opt.trap}</span>`;
                        } else if (opt.is_correct) {
                          cls = 'correct-ans';
                          badgeHtml = `<span class="badge badge-green">${opt.no === q.student_selected ? '선택된 정답' : '실제 정답'}</span>`;
                        } else {
                          badgeHtml = `<span style="font-size:0.73rem; color:#64748B;">클릭 시 진단 전환: ${opt.trap}</span>`;
                        }
                        return `
                          <div class="diag-opt ${cls}" onclick="simulateDiagChoice(${qIdx}, ${opt.no})">
                            <span><b>${opt.no}번.</b> ${opt.text}</span>
                            ${badgeHtml}
                          </div>
                        `;
                      }).join('')}
                    </div>
                  `;
                }).join('')}
              </div>
            </div>

            <!-- Right: Vocab/Syntax/Structure X-Ray + Dick&Carey Bottleneck + Trap Radar + Backtracking -->
            <div>
              <!-- Dimension 3 & 4: Vocabulary Tier 1~3 / Syntax / 6 Text Structures -->
              <div class="card">
                <div class="card-title">
                  <span>🧬 [진단 차원 ③·④] 어휘(Tier 1·2·3) · 문장 통사 · 6대 설명 구조 정밀 진단</span>
                  <span class="badge badge-purple">언어·구조 결손 해부</span>
                </div>
                <div style="font-size:0.81rem; font-weight:800; color:#1E40AF; margin-bottom:8px;">
                  • 어휘 등급(Tier 1·2·3) 및 문장·통사·담화 해독력 진단
                </div>
                ${xr.vocab_syntax_diag.map(vs => `
                  <div class="score-row">
                    <div class="score-head">
                      <span>${vs.category}</span>
                      <span style="color:${vs.status === 'danger' ? '#DC2626' : (vs.status === 'warn' ? '#D97706' : '#16A34A')};">
                        ${vs.score}점 (${vs.status === 'danger' ? '취약·결손' : (vs.status === 'warn' ? '보통·주의' : '우수')})
                      </span>
                    </div>
                    <div class="bar-bg">
                      <div class="bar-fill ${vs.status}" style="width:${vs.score}%;"></div>
                    </div>
                    <div class="score-comment">👉 ${vs.detail}</div>
                  </div>
                `).join('')}

                <div style="margin-top:14px; padding-top:11px; border-top:1px dashed #CBD5E1;">
                  <div style="font-size:0.81rem; font-weight:800; color:#1E40AF; margin-bottom:8px;">
                    • Meyer 설명문 6대 텍스트 구조별 독해 장악력
                  </div>
                  <div class="struct-grid">
                    ${xr.text_structure_diag.map(st => `
                      <div class="struct-box ${st.status}">
                        <div style="display:flex; justify-content:space-between; font-weight:800;">
                          <span>${st.structure}</span>
                          <span style="color:${st.status === 'danger' ? '#DC2626' : (st.status === 'warn' ? '#D97706' : '#16A34A')};">${st.score}%</span>
                        </div>
                        <div class="bar-bg" style="height:6px; margin-top:4px;">
                          <div class="bar-fill ${st.status}" style="width:${st.score}%;"></div>
                        </div>
                      </div>
                    `).join('')}
                  </div>
                </div>
              </div>

              <!-- Dimension 5 & 6: Dick & Carey Bottleneck + CSAT Trap Vulnerability + Longitudinal Backtracking -->
              <div class="card">
                <div class="card-title">
                  <span>🧭 [진단 차원 ⑤·⑥] 인지 병목(Step 1·2·3) · 수능 6대 함정 취약도 · 결손 뿌리 역추적</span>
                  <span class="badge badge-amber">처방 알고리즘 연동</span>
                </div>

                <div style="font-weight:800; font-size:0.86rem; color:#991B1B; margin-bottom:4px;">
                  🚨 ${dr.bottleneck.diagnosis_title}
                </div>
                <div class="dc-meter">
                  <div class="dc-box ${dr.bottleneck.step1_rate < 60 ? 'bottleneck' : ''}">
                    <div style="font-size:0.75rem; font-weight:700;">Step 1. 지문 단서 포착</div>
                    <div class="dc-val">${dr.bottleneck.step1_rate}%</div>
                  </div>
                  <div class="dc-box ${dr.bottleneck.step2_rate < 60 ? 'bottleneck' : ''}">
                    <div style="font-size:0.75rem; font-weight:700;">Step 2. 관계·맥락 연결</div>
                    <div class="dc-val" style="color:${dr.bottleneck.step2_rate < 60 ? '#DC2626' : '#0F172A'};">${dr.bottleneck.step2_rate}%</div>
                  </div>
                  <div class="dc-box ${dr.bottleneck.step3_rate < 60 ? 'bottleneck' : ''}">
                    <div style="font-size:0.75rem; font-weight:700;">Step 3. 구조화·선지 판별</div>
                    <div class="dc-val" style="color:${dr.bottleneck.step3_rate < 60 ? '#DC2626' : '#0F172A'};">${dr.bottleneck.step3_rate}%</div>
                  </div>
                </div>
                <div style="font-size:0.81rem; background:#FEF2F2; border-left:4px solid #DC2626; padding:8px 11px; border-radius:6px; color:#7F1D1D; margin-bottom:13px;">
                  ${dr.bottleneck.diagnosis_detail}
                </div>

                <div style="font-size:0.81rem; font-weight:800; color:#334155; margin-bottom:6px;">
                  • 수능 6대 매력적 오답 공식(D1~D6) 취약 지수
                </div>
                <div class="trap-grid" style="margin-bottom:13px;">
                  ${dr.trap_radar.map(t => `
                    <div class="trap-item ${t.vuln >= 75 ? 'high-risk' : ''}">
                      <div style="display:flex; justify-content:space-between; font-weight:800;">
                        <span>[${t.code}] ${t.name}</span>
                        <span style="color:${t.vuln >= 75 ? '#DC2626' : '#475569'};">취약도 ${t.vuln}%</span>
                      </div>
                      <div class="bar-bg" style="height:6px; margin-top:4px;">
                        <div class="bar-fill ${t.vuln >= 75 ? 'danger' : (t.vuln >= 50 ? 'warn' : 'good')}" style="width:${t.vuln}%;"></div>
                      </div>
                    </div>
                  `).join('')}
                </div>

                <div style="font-size:0.81rem; font-weight:800; color:#334155; margin-bottom:6px;">
                  • 종적 위계 결손 뿌리 역추적(Root-Cause Backtracking) 경로
                </div>
                <div class="bt-chain">
                  ${dr.backtracking_path.map(node => `
                    <div class="bt-node ${node.status}">
                      <span class="badge ${node.status === 'review' ? 'badge-amber' : (node.status === 'target' ? 'badge-blue' : 'badge-green')}">
                        ${node.grade}
                      </span>
                      <div>
                        <div style="font-weight:800;">${node.code}</div>
                        <div style="font-size:0.8rem; color:#334155;">${node.title}</div>
                      </div>
                    </div>
                  `).join('')}
                </div>

                <div style="margin-top:15px; text-align:right;">
                  <button class="cta-btn" onclick="goStage(2)">
                    💊 진단된 결손(${p.slot_id}) 1:1 맞춤형 처방 클리닉으로 이동 ➔
                  </button>
                </div>
              </div>
            </div>
          </div>
        `;
        return;
      }

      // =====================================================================
      // STAGE 2: 1:1 맞춤형 처방 클리닉
      // =====================================================================
      if (currentStage === 2) {
        const rx = p.prescription_clinic;
        ws.innerHTML = `
          ${xrayHeroHtml}
          <div class="rx-banner">
            <div>
              <div style="font-size:0.76rem; color:#93C5FD; font-weight:800;">AI ADAPTIVE PRESCRIPTION CLINIC</div>
              <div style="font-size:1.12rem; font-weight:800; margin-top:2px;">💊 ${rx.rx_title}</div>
              <div style="font-size:0.84rem; color:#E2E8F0; margin-top:3px;">${rx.rx_reason}</div>
            </div>
            <button class="cta-btn" style="background:#FACC15; color:#0F172A;" onclick="goStage(3)">
              🏆 처방 완료 후 실전 수능 대비 문제 풀기 ➔
            </button>
          </div>

          <div class="grid-2">
            <div>
              <div class="card">
                <div class="card-title">
                  <span>🪜 [처방 1단계] 역추적된 하위 학년 선행 결손 징검다리 복습</span>
                  <span class="badge badge-amber">${rx.step0_remedial.badge}</span>
                </div>
                <div style="background:#FFFBEB; border:1px solid #FDE68A; padding:12px; border-radius:9px; font-size:0.88rem; margin-bottom:11px;">
                  ${rx.step0_remedial.rule_box}
                </div>
                <div style="font-weight:800; font-size:0.89rem; margin-bottom:8px;">
                  ❓ 선행 개념 확인 퀴즈: ${rx.step0_remedial.mini_question}
                </div>
                <div style="display:flex; gap:8px; flex-wrap:wrap;">
                  ${rx.step0_remedial.choices.map((ch, idx) => `
                    <button class="ox-btn" onclick="
                      const ok = (${idx} === ${rx.step0_remedial.choices.indexOf(rx.step0_remedial.correct)});
                      this.className = 'ox-btn ' + (ok ? 'done-ok' : 'done-no');
                      document.getElementById('step0-fb').style.display = 'block';
                    ">${ch}</button>
                  `).join('')}
                </div>
                <div id="step0-fb" class="opt-feedback" style="border-left-color:#16A34A; background:#F0FDF4;">
                  ⭕ ${rx.step0_remedial.feedback}
                </div>
              </div>

              <div class="card">
                <div class="card-title">
                  <span>🧠 [처방 2단계] Dick & Carey 병목 돌파 (Step 1 단서 포착 + Step 2 사고구술 조립)</span>
                  <span class="badge badge-blue">${rx.step1_2_drill.badge}</span>
                </div>
                <div style="font-size:0.8rem; color:#475569; margin-bottom:6px;">
                  💡 지문 속 노란색 <b>단서 칩</b>을 클릭해 깨운 뒤, 아래 사고구술(Think-Aloud) 빈칸을 드롭다운으로 조립하세요.
                </div>
                <div class="passage-box">
                  <p>${rx.step1_2_drill.passage_snippet}</p>
                </div>
                <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:10px; padding:13px;">
                  <div style="font-weight:800; color:#1E40AF; font-size:0.88rem; margin-bottom:8px;">
                    🗣️ 사고구술(Think-Aloud) 구조 조립: ${rx.step1_2_drill.think_aloud_prompt}
                  </div>
                  ${rx.step1_2_drill.cloze_sentences.map(line => {
                    let rendered = line;
                    rx.step1_2_drill.blanks.forEach(b => {
                      const selHtml = `
                        <select class="cloze-select" id="rx-cloze-${b.id}" onchange="checkRxCloze('${b.id}', '${b.correct}')">
                          <option value="">-- 선택 --</option>
                          ${b.options.map(o => `<option value="${o}">${o}</option>`).join('')}
                        </select>
                      `;
                      rendered = rendered.replace(`{${b.id}}`, selHtml);
                    });
                    return `<div style="margin-bottom:8px; font-size:0.88rem; font-weight:700;">${rendered}</div>`;
                  }).join('')}
                </div>
              </div>
            </div>

            <div>
              <div class="card">
                <div class="card-title">
                  <span>🛡️ [처방 3단계] 수능 매력적 오답 함정 백신 드릴 (O/X 판별)</span>
                  <span class="badge badge-red">${rx.step3_vaccine.badge}</span>
                </div>
                <div style="font-size:0.84rem; color:#334155; margin-bottom:11px;">
                  ${rx.step3_vaccine.desc}
                </div>
                ${rx.step3_vaccine.items.map((item, idx) => `
                  <div class="vaccine-card">
                    <div style="font-weight:800; font-size:0.89rem; margin-bottom:8px;">
                      함정 검증 문장 ${idx + 1}. “${item.statement}”
                    </div>
                    <div>
                      <button class="ox-btn" onclick="checkVaccine(this, '${item.answer}', 'O', 'vac-fb-${idx}')">⭕ O (적절함)</button>
                      <button class="ox-btn" onclick="checkVaccine(this, '${item.answer}', 'X', 'vac-fb-${idx}')">❌ X (함정 오답!)</button>
                    </div>
                    <div id="vac-fb-${idx}" class="opt-feedback">
                      <b>[정답: ${item.answer}]</b> ${item.reason}
                    </div>
                  </div>
                `).join('')}

                <div style="margin-top:16px; padding:13px; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                  <div>
                    <div style="font-weight:800; color:#166534; font-size:0.9rem;">✅ 맞춤형 처방 3단계 훈련 완료!</div>
                    <div style="font-size:0.79rem; color:#15803D;">이제 학년 수준에 맞춘 실전 수능 대비 지문과 문항으로 실력을 검증합니다.</div>
                  </div>
                  <button class="cta-btn" style="background:#16A34A;" onclick="goStage(3)">
                    🏆 실전 수능 대비 문제로 이동 ➔
                  </button>
                </div>
              </div>
            </div>
          </div>
        `;

        document.querySelectorAll('.rx-cue').forEach(el => {
          el.onclick = () => el.classList.toggle('active');
        });
        return;
      }

      // =====================================================================
      // STAGE 3: 실전 수능 대비 문제 & 프로토타입(지문 스펙·단서·어휘·수능문항·성장리포트)
      // =====================================================================
      if (currentStage === 3) {
        const csat = p.real_csat_test;
        ws.innerHTML = `
          ${xrayHeroHtml}

          <!-- Prototype Complexity & Curriculum Spec Strip -->
          <div class="card" style="padding:13px 18px; background:#F8FAFC;">
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:10px; font-size:0.8rem;">
              <div><b style="color:#1E40AF;">📚 교과 단원·개념:</b><br>${p.curriculum_concept.subject} — ${p.curriculum_concept.concept}</div>
              <div><b style="color:#1E40AF;">🧩 텍스트 구조:</b><br>${p.curriculum_concept.text_structure}</div>
              <div><b style="color:#1E40AF;">📏 지문 정량 규격:</b><br>${p.complexity_metrics.para_count} · ${p.complexity_metrics.char_count} · ${p.complexity_metrics.eojeol_count}</div>
              <div><b style="color:#1E40AF;">🔤 어휘 등급 배합:</b><br>${p.complexity_metrics.vocab_profile}</div>
              <div><b style="color:#1E40AF;">🎯 Mager 수행 목표:</b><br>${p.mager_goal}</div>
            </div>
          </div>

          <div class="grid-2">
            <!-- Left: Full Passage + Step 1 Cue Mission + Visual Chart + Tier 1~3 Vocab -->
            <div>
              <div class="card">
                <div class="card-title">
                  <span>📖 ${csat.test_title}</span>
                  <button class="ox-btn" id="cue-toggle-btn" style="font-size:0.76rem; padding:4px 10px; border-color:#CA8A04; color:#92400E; background:#FEF9C3;" onclick="togglePassageCues()">
                    🔍 Step 1 본문 단서 포착 하이라이팅 켜기
                  </button>
                </div>
                <div style="background:#EFF6FF; border-left:4px solid #2563EB; padding:7px 11px; border-radius:6px; font-size:0.8rem; color:#1E3A8A; margin-bottom:9px;">
                  <b>${p.prototype_step1_2.step1_mission}</b><br>
                  <span>${p.prototype_step1_2.step2_mission}</span>
                </div>
                <div style="font-weight:800; font-size:1.04rem; color:#0F172A; margin-bottom:8px;">
                  「${csat.passage_title}」 <span style="font-size:0.78rem; color:#64748B; font-weight:600;">(${csat.passage_spec})</span>
                </div>
                <div class="passage-box">
                  ${csat.paragraphs.map((para, i) => `<p><span style="color:#94A3B8;font-size:0.75rem;font-weight:700;margin-right:4px;">[${i+1}문단]</span>${para}</p>`).join('')}
                </div>
                ${csat.visual_html || ''}
                <div class="vocab-bar">
                  ${(csat.vocab_notes || []).map(v => `
                    <div class="vocab-chip">
                      <b>${v.word}</b> <span style="color:#64748B;">(${v.tier})</span>: ${v.desc}
                    </div>
                  `).join('')}
                </div>
              </div>
            </div>

            <!-- Right: Real CSAT Questions & Before/After Growth Report -->
            <div>
              <div class="card">
                <div class="card-title">
                  <span>✍️ Step 3. KICE 평가원 스타일 실전 수능 대비 문항 세트 (${csat.questions.length}문항)</span>
                  <span class="badge badge-green">선지 클릭 시 오답 공식(D1~D6) 즉시 피드백</span>
                </div>
                ${csat.questions.map((q, qIdx) => `
                  <div class="csat-q-box">
                    <div style="margin-bottom:5px;">
                      <span class="badge badge-blue">${q.archetype}</span>
                    </div>
                    <div style="font-weight:800; font-size:0.93rem; margin-bottom:7px;">
                      문항 ${q.q_no}. ${q.stem}
                    </div>
                    ${q.bogi ? `<div class="bogi-box">${q.bogi}</div>` : ''}
                    <div>
                      ${q.options.map(opt => `
                        <button class="csat-opt-btn" onclick="solveCsatOption(this, ${opt.is_correct ? 'true' : 'false'}, 'csat-fb-${qIdx}-${opt.no}')">
                          <span style="font-weight:800;">${opt.no}번.</span>
                          <span>${opt.text}</span>
                        </button>
                        <div id="csat-fb-${qIdx}-${opt.no}" class="opt-feedback" style="border-left-color:${opt.is_correct ? '#16A34A' : '#DC2626'};">
                          <div style="font-weight:800; font-size:0.77rem; color:#475569; margin-bottom:2px;">[${opt.formula}]</div>
                          <div>${opt.explanation}</div>
                        </div>
                      `).join('')}
                    </div>
                  </div>
                `).join('')}

                <div id="growth-banner" class="growth-banner">
                  <div style="font-size:1.02rem; font-weight:800; margin-bottom:5px;">
                    🎉 [정밀 진단 ➔ 맞춤형 처방 ➔ 실전 수능 전이 성공!] 학습자 성취도 Before / After 리포트
                  </div>
                  <div style="font-size:0.84rem; opacity:0.96; margin-bottom:10px;">
                    • <b>핵심 결손 위계(${p.slot_id}) 성취도:</b> 진단 초기 <b>38~42점 (심각 결손)</b> ➔ 처방 및 실전 통과 후 <b>96점 (마스터 달성!)</b><br>
                    • <b>인지 병목 및 오답 함정 방어:</b> Dick & Carey 병목 해소 완료 · 목표 이독성(${p.complexity_metrics.kread_target}) 실전 수능 문항 정복!
                  </div>
                  <button class="cta-btn" style="background:#FACC15; color:#0F172A;" onclick="goStage(1)">
                    📊 1단계 정밀 X-Ray 진단 대시보드 다시 보기
                  </button>
                </div>
              </div>
            </div>
          </div>
        `;
      }
    }

    function checkRxCloze(blankId, correctVal) {
      const el = document.getElementById(`rx-cloze-${blankId}`);
      if (!el) return;
      if (el.value === correctVal) {
        el.style.background = '#DCFCE7';
        el.style.borderColor = '#16A34A';
      } else if (el.value !== '') {
        el.style.background = '#FEE2E2';
        el.style.borderColor = '#DC2626';
      }
    }

    function checkVaccine(btn, correctAns, chosenAns, fbId) {
      btn.classList.remove('done-ok', 'done-no');
      btn.classList.add(correctAns === chosenAns ? 'done-ok' : 'done-no');
      const fb = document.getElementById(fbId);
      if (fb) fb.style.display = 'block';
    }

    function solveCsatOption(btn, isCorrect, fbId) {
      btn.classList.remove('correct', 'wrong');
      btn.classList.add(isCorrect ? 'correct' : 'wrong');
      const fb = document.getElementById(fbId);
      if (fb) fb.style.display = 'block';
      if (isCorrect) {
        const banner = document.getElementById('growth-banner');
        if (banner) banner.classList.add('show');
      }
    }

    // Render View 2: 1~6학년 프로토타입 전 단원 비교 갤러리
    function renderPrototypeGallery() {
      const wrap = document.getElementById('prototype-gallery-wrap');
      wrap.innerHTML = `
        <div class="card">
          <div class="card-title">
            <span>📚 초등 1~6학년 학년별 대표 단원 프로토타입 한눈에 비교하기 (총 6개 학년 세트)</span>
            <span class="badge badge-blue">각 학년의 [이 단원으로 정밀 진단·처방 시작 ➔] 클릭 시 즉시 연동</span>
          </div>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(440px, 1fr)); gap:16px;">
            ${GRADES_DATA.map((g, idx) => `
              <div style="border:1px solid #CBD5E1; border-radius:12px; padding:16px; background:#F8FAFC;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                  <span class="badge badge-blue" style="font-size:0.82rem;">${g.grade} · ${g.slot_id} (${g.layer})</span>
                  <button class="ox-btn" style="border-color:#1D4ED8; color:#1D4ED8; font-size:0.78rem;" onclick="switchMainView(1); selectGradePersona(${idx});">
                    이 단원 정밀 진단·처방·수능 체험 ➔
                  </button>
                </div>
                <div style="font-weight:800; font-size:1rem; color:#0F172A; margin-bottom:4px;">
                  「${g.real_csat_test.passage_title}」
                </div>
                <div style="font-size:0.8rem; color:#475569; margin-bottom:8px;">
                  • <b>교과 개념:</b> ${g.curriculum_concept.subject} (${g.curriculum_concept.concept})<br>
                  • <b>복잡도 규격:</b> ${g.complexity_metrics.para_count} · ${g.complexity_metrics.char_count} · KReaD ${g.complexity_metrics.kread_target}<br>
                  • <b>문항 구성:</b> ${g.complexity_metrics.csat_scaling} (실전 문항 ${g.real_csat_test.questions.length}개 탑재)
                </div>
                <div style="background:#fff; border:1px solid #E2E8F0; border-radius:8px; padding:10px; font-size:0.83rem; max-height:130px; overflow-y:auto;">
                  ${g.real_csat_test.paragraphs[0]}
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    // Render View 4: 96 + 36 Hierarchy Explorer
    function jumpToGradeFromExplorer(gradeStr) {
      const gNum = parseInt(gradeStr);
      const targetIdx = GRADES_DATA.findIndex(g => g.grade_num === gNum);
      if (targetIdx !== -1) {
        switchMainView(1);
        selectGradePersona(targetIdx);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function renderHierarchyTable() {
      const sheetKey = document.getElementById('f-sheet').value;
      const gradeVal = document.getElementById('f-grade').value;
      const domainVal = document.getElementById('f-domain').value;
      const kw = (document.getElementById('f-keyword').value || '').trim().toLowerCase();

      const rows = HIERARCHY_DATA[sheetKey] || [];
      const filtered = rows.filter(r => {
        if (gradeVal !== 'ALL' && r.grade !== gradeVal) return false;
        if (domainVal !== 'ALL' && !(r.domain || '').includes(domainVal)) return false;
        if (kw) {
          const hay = `${r.code} ${r.sub_skill_name} ${r.dc_step1} ${r.dc_step2} ${r.dc_step3} ${r.mager_reading}`.toLowerCase();
          if (!hay.includes(kw)) return false;
        }
        return true;
      });

      const wrap = document.getElementById('hierarchy-table-wrap');
      wrap.innerHTML = `
        <div style="margin-bottom:8px; font-size:0.84rem; color:#475569; font-weight:700;">
          검색된 위계 목표: 총 ${filtered.length}개
        </div>
        <table class="std-table">
          <thead>
            <tr>
              <th style="width:115px;">위계 코드</th>
              <th style="width:90px;">학년 (체험)</th>
              <th style="width:130px;">영역 / 층위</th>
              <th style="width:185px;">세부 하위기능명</th>
              <th>Dick & Carey 3단계 (Step 1 ➔ Step 2 ➔ Step 3)</th>
              <th>이해(독해·점검) Mager 수행목표</th>
            </tr>
          </thead>
          <tbody>
            ${filtered.map(r => `
              <tr>
                <td><b>${r.code}</b></td>
                <td>
                  <b>${r.grade}</b><br>
                  <button class="ox-btn" style="font-size:0.71rem; padding:2px 6px; margin-top:4px; border-color:#2563EB; color:#1D4ED8;" onclick="jumpToGradeFromExplorer('${r.grade}')">
                    진단·처방 체험 ➔
                  </button>
                </td>
                <td>${r.domain}<br><span style="color:#2563EB;font-size:0.77rem;">${r.layer}</span></td>
                <td><b>${r.sub_skill_name}</b></td>
                <td style="font-size:0.79rem;">
                  • <b>Step 1:</b> ${r.dc_step1}<br>
                  • <b>Step 2:</b> ${r.dc_step2}<br>
                  • <b>Step 3:</b> ${r.dc_step3}
                </td>
                <td style="font-size:0.79rem;">${r.mager_reading}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;
    }

    // Initialize
    selectGradePersona(4); // 초5 김민준 기본 로드
    renderPrototypeGallery();
    renderHierarchyTable();
  </script>
</body>
</html>
"""

final_html = HTML_CONTENT.replace(
    "__MASTER_BUNDLE_JSON__", json.dumps(MASTER_BUNDLE, ensure_ascii=False)
).replace(
    "__HIERARCHY_JSON__", json.dumps(HIERARCHY_DATA, ensure_ascii=False)
)

out_path = os.path.join(OUTPUT_DIR, "expository_literacy_courseware.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated all-in-one courseware/output/expository_literacy_courseware.html successfully!")
