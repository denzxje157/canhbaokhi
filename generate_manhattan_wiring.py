# -*- coding: utf-8 -*-
"""
Script to build the Clean-Routed, Professional Manhattan-Style Wiring Studio.
Eliminates all overlapping diagonal wires, uses clean cable channels with rounded right angles,
pin terminal dots, custom focus filters, and modern slate/cyan tech aesthetics.
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sơ Đồ Nối Dây Gọn Gàng Chuẩn Kỹ Thuật - Cảnh Báo Khí Độc</title>
  <!-- Wokwi Elements Official Web Components -->
  <script src="wokwi-elements.bundle.js"></script>
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg: #090d16;
      --workbench-bg: #0f172a;
      --card-bg: rgba(19, 27, 46, 0.96);
      --card-border: rgba(148, 163, 184, 0.16);
      --cyan: #06b6d4;
      --cyan-glow: rgba(6, 182, 212, 0.45);
      --blue: #3b82f6;
      --red: #ef4444;
      --yellow: #f59e0b;
      --green: #10b981;
      --purple: #a855f7;
      --orange: #f97316;
      --text: #f8fafc;
      --muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text);
      overflow: hidden;
      width: 100vw;
      height: 100vh;
    }

    /* TOP HEADER */
    header {
      position: absolute;
      top: 14px;
      left: 20px;
      right: 20px;
      z-index: 50;
      display: flex;
      justify-content: space-between;
      align-items: center;
      pointer-events: none;
    }

    .header-title {
      background: rgba(15, 23, 42, 0.94);
      border: 1px solid rgba(56, 189, 248, 0.28);
      backdrop-filter: blur(16px);
      padding: 10px 22px;
      border-radius: 14px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.55);
      pointer-events: auto;
    }

    .header-title h1 {
      font-size: 1.15rem;
      font-weight: 700;
      background: linear-gradient(135deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .header-title p {
      font-size: 0.8rem;
      color: var(--muted);
      margin-top: 3px;
    }

    .header-actions {
      display: flex;
      gap: 10px;
      pointer-events: auto;
    }

    /* BUTTONS */
    .btn {
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(56, 189, 248, 0.25);
      color: var(--text);
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 0.84rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      backdrop-filter: blur(16px);
      transition: all 0.2s ease;
      box-shadow: 0 4px 16px rgba(0,0,0,0.3);
    }

    .btn:hover {
      border-color: var(--cyan);
      box-shadow: 0 0 15px var(--cyan-glow);
      transform: translateY(-2px);
    }

    .btn-power {
      background: linear-gradient(135deg, #1e293b, #0f172a);
      border-color: #475569;
    }

    .btn-power.active {
      background: linear-gradient(135deg, #059669, #10b981);
      border-color: #34d399;
      color: #fff;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.6);
    }

    /* FILTER BAR */
    .filter-bar {
      position: absolute;
      top: 85px;
      left: 330px;
      z-index: 45;
      display: flex;
      gap: 8px;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 6px 12px;
      border-radius: 12px;
      backdrop-filter: blur(14px);
    }

    .filter-btn {
      background: transparent;
      border: 1px solid transparent;
      color: var(--muted);
      padding: 5px 11px;
      border-radius: 8px;
      font-size: 0.74rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 5px;
    }

    .filter-btn:hover {
      color: #fff;
      background: rgba(51, 65, 85, 0.6);
    }

    .filter-btn.active {
      background: #0284c7;
      color: #fff;
      border-color: #38bdf8;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }

    /* WORKSPACE STAGE */
    #workspace-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      cursor: grab;
      background: 
        radial-gradient(circle at 50% 50%, #131c30 0%, #070a13 100%),
        radial-gradient(rgba(56, 189, 248, 0.08) 1.5px, transparent 1.5px);
      background-size: 100% 100%, 32px 32px;
    }

    #workspace-container:active {
      cursor: grabbing;
    }

    #pan-zoom-stage {
      position: absolute;
      top: 0;
      left: 0;
      width: 2500px;
      height: 1350px;
      transform-origin: 0 0;
      transition: transform 0.05s linear;
    }

    /* SVG WIRING OVERLAY */
    #wiring-svg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 10;
    }

    /* BENCH MAT PLATFORMS */
    .bench-mat {
      position: absolute;
      border-radius: 20px;
      border: 1px solid rgba(148, 163, 184, 0.2);
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(12px);
      box-shadow: 0 25px 60px rgba(0,0,0,0.65), inset 0 0 40px rgba(56, 189, 248, 0.03);
      z-index: 2;
    }

    .bench-mat-title {
      position: absolute;
      top: 16px;
      left: 22px;
      font-size: 0.95rem;
      font-weight: 700;
      color: #38bdf8;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .bench-mat-badge {
      font-size: 0.72rem;
      padding: 3px 9px;
      border-radius: 6px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.25);
      color: #7dd3fc;
    }

    /* ELECTRONIC MODULE CARDS */
    .comp-card {
      position: absolute;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 14px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.55);
      cursor: pointer;
      transition: all 0.25s ease;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .comp-card:hover {
      border-color: #38bdf8;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.35);
      transform: translateY(-3px);
    }

    .comp-card.active {
      border-color: #38bdf8;
      box-shadow: 0 0 30px rgba(56, 189, 248, 0.6);
      outline: 2px solid #38bdf8;
    }

    .comp-card-hdr {
      font-size: 0.8rem;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 8px;
      text-align: center;
      display: flex;
      align-items: center;
      gap: 7px;
    }

    .comp-card-repo {
      font-size: 0.68rem;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      padding: 2px 7px;
      border-radius: 4px;
      margin-top: 6px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .comp-card-repo:hover {
      background: rgba(56, 189, 248, 0.25);
    }

    .real-photo-box {
      width: 140px;
      height: 140px;
      border-radius: 10px;
      overflow: hidden;
      background: #020617;
      border: 1px solid #1e293b;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .real-photo-box img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }

    /* EXPLICIT CONNECTION TERMINAL PORTS */
    .terminal-header {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 5px;
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px solid #1e293b;
    }

    .terminal-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.68rem;
      font-family: monospace;
      padding: 2px 4px;
      background: rgba(15, 23, 42, 0.6);
      border-radius: 4px;
    }

    .port-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: #475569;
      border: 1.5px solid #fff;
      display: inline-block;
      box-shadow: 0 0 6px rgba(0,0,0,0.5);
    }

    .port-dot.p-red { background: #ef4444; }
    .port-dot.p-green { background: #10b981; }
    .port-dot.p-cyan { background: #06b6d4; }
    .port-dot.p-yellow { background: #f59e0b; }
    .port-dot.p-purple { background: #a855f7; }
    .port-dot.p-orange { background: #f97316; }

    /* SIDEBARS */
    .sidebar-left {
      position: absolute;
      top: 85px;
      left: 20px;
      bottom: 25px;
      width: 290px;
      background: rgba(15, 23, 42, 0.94);
      border: 1px solid rgba(56, 189, 248, 0.22);
      border-radius: 16px;
      backdrop-filter: blur(18px);
      z-index: 50;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.55);
      overflow: hidden;
    }

    .sidebar-right {
      position: absolute;
      top: 85px;
      right: 20px;
      bottom: 25px;
      width: 430px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      backdrop-filter: blur(18px);
      z-index: 50;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.55);
      overflow: hidden;
    }

    .panel-hdr {
      padding: 13px 16px;
      border-bottom: 1px solid rgba(56, 189, 248, 0.2);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 700;
      font-size: 0.86rem;
      color: #38bdf8;
      background: rgba(15, 23, 42, 0.75);
    }

    .component-list {
      flex: 1;
      overflow-y: auto;
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .group-label {
      font-size: 0.72rem;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin: 10px 6px 4px 6px;
    }

    .comp-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 10px;
      border-radius: 10px;
      background: rgba(30, 41, 59, 0.35);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .comp-item:hover {
      background: rgba(30, 41, 59, 0.85);
      border-color: rgba(56, 189, 248, 0.3);
    }

    .comp-item.active {
      background: linear-gradient(90deg, rgba(6, 182, 212, 0.2), rgba(59, 130, 246, 0.12));
      border-color: var(--cyan);
      box-shadow: 0 0 14px rgba(6, 182, 212, 0.28);
    }

    .comp-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      flex-shrink: 0;
    }

    .comp-info { flex: 1; min-width: 0; }
    .comp-name { font-size: 0.8rem; font-weight: 600; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .comp-sub { font-size: 0.7rem; color: var(--muted); margin-top: 1px; }

    /* DETAIL PANEL */
    .detail-body {
      flex: 1;
      overflow-y: auto;
      padding: 18px;
    }

    .comp-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.74rem;
      font-weight: 600;
      background: rgba(6, 182, 212, 0.15);
      color: var(--cyan);
      border: 1px solid rgba(6, 182, 212, 0.3);
      margin-bottom: 10px;
    }

    .comp-title-large {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 4px;
    }

    .repo-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #1e293b;
      border: 1px solid #334155;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.74rem;
      color: #38bdf8;
      text-decoration: none;
      margin: 6px 0 12px 0;
      transition: all 0.2s;
    }
    .repo-pill:hover {
      border-color: #38bdf8;
      background: #24344d;
    }

    .pin-mapping-box {
      margin-top: 10px;
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 12px 14px;
    }

    .pin-mapping-box h4 {
      font-size: 0.82rem;
      color: #38bdf8;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .pin-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 0;
      border-bottom: 1px dashed rgba(51, 65, 85, 0.5);
      font-size: 0.8rem;
    }
    .pin-row:last-child { border-bottom: none; }

    .pin-from { color: #e2e8f0; font-weight: 600; display: flex; align-items: center; gap: 6px; }
    .pin-arrow { color: #64748b; font-size: 0.7rem; }
    .pin-to {
      color: #38bdf8;
      font-family: monospace;
      font-weight: 600;
      background: rgba(56, 189, 248, 0.12);
      padding: 2px 7px;
      border-radius: 5px;
      border: 1px solid rgba(56, 189, 248, 0.25);
    }

    .code-snippet-box {
      margin-top: 12px;
      background: #030712;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 10px 12px;
      font-family: "Fira Code", monospace;
      font-size: 0.74rem;
      color: #a5f3fc;
      overflow-x: auto;
      line-height: 1.45;
    }

    .explanation-card {
      margin-top: 14px;
      background: linear-gradient(145deg, rgba(30, 41, 59, 0.5), rgba(15, 23, 42, 0.6));
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 14px;
    }

    .explanation-card h4 {
      font-size: 0.84rem;
      color: #fbbf24;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .explanation-card p {
      font-size: 0.8rem;
      line-height: 1.48;
      color: #cbd5e1;
    }

    .highlight-tip {
      margin-top: 10px;
      padding: 8px 10px;
      border-radius: 8px;
      background: rgba(245, 158, 11, 0.1);
      border-left: 3px solid var(--yellow);
      font-size: 0.76rem;
      color: #fde68a;
      line-height: 1.4;
    }

    .physicsTip {
      margin-top: 10px;
      padding: 8px 10px;
      border-radius: 8px;
      background: rgba(16, 185, 129, 0.1);
      border-left: 3px solid var(--green);
      font-size: 0.76rem;
      color: #a7f3d0;
      line-height: 1.4;
    }

    /* BOTTOM BAR */
    .bottom-bar {
      position: absolute;
      bottom: 25px;
      left: 330px;
      right: 470px;
      height: 60px;
      background: rgba(15, 23, 42, 0.94);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 14px;
      backdrop-filter: blur(18px);
      z-index: 50;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.55);
    }

    .flow-status { display: flex; align-items: center; gap: 12px; }
    .status-dot { width: 12px; height: 12px; border-radius: 50%; background: #64748b; box-shadow: 0 0 8px rgba(100, 116, 139, 0.4); }
    .status-dot.active { background: var(--green); box-shadow: 0 0 12px rgba(16, 185, 129, 0.8); animation: pulse 1.8s infinite; }

    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.7; }
    }

    .sim-levels { display: flex; gap: 8px; }
    .btn-level {
      padding: 6px 12px;
      font-size: 0.78rem;
      border-radius: 8px;
      border: 1px solid #334155;
      background: rgba(30, 41, 59, 0.6);
      color: var(--text);
      cursor: pointer;
      font-weight: 600;
      transition: all 0.2s;
    }

    .btn-level.active-safe { background: var(--green); border-color: #34d399; color: #fff; box-shadow: 0 0 12px rgba(16, 185, 129, 0.4); }
    .btn-level.active-warn { background: var(--yellow); border-color: #fbbf24; color: #000; box-shadow: 0 0 12px rgba(245, 158, 11, 0.4); }
    .btn-level.active-dang { background: var(--red); border-color: #f87171; color: #fff; box-shadow: 0 0 12px rgba(239, 68, 68, 0.5); }
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header>
    <div class="header-title">
      <h1><i class="fa-solid fa-microchip"></i> SƠ ĐỒ ĐI DÂY GỌN GÀNG CHUẨN KỸ THUẬT</h1>
      <p>Hệ Thống Cảnh Báo Khí Độc & Thiếu Oxygen (Đi Dây Vuông Góc Manhattan Bus Routing)</p>
    </div>
    <div class="header-actions">
      <button class="btn btn-power" id="btn-power">
        <i class="fa-solid fa-power-off"></i> <span id="power-text">BẬT NGUỒN PIN (5.2V)</span>
      </button>
      <button class="btn" id="btn-toggle-isolate">
        <i class="fa-solid fa-filter"></i> <span id="isolate-text">Chế Độ: Xem Tất Cả Dây</span>
      </button>
      <button class="btn btn-sound" id="btn-sound">
        <i class="fa-solid fa-volume-high"></i> <span id="sound-text">Âm Thanh: BẬT</span>
      </button>
      <button class="btn" id="btn-reset-view">
        <i class="fa-solid fa-arrows-rotate"></i> Reset Vị Trí
      </button>
    </div>
  </header>

  <!-- BỘ LỌC TỪNG CỤM DÂY NHANH -->
  <div class="filter-bar">
    <span style="font-size: 0.74rem; color: #94a3b8; display: flex; align-items: center; gap: 4px; margin-right: 4px;">
      <i class="fa-solid fa-diagram-project"></i> Lọc Mạch:
    </span>
    <button class="filter-btn active" onclick="filterCircuit('all')">Tất Cả Mạch</button>
    <button class="filter-btn" onclick="filterCircuit('o2_sensor')"><span class="port-dot p-cyan"></span> Oxy (I2C)</button>
    <button class="filter-btn" onclick="filterCircuit('mq7_sensor')"><span class="port-dot p-orange"></span> MQ-7 (CO)</button>
    <button class="filter-btn" onclick="filterCircuit('mq4_sensor')"><span class="port-dot p-yellow"></span> MQ-4 (CH4)</button>
    <button class="filter-btn" onclick="filterCircuit('dht22_sensor')"><span class="port-dot p-purple"></span> DHT22</button>
    <button class="filter-btn" onclick="filterCircuit('cable_cat5e')"><span class="port-dot p-orange"></span> Cáp Cat5e 3-3-2</button>
    <button class="filter-btn" onclick="filterCircuit('alarm_system')"><span class="port-dot p-red"></span> Còi & LED</button>
  </div>

  <!-- SIDEBAR TRÁI: DANH SÁCH THIẾT BỊ -->
  <div class="sidebar-left">
    <div class="panel-hdr">
      <span><i class="fa-solid fa-layer-group"></i> THIẾT BỊ HỆ THỐNG</span>
      <span style="font-size: 0.72rem; color: var(--muted);">11 Module</span>
    </div>
    <div class="component-list" id="comp-list">
      <!-- Render bằng Javascript -->
    </div>
  </div>

  <!-- WORKSPACE PAN & ZOOM STAGE -->
  <div id="workspace-container">
    <div id="pan-zoom-stage">
      <!-- SVG WIRING OVERLAY -->
      <svg id="wiring-svg">
        <defs>
          <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3.5" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>
        <g id="wire-group"></g>
        <g id="particles-group"></g>
      </svg>

      <!-- 1. BỆ ĐỠ KHỐI KHÔNG GIAN KÍN (SLAVE) -->
      <div class="bench-mat" style="left: 70px; top: 120px; width: 1060px; height: 1140px;">
        <div class="bench-mat-title">
          <i class="fa-solid fa-dungeon"></i> KHỐI DƯỚI ĐÁY KHÔNG GIAN KÍN (SLAVE)
          <span class="bench-mat-badge">Thu thập 5 thông số khí & Gom gói JSON</span>
        </div>

        <!-- CẢM BIẾN OXY DFROBOT (SEN0496 / SEN0322) -->
        <div class="comp-card" id="card-o2_sensor" style="left: 40px; top: 60px; width: 240px;" onclick="selectComponent('o2_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-lungs" style="color: #06b6d4;"></i> Cảm Biến Oxy DFRobot</div>
          <div class="real-photo-box">
            <img src="images/sensor_o2.png" alt="DFRobot Gravity O2">
          </div>
          <a class="comp-card-repo" href="https://github.com/DFRobot/DFRobot_OxygenSensor" target="_blank"><i class="fa-brands fa-github"></i> DFRobot_OxygenSensor</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>SCL (Clock)</span><span class="port-dot p-cyan" id="port-o2-scl"></span></div>
            <div class="terminal-row"><span>SDA (Data)</span><span class="port-dot p-cyan" id="port-o2-sda"></span></div>
            <div class="terminal-row"><span>VCC (3.3-5V)</span><span class="port-dot p-red" id="port-o2-vcc"></span></div>
            <div class="terminal-row"><span>GND</span><span class="port-dot p-green" id="port-o2-gnd"></span></div>
          </div>
        </div>

        <!-- CẢM BIẾN KHÍ CO MQ-7 -->
        <div class="comp-card" id="card-mq7_sensor" style="left: 40px; top: 340px; width: 240px;" onclick="selectComponent('mq7_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-skull-crossbones" style="color: #f97316;"></i> Khí Than CO (MQ-7)</div>
          <div class="real-photo-box">
            <img src="images/sensor_mq7.png" alt="Winsen MQ-7">
          </div>
          <a class="comp-card-repo" href="https://github.com/miguel5612/MQSensorsLib" target="_blank"><i class="fa-brands fa-github"></i> miguel5612/MQSensorsLib</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>A0 (Analog)</span><span class="port-dot p-orange" id="port-mq7-a0"></span></div>
            <div class="terminal-row"><span>VCC (5V Nung)</span><span class="port-dot p-red" id="port-mq7-vcc"></span></div>
            <div class="terminal-row"><span>GND</span><span class="port-dot p-green" id="port-mq7-gnd"></span></div>
          </div>
        </div>

        <!-- CẢM BIẾN KHÍ GAS/METAN MQ-4 -->
        <div class="comp-card" id="card-mq4_sensor" style="left: 40px; top: 620px; width: 240px;" onclick="selectComponent('mq4_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-fire-flame-simple" style="color: #eab308;"></i> Khí Gas Metan (MQ-4)</div>
          <div class="real-photo-box">
            <img src="images/sensor_mq4.png" alt="Winsen MQ-4">
          </div>
          <a class="comp-card-repo" href="https://github.com/miguel5612/MQSensorsLib" target="_blank"><i class="fa-brands fa-github"></i> miguel5612/MQSensorsLib</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>A0 (Analog)</span><span class="port-dot p-yellow" id="port-mq4-a0"></span></div>
            <div class="terminal-row"><span>VCC (5V Nung)</span><span class="port-dot p-red" id="port-mq4-vcc"></span></div>
            <div class="terminal-row"><span>GND</span><span class="port-dot p-green" id="port-mq4-gnd"></span></div>
          </div>
        </div>

        <!-- CẢM BIẾN NHIỆT ĐỘ - ĐỘ ẨM DHT22 -->
        <div class="comp-card" id="card-dht22_sensor" style="left: 40px; top: 890px; width: 240px;" onclick="selectComponent('dht22_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-temperature-half" style="color: #3b82f6;"></i> Nhiệt Ẩm DHT22</div>
          <div style="transform: scale(0.9); margin: -5px 0;">
            <wokwi-dht22></wokwi-dht22>
          </div>
          <a class="comp-card-repo" href="https://github.com/adafruit/DHT-sensor-library" target="_blank"><i class="fa-brands fa-github"></i> adafruit/DHT-sensor-library</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>DATA (1-Wire)</span><span class="port-dot p-purple" id="port-dht22-data"></span></div>
            <div class="terminal-row"><span>VCC</span><span class="port-dot p-red" id="port-dht22-vcc"></span></div>
            <div class="terminal-row"><span>GND</span><span class="port-dot p-green" id="port-dht22-gnd"></span></div>
          </div>
        </div>

        <!-- BO MẠCH VI ĐIỀU KHIỂN ESP32 SLAVE (WOKWI ELEMENT) -->
        <div class="comp-card" id="card-esp32_slave" style="left: 450px; top: 360px; width: 270px;" onclick="selectComponent('esp32_slave')">
          <div class="comp-card-hdr"><i class="fa-solid fa-microchip" style="color: #10b981;"></i> ESP32 SLAVE (DƯỚI ĐÁY)</div>
          <div style="transform: scale(0.94); margin: 6px 0;">
            <wokwi-esp32-devkit-v1></wokwi-esp32-devkit-v1>
          </div>
          <div style="font-size: 0.7rem; color: #a5f3fc; text-align: center; margin-top: 4px;">NodeMCU-32S Dual Core 240MHz</div>

          <!-- Các chân kết nối phần cứng chính xác -->
          <div class="terminal-header">
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-esp32s-d21"></span><span>GPIO 21 (I2C SDA Oxy)</span></div>
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-esp32s-d22"></span><span>GPIO 22 (I2C SCL Oxy)</span></div>
            <div class="terminal-row"><span class="port-dot p-orange" id="port-esp32s-gpio35"></span><span>GPIO 35 (ADC1 MQ-7)</span></div>
            <div class="terminal-row"><span class="port-dot p-yellow" id="port-esp32s-gpio34"></span><span>GPIO 34 (ADC1 MQ-4)</span></div>
            <div class="terminal-row"><span class="port-dot p-purple" id="port-esp32s-d4"></span><span>GPIO 4 (1-Wire DHT22)</span></div>
            <div class="terminal-row"><span class="port-dot p-red" id="port-esp32s-vin"></span><span>VIN (+5.2V Nguồn Cáp)</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-esp32s-gnd"></span><span>GND (Mass Chung)</span></div>
            <div class="terminal-row"><span>UART2 TX2 (GPIO 17)</span><span class="port-dot p-purple" id="port-esp32s-tx2"></span></div>
            <div class="terminal-row"><span>UART2 RX2 (GPIO 16)</span><span class="port-dot p-purple" id="port-esp32s-rx2"></span></div>
          </div>
        </div>

        <!-- MODULE MAX485 SLAVE -->
        <div class="comp-card" id="card-max485_slave" style="left: 810px; top: 430px; width: 220px;" onclick="selectComponent('max485_slave')">
          <div class="comp-card-hdr"><i class="fa-solid fa-network-wired" style="color: #a855f7;"></i> MAX485 SLAVE (TX)</div>
          <div style="background: #0284c7; width: 150px; height: 95px; border-radius: 8px; border: 2px solid #38bdf8; display: flex; flex-direction: column; justify-content: space-between; padding: 6px;">
            <div style="font-size: 0.72rem; font-weight: 700; color: #fff; text-align: center;">MAX485 TRANSMITTER</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div style="background: #111827; width: 50px; height: 35px; border-radius: 4px; border: 1px solid #475569; color: #e2e8f0; font-size: 0.62rem; display: flex; align-items: center; justify-content: center; font-family: monospace;">MAX485</div>
              <div style="background: #15803d; width: 45px; height: 42px; border-radius: 4px; border: 1px solid #22c55e; display: flex; flex-direction: column; justify-content: space-around; align-items: center; color: #fff; font-size: 0.65rem; font-weight: 700;">
                <div>A</div><div>B</div>
              </div>
            </div>
            <div style="font-size: 0.6rem; color: #e0f2fe; display: flex; justify-content: space-between; font-family: monospace;">
              <span>VCC</span><span>GND</span><span>RO</span><span>DI</span>
            </div>
          </div>
          <div class="terminal-header">
            <div class="terminal-row"><span class="port-dot p-purple" id="port-max485s-di"></span><span>DI (Nhận từ TX2)</span></div>
            <div class="terminal-row"><span class="port-dot p-purple" id="port-max485s-ro"></span><span>RO (Về RX2)</span></div>
            <div class="terminal-row"><span>Chân A (Vi Sai +)</span><span class="port-dot p-cyan" id="port-max485s-a"></span></div>
            <div class="terminal-row"><span>Chân B (Vi Sai -)</span><span class="port-dot p-cyan" id="port-max485s-b"></span></div>
          </div>
        </div>
      </div>

      <!-- 2. CỤM CÁP MẠNG CAT5E (CỤM 3 - 3 - 2) Ở CHÍNH GIỮA -->
      <div class="comp-card" id="card-cable_cat5e" style="left: 1190px; top: 460px; width: 250px;" onclick="selectComponent('cable_cat5e')">
        <div class="comp-card-hdr"><i class="fa-solid fa-ethernet" style="color: #f59e0b;"></i> Cáp Cat5e (Cụm 3 - 3 - 2)</div>
        <div style="background: #1e293b; border: 1px solid #475569; border-radius: 10px; width: 220px; padding: 10px; text-align: left; font-size: 0.72rem; line-height: 1.6;">
          <div style="color: #f97316; font-weight: 700; display: flex; justify-content: space-between;">
            <span class="port-dot p-orange" id="port-cat5-pwr-left"></span>
            <span>3 Dây Dương (+5.2V)</span>
            <span class="port-dot p-orange" id="port-cat5-pwr-right"></span>
          </div>
          <div style="color: #10b981; font-weight: 700; display: flex; justify-content: space-between; margin-top: 4px;">
            <span class="port-dot p-green" id="port-cat5-gnd-left"></span>
            <span>3 Dây Mass (GND)</span>
            <span class="port-dot p-green" id="port-cat5-gnd-right"></span>
          </div>
          <div style="color: #38bdf8; font-weight: 700; display: flex; justify-content: space-between; margin-top: 4px;">
            <span class="port-dot p-cyan" id="port-cat5-rs485-left"></span>
            <span>2 Dây Vi Sai RS-485</span>
            <span class="port-dot p-cyan" id="port-cat5-rs485-right"></span>
          </div>
        </div>
        <div style="font-size: 0.68rem; color: #facc15; margin-top: 6px; text-align: center;">Vật lý 9: R = &rho;&middot;(l / S) &rarr; Tăng S gấp 3, giảm R 3 lần</div>
      </div>

      <!-- 3. BỆ ĐỠ KHỐI TRÊN MẶT ĐẤT (MASTER) -->
      <div class="bench-mat" style="left: 1490px; top: 120px; width: 950px; height: 1140px;">
        <div class="bench-mat-title">
          <i class="fa-solid fa-tower-broadcast"></i> KHỐI TRÊN MẶT ĐẤT (MASTER)
          <span class="bench-mat-badge">Phân tích nồng độ, Phát Wi-Fi Web Server & Báo động</span>
        </div>

        <!-- NGUỒN XUNG HẠ ÁP LM2596 (5.2V) -->
        <div class="comp-card" id="card-lm2596" style="left: 40px; top: 130px; width: 230px;" onclick="selectComponent('lm2596')">
          <div class="comp-card-hdr"><i class="fa-solid fa-bolt" style="color: #0284c7;"></i> Nguồn Xung LM2596 (5.2V)</div>
          <div style="background: #0369a1; border: 2px solid #38bdf8; border-radius: 8px; width: 140px; height: 100px; padding: 6px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="font-size: 0.68rem; color: #fff; font-weight: 700; text-align: center;">DC-DC BUCK 5.2V</div>
            <div style="display: flex; justify-content: space-around; align-items: center;">
              <div style="background: #1e293b; width: 34px; height: 34px; border-radius: 50%; border: 2px solid #d97706; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #f59e0b;">Cuộn</div>
              <div style="background: #2563eb; width: 25px; height: 35px; border-radius: 4px; border: 1px solid #f59e0b; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #fff;">3296</div>
              <div style="background: #334155; width: 30px; height: 35px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #fff;">Tụ</div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.62rem; color: #fff; font-weight: 700;">
              <span>PIN 7.4-12V</span><span>OUT 5.2V</span>
            </div>
          </div>
          <div class="terminal-header">
            <div class="terminal-row"><span>OUT+ (5.2V Cấp Cáp)</span><span class="port-dot p-orange" id="port-lm2596-out-pos"></span></div>
            <div class="terminal-row"><span>OUT- (Mass GND)</span><span class="port-dot p-green" id="port-lm2596-out-neg"></span></div>
          </div>
        </div>

        <!-- MODULE MAX485 MASTER -->
        <div class="comp-card" id="card-max485_master" style="left: 40px; top: 450px; width: 230px;" onclick="selectComponent('max485_master')">
          <div class="comp-card-hdr"><i class="fa-solid fa-network-wired" style="color: #a855f7;"></i> MAX485 MASTER (RX)</div>
          <div style="background: #0284c7; width: 140px; height: 95px; border-radius: 8px; border: 2px solid #38bdf8; display: flex; flex-direction: column; justify-content: space-between; padding: 6px;">
            <div style="font-size: 0.72rem; font-weight: 700; color: #fff; text-align: center;">MAX485 RECEIVER</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div style="background: #15803d; width: 42px; height: 40px; border-radius: 4px; border: 1px solid #22c55e; display: flex; flex-direction: column; justify-content: space-around; align-items: center; color: #fff; font-size: 0.65rem; font-weight: 700;">
                <div>A</div><div>B</div>
              </div>
              <div style="background: #111827; width: 50px; height: 35px; border-radius: 4px; border: 1px solid #475569; color: #e2e8f0; font-size: 0.62rem; display: flex; align-items: center; justify-content: center; font-family: monospace;">MAX485</div>
            </div>
            <div style="font-size: 0.6rem; color: #e0f2fe; display: flex; justify-content: space-between; font-family: monospace;">
              <span>VCC</span><span>GND</span><span>RO</span><span>DI</span>
            </div>
          </div>
          <div class="terminal-header">
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-max485m-a"></span><span>Chân A (Từ Cáp)</span></div>
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-max485m-b"></span><span>Chân B (Từ Cáp)</span></div>
            <div class="terminal-row"><span>RO (Chuỗi JSON ra)</span><span class="port-dot p-purple" id="port-max485m-ro"></span></div>
          </div>
        </div>

        <!-- BO MẠCH VI ĐIỀU KHIỂN ESP32 MASTER (WOKWI ELEMENT) -->
        <div class="comp-card" id="card-esp32_master" style="left: 350px; top: 360px; width: 270px;" onclick="selectComponent('esp32_master')">
          <div class="comp-card-hdr"><i class="fa-solid fa-microchip" style="color: #6366f1;"></i> ESP32 MASTER (MẶT ĐẤT)</div>
          <div style="transform: scale(0.94); margin: 6px 0;">
            <wokwi-esp32-devkit-v1></wokwi-esp32-devkit-v1>
          </div>
          <div style="font-size: 0.7rem; color: #818cf8; text-align: center; margin-top: 4px;">Web Server AP + Phân tích Logic</div>
          <div class="terminal-header">
            <div class="terminal-row"><span class="port-dot p-purple" id="port-esp32m-rx2"></span><span>GPIO 16 (RX2 Nhận JSON)</span></div>
            <div class="terminal-row"><span>GPIO 21 (I2C SDA OLED)</span><span class="port-dot p-cyan" id="port-esp32m-d21"></span></div>
            <div class="terminal-row"><span>GPIO 22 (I2C SCL OLED)</span><span class="port-dot p-cyan" id="port-esp32m-d22"></span></div>
            <div class="terminal-row"><span>GPIO 23 (Còi Buzzer)</span><span class="port-dot p-red" id="port-esp32m-d23"></span></div>
            <div class="terminal-row"><span>GPIO 19 (LED ĐỎ)</span><span class="port-dot p-red" id="port-esp32m-d19"></span></div>
            <div class="terminal-row"><span>GPIO 5 (LED VÀNG)</span><span class="port-dot p-yellow" id="port-esp32m-d5"></span></div>
            <div class="terminal-row"><span>GPIO 18 (LED XANH)</span><span class="port-dot p-green" id="port-esp32m-d18"></span></div>
          </div>
        </div>

        <!-- MÀN HÌNH OLED 0.96 INCH SSD1306 -->
        <div class="comp-card" id="card-oled_display" style="left: 670px; top: 160px; width: 240px;" onclick="selectComponent('oled_display')">
          <div class="comp-card-hdr"><i class="fa-solid fa-tv" style="color: #38bdf8;"></i> Màn Hình OLED 0.96" SSD1306</div>
          <div style="transform: scale(0.9); margin: -5px 0;">
            <wokwi-ssd1306 id="wokwi-oled"></wokwi-ssd1306>
          </div>
          <div class="terminal-header">
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-oled-sda"></span><span>SDA (Data)</span></div>
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-oled-scl"></span><span>SCL (Clock)</span></div>
            <div class="terminal-row"><span class="port-dot p-red" id="port-oled-vcc"></span><span>VCC</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-oled-gnd"></span><span>GND</span></div>
          </div>
        </div>

        <!-- CÒI BUZZER VÀ 3 ĐÈN LED BÁO ĐỘNG -->
        <div class="comp-card" id="card-alarm_system" style="left: 670px; top: 580px; width: 240px;" onclick="selectComponent('alarm_system')">
          <div class="comp-card-hdr"><i class="fa-solid fa-bullhorn" style="color: #ef4444;"></i> Còi Hú & 3 LED Cảnh Báo</div>
          <div style="display: flex; gap: 14px; align-items: center; margin: 8px 0;">
            <wokwi-buzzer id="wokwi-buzz" style="transform: scale(0.85);"></wokwi-buzzer>
            <div style="display: flex; flex-direction: column; gap: 6px;">
              <wokwi-led id="wokwi-led-red" color="red"></wokwi-led>
              <wokwi-led id="wokwi-led-yellow" color="yellow"></wokwi-led>
              <wokwi-led id="wokwi-led-green" color="green" value="1"></wokwi-led>
            </div>
          </div>
          <div class="terminal-header">
            <div class="terminal-row"><span class="port-dot p-red" id="port-alarm-buzz"></span><span>Còi Hú (+) &larr; GPIO 23</span></div>
            <div class="terminal-row"><span class="port-dot p-red" id="port-alarm-red"></span><span>LED ĐỎ (+) &larr; GPIO 19</span></div>
            <div class="terminal-row"><span class="port-dot p-yellow" id="port-alarm-yel"></span><span>LED VÀNG (+) &larr; GPIO 5</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-alarm-grn"></span><span>LED XANH (+) &larr; GPIO 18</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- BOTTOM BAR: MÔ PHỎNG DÒNG ĐIỆN & CẤP ĐỘ KHÍ -->
  <div class="bottom-bar">
    <div class="flow-status">
      <div class="status-dot" id="flow-dot"></div>
      <div>
        <div class="status-text" id="flow-status-text">Nguồn đang tắt (Chưa có dòng điện)</div>
        <div style="font-size: 0.7rem; color: var(--muted);" id="flow-desc">Bấm 'BẬT NGUỒN PIN' để dòng điện và xung tín hiệu RS485 chuyển động</div>
      </div>
    </div>
    <div class="sim-levels">
      <button class="btn-level active-safe" id="btn-lvl-safe"><i class="fa-solid fa-shield-halved"></i> Mức An Toàn</button>
      <button class="btn-level" id="btn-lvl-warn"><i class="fa-solid fa-triangle-exclamation"></i> Mức Cảnh Báo</button>
      <button class="btn-level" id="btn-lvl-dang"><i class="fa-solid fa-radiation"></i> Mức Nguy Hiểm</button>
    </div>
  </div>

  <!-- SIDEBAR PHẢI: CHI TIẾT NỐI CHÂN & TẠI SAO NỐI NHƯ VẬY -->
  <div class="sidebar-right" id="sidebar-right">
    <div class="panel-hdr">
      <span><i class="fa-solid fa-circle-info"></i> THÔNG TIN KẾT NỐI & CODE THƯ VIỆN</span>
      <span style="font-size: 0.75rem; color: var(--cyan);" id="detail-category">SLAVE</span>
    </div>
    <div class="detail-body" id="detail-body">
      <!-- Sẽ render động khi click linh kiện -->
    </div>
  </div>

  <!-- JAVASCRIPT ĐI DÂY VUÔNG GÓC MANHATTAN ROUTING VÀ TƯƠNG TÁC -->
  <script>
    const COMPONENTS = [
      {
        id: "o2_sensor",
        name: "Cảm Biến Oxygen (O2)",
        sub: "DFRobot Gravity I2C (SEN0496 / SEN0322)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Cảm biến điện hóa I2C",
        repo: "DFRobot/DFRobot_OxygenSensor",
        repoUrl: "https://github.com/DFRobot/DFRobot_OxygenSensor",
        color: "#06b6d4",
        icon: "fa-lungs",
        pins: [
          { from: "SDA (Data)", to: "GPIO 21 (D21)", note: "Chân I2C Data phần cứng ESP32" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22)", note: "Chân I2C Clock phần cứng ESP32" },
          { from: "VCC", to: "3.3V / 5V", note: "Nguồn nuôi mạch cảm biến điện hóa" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" }
        ],
        codeSnippet: `// Khởi tạo thư viện DFRobot_OxygenSensor theo chuẩn I2C\n#include "DFRobot_OxygenSensor.h"\n#define Oxygen_IICAddress ADDRESS_3 // 0x73 mặc định\nDFRobot_OxygenSensor oxygen;\n\nvoid setup() {\n  Wire.begin(21, 22); // SDA=21, SCL=22 phần cứng\n  while(!oxygen.begin(Oxygen_IICAddress)) {\n    Serial.println("I2C Error!"); delay(1000);\n  }\n}\nfloat readO2() {\n  return oxygen.getOxygenData(10); // Đọc trung bình 10 lần\n}`,
        why: "TẠI SAO NỐI VÀO GPIO 21 (SDA) VÀ GPIO 22 (SCL)?",
        whyContent: "Trên vi điều khiển ESP32, bộ điều khiển I2C phần cứng (Hardware I2C Wire) được ghim sẵn tại chân GPIO 21 và GPIO 22. Thư viện DFRobot_OxygenSensor giao tiếp với cảm biến qua địa chỉ hex 0x73 với tốc độ 400kHz. Nối đúng 2 chân này giúp đọc dữ liệu nồng độ Oxy siêu tốc, chính xác đến 0.1% thể tích và không bao giờ bị nghẽn CPU.",
        physicsTip: "💡 Tiêu chuẩn QCVN 34: Khi nồng độ Oxy < 18.0%, chỉ sau 30-45 giây não bộ sẽ mất ý thức ngất xỉu. Bình thường khí quyển đạt 20.9%."
      },
      {
        id: "mq7_sensor",
        name: "Cảm Biến Khí Than Độc (CO)",
        sub: "Winsen MQ-7 (AO Analog Output)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Lò nung sấy SnO2 bán dẫn",
        repo: "miguel5612/MQSensorsLib",
        repoUrl: "https://github.com/miguel5612/MQSensorsLib",
        color: "#f97316",
        icon: "fa-skull-crossbones",
        pins: [
          { from: "A0 (Analog)", to: "GPIO 35", note: "Khối ADC1 Input Only độc lập" },
          { from: "VCC", to: "5.0V (Sau LM2596)", note: "Cấp dòng lò nung sấy nhiệt ~150mA" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung toàn mạch" }
        ],
        codeSnippet: `// Cấu hình thư viện MQUnifiedsensor cho MQ-7\n#include <MQUnifiedsensor.h>\n#define Pin 35 // ADC1 GPIO 35\nMQUnifiedsensor MQ7("ESP-32", 3.3, 12, Pin, "MQ-7");\n\nvoid setup() {\n  MQ7.init();\n  MQ7.setRegressionMethod(1); // PPM = a*ratio^b\n  MQ7.setA(99.042); MQ7.setB(-1.518); // Hệ số chuẩn khí CO\n}\nfloat readCO() {\n  MQ7.update();\n  return MQ7.readSensor();\n}`,
        why: "TẠI SAO NỐI VÀO CHÂN GPIO 35?",
        whyContent: "GPIO 35 là chân Analog thuần túy (Input-Only) thuộc khối ADC1 của ESP32. Nếu cắm nhầm sang khối ADC2 (GPIO 0, 2, 4, 12, 13, 14, 15), việc đọc cảm biến sẽ BỊ TREO HOẶC SAI LỆCH NẶNG khi chip bật sóng Wi-Fi/Bluetooth do bộ phận RF chiếm dụng ADC2. Nối GPIO 35 đảm bảo đo đạc khí than CO liên tục, tuyệt đối không bị nhiễu.",
        physicsTip: "💡 Khí CO chiếm ái lực với hồng cầu gấp 250 lần dưỡng khí Oxy. Mức >= 30 ppm là mức nguy hại phải bật còi báo khẩn cấp ngay."
      },
      {
        id: "mq4_sensor",
        name: "Cảm Biến Khí Gas/Metan (CH4)",
        sub: "Winsen MQ-4 (AO Analog Output)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Cảm biến nung khí cháy",
        repo: "miguel5612/MQSensorsLib",
        repoUrl: "https://github.com/miguel5612/MQSensorsLib",
        color: "#eab308",
        icon: "fa-fire-flame-simple",
        pins: [
          { from: "A0 (Analog)", to: "GPIO 34", note: "Khối ADC1 Input Only độc lập" },
          { from: "VCC", to: "5.0V (Sau LM2596)", note: "Cấp lò nung sấy nhiệt" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" }
        ],
        codeSnippet: `// Cấu hình thư viện MQUnifiedsensor cho MQ-4\n#include <MQUnifiedsensor.h>\n#define PinMQ4 34 // ADC1 GPIO 34\nMQUnifiedsensor MQ4("ESP-32", 3.3, 12, PinMQ4, "MQ-4");\n\nvoid setup() {\n  MQ4.init();\n  MQ4.setRegressionMethod(1);\n  MQ4.setA(1012.7); MQ4.setB(-2.786); // Hệ số khí CH4\n}\nfloat readCH4_LEL() {\n  MQ4.update();\n  float ppm = MQ4.readSensor();\n  return (ppm / 50000.0) * 100.0; // 50,000 ppm = 100% LEL\n}`,
        why: "TẠI SAO NỐI VÀO CHÂN GPIO 34?",
        whyContent: "Tương tự như MQ-7, GPIO 34 thuộc bộ chuyển đổi ADC1 nội bộ độc lập. Cảm biến MQ-4 tiêu thụ dòng sấy lớn, khi nung nóng điện trở SnO2 giảm tỉ lệ với mật độ khí Metan bốc lên từ bùn rác thối. Đo điện áp qua GPIO 34 giúp cập nhật %LEL (Giới hạn nổ dưới) ổn định nhất.",
        physicsTip: "💡 Giới hạn nổ dưới (LEL) của Metan là 5% thể tích. Khi đạt >= 10% LEL, tia lửa nhỏ từ giày dép hay kim loại cũng có thể gây nổ hầm."
      },
      {
        id: "dht22_sensor",
        name: "Cảm Biến Nhiệt Độ - Độ Ẩm",
        sub: "Aosong AM2302 (DHT22)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Bù nhiệt ẩm môi trường",
        repo: "adafruit/DHT-sensor-library",
        repoUrl: "https://github.com/adafruit/DHT-sensor-library",
        color: "#3b82f6",
        icon: "fa-temperature-half",
        pins: [
          { from: "DATA (1-Wire)", to: "GPIO 4 (D4)", note: "Chân 1-Wire số giao tiếp xung" },
          { from: "VCC", to: "3.3V / 5V", note: "Nguồn nuôi cảm biến" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" }
        ],
        codeSnippet: `// Khởi tạo thư viện Adafruit DHT\n#include "DHT.h"\n#define DHTPIN 4     // Nối vào GPIO 4\n#define DHTTYPE DHT22\nDHT dht(DHTPIN, DHTTYPE);\n\nvoid setup() {\n  dht.begin();\n}\nvoid readEnv(float &temp, float &hum) {\n  hum = dht.readHumidity();\n  temp = dht.readTemperature();\n}`,
        why: "TẠI SAO LẠI PHẢI ĐO NHIỆT ĐỘ VÀ ĐỘ ẨM?",
        whyContent: "Dưới cống rãnh ngầm, độ ẩm thường đạt 80-99% và nhiệt độ thay đổi thất thường. Độ nhạy của các đầu đo bán dẫn SnO2 (MQ-4, MQ-7) bị sai lệch theo nhiệt ẩm môi trường. Đọc DHT22 qua GPIO 4 giúp thuật toán bù trừ hệ số trôi nhiệt, đảm bảo số đo PPM không bị báo động giả.",
        physicsTip: "💡 Giao tiếp 1-Wire đọc xung thời gian cực ngắn (26-70 micro-giây) nên cần chân GPIO phản hồi ngắt nhanh như GPIO 4."
      },
      {
        id: "esp32_slave",
        name: "Vi Điều Khiển Dưới Đáy (Slave)",
        sub: "ESP32 NodeMCU 30 Chân (Thu thập & Gom gói)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Đầu não xử lý tín hiệu tại chỗ",
        repo: "kike-canaries/canairio_sensorlib",
        repoUrl: "https://github.com/kike-canaries/canairio_sensorlib",
        color: "#10b981",
        icon: "fa-microchip",
        pins: [
          { from: "GPIO 17 (TX2)", to: "DI (MAX485 Slave)", note: "Bắn chuỗi JSON dữ liệu lên mặt đất" },
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Slave)", note: "Cổng nhận nối tiếp UART2" },
          { from: "VIN & GND", to: "5.2V Cáp Nguồn & GND", note: "Nhận điện từ LM2596 mặt đất cấp xuống" }
        ],
        codeSnippet: `// Đóng gói JSON và gửi qua UART2 RS485\nvoid sendDataToMaster(float o2, float co, float ch4, float t, float h) {\n  String json = "{\\"o2\\":" + String(o2,1) + \n                ",\\"co\\":" + String(co,1) + \n                ",\\"ch4\\":" + String(ch4,1) + \n                ",\\"t\\":" + String(t,1) + \n                ",\\"h\\":" + String(h,1) + "}\\n";\n  Serial2.print(json); // Bắn lên qua MAX485\n}`,
        why: "TẠI SAO DÙNG CHÂN GPIO 16 & GPIO 17 (UART2)?",
        whyContent: "ESP32 có cổng UART0 mặc định (GPIO 1 & GPIO 3) dùng để nạp code và in Serial Monitor gỡ lỗi qua cổng USB máy tính. Nếu cắm MAX485 chung vào UART0, mạch sẽ bị xung đột tín hiệu, không thể nạp code được và chip sẽ bị treo. Sử dụng phần cứng UART2 độc lập tại GPIO 16/17 giúp đường truyền RS485 thông suốt 100%.",
        physicsTip: "💡 ESP32 chạy chip lõi kép Tensilica Xtensa 240MHz, đóng gói chuỗi JSON 5 tham số chỉ trong chưa đầy 2 phần nghìn giây."
      },
      {
        id: "max485_slave",
        name: "Module Chuyển Đổi MAX485 (Slave)",
        sub: "UART sang Vi Sai RS-485",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Bộ kích truyền dẫn chống nhiễu",
        repo: "HardwareSerial RS-485",
        repoUrl: "https://github.com/kike-canaries/canairio_sensorlib",
        color: "#a855f7",
        icon: "fa-network-wired",
        pins: [
          { from: "DI", to: "GPIO 17 (TX2)", note: "Nhận luồng dữ liệu từ ESP32" },
          { from: "RO", to: "GPIO 16 (RX2)", note: "Cổng nối tiếp UART2" },
          { from: "Chân A & B", to: "Cặp Xoắn Đôi Cáp Cat5e", note: "Tín hiệu vi sai chống nhiễu" }
        ],
        codeSnippet: `// Cấu hình cổng Serial2 phần cứng cho MAX485\nvoid setup() {\n  Serial2.begin(9600, SERIAL_8N1, 16, 17);\n}`,
        why: "TẠI SAO PHẢI DÙNG MAX485 THAY VÌ KÉO DÂY UART TRỰC TIẾP?",
        whyContent: "Tín hiệu UART chỉ có biên độ 3.3V và dựa vào mass đất. Nếu kéo dây đi xa 10-30m trong môi trường ẩm ướt đầy sóng điện trường, xung điện áp sẽ bị méo mó hoàn toàn. MAX485 biến đổi thành tín hiệu vi sai (hiệu điện thế giữa 2 dây A và B). Mọi xung nhiễu đánh vào cả 2 dây sẽ tự động triệt tiêu nhau, giúp đường truyền không mất một bit dữ liệu nào.",
        physicsTip: "💡 Nguyên lý vi sai: V_out = V_A - V_B. Nhiễu đánh vào cả 2 dây như nhau nên (V_A + noise) - (V_B + noise) = V_A - V_B (Triệt nhiễu tuyệt đối)."
      },
      {
        id: "cable_cat5e",
        name: "Cáp Mạng Cat5e (Cụm 3 - 3 - 2)",
        sub: "Chiều dài thực tế 10m - 50m",
        group: "ĐƯỜNG TRUYỀN VẬT LÝ",
        badge: "Giải pháp Vật lý 9 chống sụt áp",
        repo: "Quy chuẩn bấm dây T568B",
        repoUrl: "https://github.com",
        color: "#f59e0b",
        icon: "fa-ethernet",
        pins: [
          { from: "3 Dây Dương (+)", to: "Cam, Trắng-Cam, Trắng-Nâu", note: "Tăng tiết diện S gấp 3, giảm điện trở R 3 lần" },
          { from: "3 Dây Mass (GND)", to: "Nâu, Xanh Lá, Trắng-Xanh Lá", note: "Đường hồi tiếp dòng điện nung lớn" },
          { from: "2 Dây Tín Hiệu", to: "Xanh Dương (A) & Trắng-Xanh (B)", note: "Cặp xoắn chống nhiễu vi sai RS485" }
        ],
        codeSnippet: `// Định luật Ohm & Điện trở dây (Vật lý 9):\n// R = rho * (l / S)\n// Chập 3 sợi làm 1 => S tăng gấp 3 => R giảm 3 lần!\n// Kết hợp nâng nguồn LM2596 lên 5.2V bù sụt áp 0.2V đường dài.`,
        why: "TẠI SAO LẠI PHẢI CHẬP CỤM 3 SỢI VÀ CHỈNH NGUỒN LÊN 5.2V?",
        whyContent: "Theo công thức Vật lý 9: R = rho * (l / S). Một sợi lõi đồng cáp Cat5e rất mảnh (S = 0.2 mm2). Với chiều dài 20m cả đi và về, điện trở dây lên tới 3.5 Ohm. Các cảm biến nung nhiệt MQ dưới đáy ngốn dòng 0.4A, gây sụt áp Delta U = I * R = 0.4 * 3.5 = 1.4V! Nếu cấp 5V ở trên, xuống đáy chỉ còn 3.6V làm cảm biến chết đứng. Bằng cách chập 3 sợi làm 1, ta tăng tiết diện S gấp 3 lần, làm giảm R đi 3 lần, kết hợp vặn LM2596 lên 5.2V bù trừ, điện áp dưới đáy luôn duy trì chuẩn 4.95V - 5.05V.",
        physicsTip: "💡 Đây là điểm sáng kiến kỹ thuật đạt điểm tối đa trước ban giám khảo vì áp dụng định luật Ohm và công thức điện trở thuần túy."
      },
      {
        id: "max485_master",
        name: "Module Chuyển Đổi MAX485 (Master)",
        sub: "RS-485 sang UART Vi Điều Khiển",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Bộ thu tín hiệu từ đáy",
        repo: "HardwareSerial RS-485",
        repoUrl: "https://github.com",
        color: "#a855f7",
        icon: "fa-network-wired",
        pins: [
          { from: "Chân A & B", to: "Nhận từ Cáp Cat5e", note: "Tín hiệu vi sai từ dưới đáy đưa lên" },
          { from: "RO", to: "GPIO 16 (RX2 Master)", note: "Đưa chuỗi JSON vào ESP32 Master" }
        ],
        codeSnippet: `// Nhận chuỗi JSON từ Slave\nvoid loop() {\n  if (Serial2.available()) {\n    String json = Serial2.readStringUntil('\\n');\n    parseGasData(json); // Giải mã 5 thông số\n  }\n}`,
        why: "TẠI SAO CẦN 2 MODULE MAX485 Ở HAI ĐẦU?",
        whyContent: "Đường truyền RS-485 là chuẩn truyền thông 2 chiều vi sai (Half-Duplex). Cần có một module phát tại đáy (Transmitter) và một module thu trên mặt đất (Receiver) để giải mã hiệu điện thế vi sai trở lại mức logic TTL 3.3V chuẩn cho vi điều khiển hiểu.",
        physicsTip: "💡 Chuẩn RS-485 cho phép truyền xa tới 1200 mét với tốc độ 100kbps mà không bị suy hao tín hiệu."
      },
      {
        id: "lm2596",
        name: "Mạch Hạ Áp DC-DC LM2596",
        sub: "Hạ Áp Hiệu Suất Cao Xung BUCK (5.2V)",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Nguồn cấp điện toàn hệ thống",
        repo: "Texas Instruments LM2596",
        repoUrl: "https://ti.com",
        color: "#0284c7",
        icon: "fa-bolt",
        pins: [
          { from: "OUT+ (5.2V)", to: "Cụm 3 Dây Dương Cáp Cat5e", note: "Chỉnh chiết áp bù 0.2V sụt áp đường dài" },
          { from: "OUT- (GND)", to: "Cụm 3 Dây Mass Cáp Cat5e", note: "Cực âm chung toàn hệ thống" }
        ],
        codeSnippet: `// Hiệu suất chuyển đổi BUCK xung:\n// H = P_out / P_in > 90% (Mạch luôn mát, tiết kiệm ắc quy gấp đôi LM7805)`,
        why: "TẠI SAO DÙNG NGUỒN XUNG LM2596 MÀ KHÔNG DÙNG LM7805?",
        whyContent: "IC tuyến tính như LM7805 hạ áp bằng cách 'đốt' điện áp thừa thành nhiệt năng. Với dòng 0.5A, nó sẽ tỏa nhiệt bỏng rát và làm pin cạn kiệt rất nhanh (hiệu suất chỉ ~45%). Mạch Buck xung LM2596 chuyển đổi điện năng bằng cuộn cảm với hiệu suất > 90%, mạch luôn mát mẻ và giúp thiết bị chạy liên tục suốt ca làm việc 8-12 tiếng trên bình ắc quy nhỏ.",
        physicsTip: "💡 Công nghệ BUCK xung PWM tần số 150kHz, tiết kiệm năng lượng tối đa cho thiết bị cứu hộ di động."
      },
      {
        id: "esp32_master",
        name: "Bộ Não Xử Lý & Web Server (Master)",
        sub: "Trung Tâm Phân Tích, Báo Động & Web SCADA",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Access Point Wi-Fi & Bộ phân tích",
        repo: "kike-canaries/canairio_sensorlib",
        repoUrl: "https://github.com/kike-canaries/canairio_sensorlib",
        color: "#6366f1",
        icon: "fa-microchip",
        pins: [
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Master)", note: "Nhận chuỗi dữ liệu JSON" },
          { from: "GPIO 21 & 22", to: "OLED SSD1306 (SDA & SCL)", note: "I2C Hiển thị số đo" },
          { from: "GPIO 23", to: "Còi Hú Báo Động (Buzzer)", note: "Bức tường âm thanh ngăn nhảy cứu" },
          { from: "GPIO 19, 5, 18", to: "LED Đỏ - Vàng - Xanh", note: "Báo động 3 cấp độ an toàn" }
        ],
        codeSnippet: `// Hàm xử lý còi đèn theo 3 cấp độ an toàn:\nvoid handleAlarm(float o2, float co, float ch4) {\n  bool isDanger = (o2 < 18.0 || co >= 30.0 || ch4 >= 10.0);\n  bool isWarning = (o2 <= 19.5 || co >= 15.0 || ch4 >= 5.0);\n  if (isDanger) {\n    digitalWrite(19, HIGH); // LED ĐỎ\n    digitalWrite(5, LOW); digitalWrite(18, LOW);\n    digitalWrite(23, (millis()/250)%2); // CÒI HÚ DỒN DẬP\n  } else if (isWarning) {\n    digitalWrite(5, HIGH); // LED VÀNG\n    digitalWrite(19, LOW); digitalWrite(18, LOW);\n    digitalWrite(23, LOW);\n  } else {\n    digitalWrite(18, HIGH); // LED XANH AN TOÀN\n    digitalWrite(19, LOW); digitalWrite(5, LOW);\n    digitalWrite(23, LOW);\n  }\n}`,
        why: "TẠI SAO NỐI CÒI VÀ ĐÈN VÀO CÁC CHÂN 23, 19, 5, 18?",
        whyContent: "Các chân GPIO 23, 19, 18, 5 là các chân Digital Output thuần túy rất an toàn. Chúng không phải là 'Strapping Pin' (như chân 0, 2, 12, 15). Nếu nối còi hoặc đèn nhầm vào các chân Strapping Pin, khi ESP32 khởi động sẽ bị ghim sai mức logic, dẫn đến việc bo mạch bị treo hoặc không thể nạp code qua cổng USB!",
        physicsTip: "💡 Tự phát Wi-Fi Access Point tên 'GIAM_SAT_KHONG_GIAN_KIN' (IP: 192.168.4.1), mở trình duyệt điện thoại là xem được biểu đồ sóng mà hoàn toàn không cần Internet hay 4G!"
      },
      {
        id: "oled_display",
        name: "Màn Hình OLED 0.96 inch",
        sub: "Hiển Thị SSD1306 I2C (0x3C)",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Hiển thị trực quan tại chỗ",
        repo: "adafruit/Adafruit_SSD1306",
        repoUrl: "https://github.com/adafruit/Adafruit_SSD1306",
        color: "#38bdf8",
        icon: "fa-tv",
        pins: [
          { from: "SDA (Data)", to: "GPIO 21 (D21 Master)", note: "Chân I2C Data" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22 Master)", note: "Chân I2C Clock" }
        ],
        codeSnippet: `// Hiển thị 5 thông số lên OLED SSD1306\n#include <Adafruit_SSD1306.h>\nAdafruit_SSD1306 display(128, 64, &Wire, -1);\nvoid updateOLED() {\n  display.clearDisplay();\n  display.setCursor(0,0);\n  display.printf("O2: %.1f%%  CO:%dppm\\n", o2_val, (int)co_val);\n  display.printf("CH4:%.1f%%LEL\\n", ch4_val);\n  display.printf("T:%.1fC  H:%.1f%%\\n", t_val, h_val);\n  display.display();\n}`,
        why: "TẠI SAO DÙNG CHUẨN I2C CHO MÀN HÌNH OLED?",
        whyContent: "Giao thức I2C chỉ cần đúng 2 dây tín hiệu (SDA và SCL) nhưng có thể truyền cả đồ thị và văn bản với tốc độ làm tươi màn hình cao. Người giám sát đứng trên mặt đất liếc nhìn là thấy ngay 5 dòng: Nồng độ Oxy, khí than CO, khí gas Metan, Nhiệt độ và Độ ẩm.",
        physicsTip: "💡 Công nghệ OLED tự phát sáng từng điểm ảnh (Pixel), góc nhìn rộng tới 160 độ, ngoài trời nắng gắt vẫn nhìn rất rõ."
      },
      {
        id: "alarm_system",
        name: "Hệ Thống Đèn 3 Màu & Còi Hú",
        sub: "Còi Buzzer & LED Đỏ - Vàng - Xanh",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Bức tường âm thanh cảnh báo",
        repo: "GPIO Digital Output",
        repoUrl: "https://github.com",
        color: "#ef4444",
        icon: "fa-bullhorn",
        pins: [
          { from: "Còi Buzzer (+)", to: "GPIO 23", note: "Âm lượng > 85dB hú ngắt quãng" },
          { from: "LED ĐỎ (+)", to: "GPIO 19", note: "Sáng khi Oxy < 18% hoặc có độc" },
          { from: "LED VÀNG (+)", to: "GPIO 5", note: "Sáng khi tiệm cận ngưỡng chú ý" },
          { from: "LED XANH (+)", to: "GPIO 18", note: "Sáng khi môi trường an toàn" }
        ],
        codeSnippet: `// Kích hoạt còi hú ngắt quãng dồn dập (250ms bật / 250ms tắt)\nif (isDanger) {\n  digitalWrite(BUZZER_PIN, (millis() / 250) % 2 == 0 ? HIGH : LOW);\n}`,
        why: "TẠI SAO LẠI PHẢI ĐẶT CÒI HÚ VÀ ĐÈN NGAY TẠI MIỆNG CỬA HẦM?",
        whyContent: "ĐÂY LÀ ĐIỂM CỐT LÕI CỨU SỐNG CON NGƯỜI: Các máy đo hiện nay chỉ báo khi người đã cầm máy bước xuống hầm. Khi người dưới ngất, người trên bờ không biết gì sẽ nhảy xuống cứu và chết chùm. Còi hú công suất lớn đặt ngay tại miệng cửa hầm đóng vai trò như 'BỨC TƯỜNG ÂM THANH' đanh thép, cảnh báo trực diện làm người trên bờ giật mình khựng lại, dứt khoát không bước xuống!",
        physicsTip: "💡 Hàm handleAlarm điều khiển còi hú ngắt quãng 250ms bật / 250ms tắt để tạo âm thanh cảnh báo khẩn cấp dồn dập nhất."
      }
    ];

    // DANH SÁCH ĐƯỜNG DÂY NỐI CHUẨN ĐIỂM TỚI ĐIỂM (POINT-TO-POINT PIN PORTS)
    // Mỗi dây có máng đi dây (gutterX) riêng biệt giúp dây đi song song vuông góc cực kỳ đẹp mắt
    const WIRE_DEFINITIONS = [
      // --- CỤM CẢM BIẾN SLAVE ĐẾN ESP32 SLAVE (MÁNG DÂY DỌC X = 370px) ---
      { fromPort: "port-o2-sda", toPort: "port-esp32s-d21", gutterX: 360, color: "#06b6d4", stroke: 3, group: "o2_sensor", label: "I2C SDA (D21)" },
      { fromPort: "port-o2-scl", toPort: "port-esp32s-d22", gutterX: 375, color: "#38bdf8", stroke: 3, group: "o2_sensor", label: "I2C SCL (D22)" },

      { fromPort: "port-mq7-a0", toPort: "port-esp32s-gpio35", gutterX: 390, color: "#f97316", stroke: 3, group: "mq7_sensor", label: "ADC1 GPIO 35 (CO)" },

      { fromPort: "port-mq4-a0", toPort: "port-esp32s-gpio34", gutterX: 405, color: "#eab308", stroke: 3, group: "mq4_sensor", label: "ADC1 GPIO 34 (CH4)" },

      { fromPort: "port-dht22-data", toPort: "port-esp32s-d4", gutterX: 420, color: "#a855f7", stroke: 3, group: "dht22_sensor", label: "1-Wire GPIO 4 (DHT22)" },

      // --- ESP32 SLAVE ĐẾN MAX485 SLAVE (NỐI NGANG TRỰC TIẾP) ---
      { fromPort: "port-esp32s-tx2", toPort: "port-max485s-di", gutterX: 770, color: "#a855f7", stroke: 3, group: "max485_slave", label: "UART2 TX2 -> DI" },
      { fromPort: "port-esp32s-rx2", toPort: "port-max485s-ro", gutterX: 785, color: "#a855f7", stroke: 3, group: "max485_slave", label: "UART2 RX2 <- RO" },

      // --- CÁP CAT5E 3-3-2 NỐI GIỮA HAI KHỐI ---
      // 3 Dây Dương (+5.2V)
      { fromPort: "port-lm2596-out-pos", toPort: "port-cat5-pwr-right", gutterX: 1350, color: "#f97316", stroke: 4.5, group: "cable_cat5e", label: "3 Dây Dương (+5.2V)" },
      { fromPort: "port-cat5-pwr-left", toPort: "port-esp32s-vin", gutterX: 1100, color: "#f97316", stroke: 4.5, group: "cable_cat5e", label: "3 Dây Dương (+5.2V)" },
      // 3 Dây Mass (GND)
      { fromPort: "port-lm2596-out-neg", toPort: "port-cat5-gnd-right", gutterX: 1365, color: "#10b981", stroke: 4.5, group: "cable_cat5e", label: "3 Dây Mass (GND)" },
      { fromPort: "port-cat5-gnd-left", toPort: "port-esp32s-gnd", gutterX: 1085, color: "#10b981", stroke: 4.5, group: "cable_cat5e", label: "3 Dây Mass (GND)" },
      // Cặp Vi Sai RS-485
      { fromPort: "port-max485s-a", toPort: "port-cat5-rs485-left", gutterX: 1115, color: "#06b6d4", stroke: 3.5, group: "cable_cat5e", label: "RS-485 Chân A" },
      { fromPort: "port-cat5-rs485-right", toPort: "port-max485m-a", gutterX: 1380, color: "#06b6d4", stroke: 3.5, group: "cable_cat5e", label: "RS-485 Chân A" },

      // --- MAX485 MASTER ĐẾN ESP32 MASTER ---
      { fromPort: "port-max485m-ro", toPort: "port-esp32m-rx2", gutterX: 300, color: "#a855f7", stroke: 3, group: "max485_master", label: "RO -> RX2 Master" },

      // --- ESP32 MASTER ĐẾN OLED SSD1306 (MÁNG DÂY X = 635px) ---
      { fromPort: "port-esp32m-d21", toPort: "port-oled-sda", gutterX: 635, color: "#06b6d4", stroke: 3, group: "oled_display", label: "I2C SDA (D21)" },
      { fromPort: "port-esp32m-d22", toPort: "port-oled-scl", gutterX: 650, color: "#38bdf8", stroke: 3, group: "oled_display", label: "I2C SCL (D22)" },

      // --- ESP32 MASTER ĐẾN CÒI & 3 LED BÁO ĐỘNG ---
      { fromPort: "port-esp32m-d23", toPort: "port-alarm-buzz", gutterX: 635, color: "#ef4444", stroke: 3.5, group: "alarm_system", label: "GPIO 23 (Còi Buzzer)" },
      { fromPort: "port-esp32m-d19", toPort: "port-alarm-red", gutterX: 650, color: "#ef4444", stroke: 3, group: "alarm_system", label: "GPIO 19 (LED ĐỎ)" },
      { fromPort: "port-esp32m-d5", toPort: "port-alarm-yel", gutterX: 662, color: "#f59e0b", stroke: 3, group: "alarm_system", label: "GPIO 5 (LED VÀNG)" },
      { fromPort: "port-esp32m-d18", toPort: "port-alarm-grn", gutterX: 674, color: "#10b981", stroke: 3, group: "alarm_system", label: "GPIO 18 (LED XANH)" }
    ];

    // HỆ THỐNG ĐI DÂY VUÔNG GÓC MANHATTAN ROUTING
    const wireGroup = document.getElementById("wire-group");
    const particlesGroup = document.getElementById("particles-group");
    const stage = document.getElementById("pan-zoom-stage");
    const container = document.getElementById("workspace-container");

    let currentFilter = "all";
    let isIsolateMode = false;
    let selectedCompId = "o2_sensor";

    let activeWires = [];

    function getPortCoordinates(portId) {
      const portEl = document.getElementById(portId);
      if (!portEl) return null;
      const stageRect = stage.getBoundingClientRect();
      const r = portEl.getBoundingClientRect();
      return {
        x: (r.left + r.width / 2 - stageRect.left) / scale,
        y: (r.top + r.height / 2 - stageRect.top) / scale
      };
    }

    // Vẽ đường dây Manhattan vuông góc có góc bo tròn mượt mà (fillet radius)
    function buildManhattanPath(p1, p2, gutterX, radius = 10) {
      const x1 = p1.x, y1 = p1.y;
      const x2 = p2.x, y2 = p2.y;

      // Hướng di chuyển từ cổng 1 tới máng dây
      const dirX1 = gutterX >= x1 ? 1 : -1;
      const dirX2 = x2 >= gutterX ? 1 : -1;
      const dirY = y2 >= y1 ? 1 : -1;

      // Nếu hai điểm thẳng hàng ngang gần nhau
      if (Math.abs(y1 - y2) < 4) {
        return `M ${x1} ${y1} L ${x2} ${y2}`;
      }

      const r = Math.min(radius, Math.abs(gutterX - x1) / 2, Math.abs(x2 - gutterX) / 2, Math.abs(y2 - y1) / 2);

      return `
        M ${x1} ${y1}
        L ${gutterX - dirX1 * r} ${y1}
        Q ${gutterX} ${y1} ${gutterX} ${y1 + dirY * r}
        L ${gutterX} ${y2 - dirY * r}
        Q ${gutterX} ${y2} ${gutterX + dirX2 * r} ${y2}
        L ${x2} ${y2}
      `;
    }

    function renderAllWires() {
      wireGroup.innerHTML = "";
      particlesGroup.innerHTML = "";
      activeWires.length = 0;

      WIRE_DEFINITIONS.forEach((wDef, index) => {
        const p1 = getPortCoordinates(wDef.fromPort);
        const p2 = getPortCoordinates(wDef.toPort);
        if (!p1 || !p2) return;

        // Tính toán tọa độ máng dây phù hợp
        let gutterX = wDef.gutterX;
        // Nếu máng dây tương đối theo khối Master
        if (wDef.group === "max485_master") gutterX = 1490 + 300;
        if (wDef.group === "oled_display" || wDef.group === "alarm_system") gutterX = 1490 + wDef.gutterX;

        const pathD = buildManhattanPath(p1, p2, gutterX, 12);

        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", pathD);
        path.setAttribute("fill", "none");
        path.setAttribute("stroke", wDef.color);
        path.setAttribute("stroke-width", wDef.stroke);
        path.setAttribute("stroke-linecap", "round");
        path.setAttribute("stroke-linejoin", "round");
        path.id = `wire-${index}`;
        wireGroup.appendChild(path);

        // Hạt electron dòng điện chạy trên dây
        const particles = [];
        for (let p = 0; p < 3; p++) {
          const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          circle.setAttribute("r", wDef.stroke >= 4 ? 4.5 : 3.5);
          circle.setAttribute("fill", "#ffffff");
          circle.setAttribute("filter", "url(#glow)");
          circle.style.display = "none";
          particlesGroup.appendChild(circle);
          particles.push({ circle, progress: p * 0.33 });
        }

        activeWires.push({
          path,
          totalLength: path.getTotalLength(),
          particles,
          wDef
        });
      });

      applyWireVisibility();
    }

    function applyWireVisibility() {
      activeWires.forEach(w => {
        let isHighlighted = false;

        if (currentFilter === "all") {
          isHighlighted = (w.wDef.group === selectedCompId || selectedCompId === "all");
        } else {
          isHighlighted = (w.wDef.group === currentFilter);
        }

        if (isHighlighted) {
          w.path.setAttribute("stroke-width", w.wDef.stroke + 2);
          w.path.setAttribute("opacity", "1");
          w.path.setAttribute("filter", "url(#glow)");
        } else {
          w.path.setAttribute("stroke-width", w.wDef.stroke);
          w.path.setAttribute("opacity", isIsolateMode ? "0.08" : "0.35");
          w.path.removeAttribute("filter");
        }
      });
    }

    // FILTER THEO CỤM MẠCH
    function filterCircuit(groupId) {
      currentFilter = groupId;
      document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
      event.target.classList.add("active");
      if (groupId !== "all") {
        selectComponent(groupId);
      } else {
        applyWireVisibility();
      }
    }

    // CHẾ ĐỘ ISOLATE (CHỈ HIỆN DÂY ĐANG CHỌN)
    const btnToggleIsolate = document.getElementById("btn-toggle-isolate");
    const isolateText = document.getElementById("isolate-text");
    btnToggleIsolate.onclick = () => {
      isIsolateMode = !isIsolateMode;
      isolateText.textContent = isIsolateMode ? "Chế Độ: Chỉ Hiện Dây Chọn" : "Chế Độ: Xem Tất Cả Dây";
      btnToggleIsolate.classList.toggle("active", isIsolateMode);
      applyWireVisibility();
    };

    // PAN & ZOOM BÀN LÀM VIỆC
    let scale = 0.82;
    let panX = -100;
    let panY = -25;
    let isDragging = false;
    let startX = 0, startY = 0;

    function updateTransform() {
      stage.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
      renderAllWires();
    }

    container.addEventListener("mousedown", (e) => {
      if (e.target.closest(".comp-card") || e.target.closest("button") || e.target.closest(".sidebar-left") || e.target.closest(".sidebar-right") || e.target.closest(".filter-bar")) return;
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    });

    window.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform();
    });

    window.addEventListener("mouseup", () => isDragging = false);

    container.addEventListener("wheel", (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.08 : 0.92;
      scale = Math.min(Math.max(scale * zoomFactor, 0.45), 1.8);
      updateTransform();
    }, { passive: false });

    document.getElementById("btn-reset-view").onclick = () => {
      scale = 0.82; panX = -100; panY = -25;
      updateTransform();
    };

    // RENDER DANH SÁCH THIẾT BỊ VÀ CHỌN CHI TIẾT
    const compListContainer = document.getElementById("comp-list");
    const detailBody = document.getElementById("detail-body");
    const detailCategory = document.getElementById("detail-category");

    let curGroup = "";
    COMPONENTS.forEach(comp => {
      if (comp.group !== curGroup) {
        curGroup = comp.group;
        const gLabel = document.createElement("div");
        gLabel.className = "group-label";
        gLabel.textContent = curGroup;
        compListContainer.appendChild(gLabel);
      }

      const item = document.createElement("div");
      item.className = "comp-item";
      item.id = `item-${comp.id}`;
      item.innerHTML = `
        <div class="comp-icon" style="background: ${comp.color}22; color: ${comp.color}; border: 1px solid ${comp.color}44;">
          <i class="fa-solid ${comp.icon}"></i>
        </div>
        <div class="comp-info">
          <div class="comp-name">${comp.name}</div>
          <div class="comp-sub">${comp.sub}</div>
        </div>
      `;
      item.onclick = () => selectComponent(comp.id);
      compListContainer.appendChild(item);
    });

    function selectComponent(compId) {
      selectedCompId = compId;
      const comp = COMPONENTS.find(c => c.id === compId);
      if (!comp) return;

      document.querySelectorAll(".comp-item").forEach(el => el.classList.remove("active"));
      const selectedItem = document.getElementById(`item-${comp.id}`);
      if (selectedItem) selectedItem.classList.add("active");

      document.querySelectorAll(".comp-card").forEach(el => el.classList.remove("active"));
      const cardEl = document.getElementById(`card-${comp.id}`);
      if (cardEl) {
        cardEl.classList.add("active");
        // Di chuyển camera pan mượt mà lại gần vật thể
        const targetX = -cardEl.offsetLeft * scale + (window.innerWidth / 2) - 150;
        const targetY = -cardEl.offsetTop * scale + (window.innerHeight / 2) - 100;
        panX = targetX;
        panY = targetY;
        updateTransform();
      }

      applyWireVisibility();

      // Render nội dung bảng thông tin chi tiết
      detailCategory.textContent = comp.group;
      detailBody.innerHTML = `
        <div class="comp-badge"><i class="fa-solid ${comp.icon}"></i> ${comp.badge}</div>
        <div class="comp-title-large">${comp.name}</div>
        <div style="font-size: 0.82rem; color: #94a3b8;">${comp.sub}</div>

        <a class="repo-pill" href="${comp.repoUrl}" target="_blank">
          <i class="fa-brands fa-github"></i> <b>Repo thư viện:</b> ${comp.repo}
        </a>

        <div class="pin-mapping-box">
          <h4><i class="fa-solid fa-arrows-split-up-and-left"></i> Sơ đồ chân kết nối chính xác</h4>
          ${comp.pins.map(p => `
            <div class="pin-row">
              <span class="pin-from"><i class="fa-solid fa-plug"></i> ${p.from}</span>
              <span class="pin-arrow"><i class="fa-solid fa-arrow-right"></i></span>
              <span class="pin-to">${p.to}</span>
            </div>
            <div style="font-size: 0.72rem; color: #64748b; margin: -2px 0 6px 12px;">• ${p.note}</div>
          `).join('')}
        </div>

        <div class="code-snippet-box">
          <div style="font-size: 0.7rem; color: #fbbf24; margin-bottom: 4px; font-weight: 700;">
            <i class="fa-solid fa-code"></i> Code khởi tạo C++ (Chuẩn Repo):
          </div>
          <pre>${comp.codeSnippet}</pre>
        </div>

        <div class="explanation-card">
          <h4><i class="fa-solid fa-circle-question"></i> ${comp.why}</h4>
          <p>${comp.whyContent}</p>
          <div class="highlight-tip">
            <strong>Ghi nhớ cốt lõi:</strong> Hãy giải thích rõ với thầy cô đây là thiết kế phần cứng có chủ đích để chống xung đột tài nguyên vi điều khiển.
          </div>
          <div class="physicsTip">
            ${comp.physicsTip}
          </div>
        </div>
      `;
    }

    // NÚT BẬT / TẮT NGUỒN PIN VÀ DÒNG ĐIỆN
    const btnPower = document.getElementById("btn-power");
    const powerText = document.getElementById("power-text");
    const flowDot = document.getElementById("flow-dot");
    const flowStatusText = document.getElementById("flow-status-text");
    const flowDesc = document.getElementById("flow-desc");
    let isPowerOn = false;

    btnPower.onclick = () => {
      isPowerOn = !isPowerOn;
      if (isPowerOn) {
        btnPower.classList.add("active");
        powerText.textContent = "NGUỒN ĐANG BẬT (5.2V)";
        flowDot.classList.add("active");
        flowStatusText.textContent = "Dòng điện đang chạy: Pin -> LM2596 (5.2V) -> Cụm 3-3-2 -> Cảm Biến";
        flowDesc.textContent = "Hạt electron phát sáng chuyển động dọc theo cáp nguồn và tín hiệu RS-485";
        activeWires.forEach(w => w.particles.forEach(p => p.circle.style.display = "block"));
      } else {
        btnPower.classList.remove("active");
        powerText.textContent = "BẬT NGUỒN PIN (5.2V)";
        flowDot.classList.remove("active");
        flowStatusText.textContent = "Nguồn đang tắt (Chưa có dòng điện)";
        flowDesc.textContent = "Bấm 'BẬT NGUỒN PIN' để kích hoạt dòng điện và truyền nhận RS485";
        activeWires.forEach(w => w.particles.forEach(p => p.circle.style.display = "none"));
      }
    };

    // HỆ THỐNG ÂM THANH CÒI BUZZER WEB AUDIO API
    let audioCtx = null;
    let isSoundMuted = false;
    const btnSound = document.getElementById("btn-sound");
    const soundText = document.getElementById("sound-text");

    btnSound.onclick = () => {
      isSoundMuted = !isSoundMuted;
      btnSound.classList.toggle("muted", isSoundMuted);
      soundText.textContent = isSoundMuted ? "Âm Thanh: TẮT" : "Âm Thanh: BẬT";
    };

    function playBeep(freq = 2400, duration = 0.18) {
      if (isSoundMuted) return;
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = "square";
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.06, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch(e) {}
    }

    // 3 CẤP ĐỘ CẢNH BÁO KHÍ VÀ ĐIỀU KHIỂN WOKWI ELEMENTS
    const btnSafe = document.getElementById("btn-lvl-safe");
    const btnWarn = document.getElementById("btn-lvl-warn");
    const btnDang = document.getElementById("btn-lvl-dang");
    const ledRed = document.getElementById("wokwi-led-red");
    const ledYellow = document.getElementById("wokwi-led-yellow");
    const ledGreen = document.getElementById("wokwi-led-green");
    let currentAlarmLevel = "safe";

    function setAlarmLevel(lvl) {
      currentAlarmLevel = lvl;
      btnSafe.className = "btn-level" + (lvl === "safe" ? " active-safe" : "");
      btnWarn.className = "btn-level" + (lvl === "warn" ? " active-warn" : "");
      btnDang.className = "btn-level" + (lvl === "dang" ? " active-dang" : "");

      if (lvl === "safe") {
        ledGreen.value = 1;
        ledYellow.value = 0;
        ledRed.value = 0;
      } else if (lvl === "warn") {
        ledGreen.value = 0;
        ledYellow.value = 1;
        ledRed.value = 0;
        playBeep(1800, 0.12);
      } else {
        ledGreen.value = 0;
        ledYellow.value = 0;
        ledRed.value = 1;
        playBeep(2600, 0.25);
      }
    }

    btnSafe.onclick = () => setAlarmLevel("safe");
    btnWarn.onclick = () => setAlarmLevel("warn");
    btnDang.onclick = () => setAlarmLevel("dang");

    // ANIMATION LOOP: DI CHUYỂN ELECTRON DÒNG ĐIỆN VÀ CHỚP NHÁY BÁO ĐỘNG
    let lastTime = performance.now();
    let blinkTimer = 0;
    let lastAlarmBeep = 0;

    function animate(time) {
      requestAnimationFrame(animate);
      const dt = (time - lastTime) / 1000;
      lastTime = time;

      // Di chuyển hạt electron
      if (isPowerOn) {
        activeWires.forEach(w => {
          w.particles.forEach(p => {
            p.progress = (p.progress + dt * 0.42) % 1.0;
            const pt = w.path.getPointAtLength(p.progress * w.totalLength);
            p.circle.setAttribute("cx", pt.x);
            p.circle.setAttribute("cy", pt.y);
          });
        });

        // Chớp nháy còi đèn nguy hiểm
        if (currentAlarmLevel === "dang") {
          blinkTimer += dt;
          if (blinkTimer > 0.25) {
            blinkTimer = 0;
            const isRedOn = ledRed.value === 1;
            ledRed.value = isRedOn ? 0 : 1;
            if (!isRedOn && (time - lastAlarmBeep > 300)) {
              playBeep(2600, 0.15);
              lastAlarmBeep = time;
            }
          }
        }
      }
    }

    // KHỞI ĐỘNG HỆ THỐNG
    window.addEventListener("DOMContentLoaded", () => {
      setTimeout(() => {
        updateTransform();
        selectComponent("o2_sensor");
        requestAnimationFrame(animate);
      }, 100);
    });

    window.addEventListener("resize", () => {
      updateTransform();
    });
  </script>
</body>
</html>
'''

output_path = r"c:\Users\Admin\Downloads\All-Project\canhbaokhi\mo_phong_3d_noi_day\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Successfully generated clean Manhattan-routed wiring studio at: {output_path}")
