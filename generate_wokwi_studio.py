# -*- coding: utf-8 -*-
"""
Script to build the ultimate Photorealistic Hardware Wiring Studio (Wokwi / Fritzing Pro)
Incorporates exact repos:
- miguel5612/MQSensorsLib (MQ-7, MQ-4)
- adafruit/DHT-sensor-library (DHT22)
- DFRobot/DFRobot_OxygenSensor + DFRobot_EOxygenSensor (SEN0496 / SEN0322)
- kike-canaries/canairio_sensorlib
- HardwareSerial RS-485
- Cat5e 3-3-2 Ohm's Law compensation
"""

import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mô Phỏng Nối Dây Thiết Bị Thật - Cảnh Báo Khí Độc</title>
  <!-- Wokwi Elements Official Web Components (High-Definition Vector Electronic Parts) -->
  <script src="wokwi-elements.bundle.js"></script>
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg: #0b1120;
      --workbench-bg: #111a2e;
      --card-bg: rgba(20, 31, 53, 0.92);
      --card-border: #1e293b;
      --cyan: #06b6d4;
      --cyan-glow: rgba(6, 182, 212, 0.4);
      --blue: #3b82f6;
      --red: #ef4444;
      --yellow: #f59e0b;
      --green: #10b981;
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
      top: 15px;
      left: 20px;
      right: 20px;
      z-index: 50;
      display: flex;
      justify-content: space-between;
      align-items: center;
      pointer-events: none;
    }

    .header-title {
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(56, 189, 248, 0.25);
      backdrop-filter: blur(16px);
      padding: 10px 22px;
      border-radius: 14px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.5);
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
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.25);
      color: var(--text);
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 0.85rem;
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

    .btn-sound.muted {
      color: var(--muted);
      opacity: 0.7;
    }

    /* WORKSPACE WORKBENCH CANVAS */
    #workspace-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      cursor: grab;
      background: 
        radial-gradient(circle at 50% 50%, #17243c 0%, #0a0f1d 100%),
        linear-gradient(rgba(56, 189, 248, 0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(56, 189, 248, 0.04) 1px, transparent 1px);
      background-size: 100% 100%, 30px 30px, 30px 30px;
    }

    #workspace-container:active {
      cursor: grabbing;
    }

    #pan-zoom-stage {
      position: absolute;
      top: 0;
      left: 0;
      width: 2400px;
      height: 1400px;
      transform-origin: 0 0;
      transition: transform 0.05s linear;
    }

    /* SVG WIRING OVERLAY LAYER */
    #wiring-svg {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 10;
    }

    /* WORKBENCH BENCH MATS (KHỐI ĐÁY VÀ KHỐI MẶT ĐẤT) */
    .bench-mat {
      position: absolute;
      border-radius: 20px;
      border: 2px solid rgba(56, 189, 248, 0.3);
      background: rgba(13, 22, 41, 0.85);
      backdrop-filter: blur(8px);
      box-shadow: 0 25px 60px rgba(0,0,0,0.6), inset 0 0 30px rgba(56, 189, 248, 0.04);
      z-index: 2;
    }

    .bench-mat-title {
      position: absolute;
      top: 14px;
      left: 20px;
      font-size: 0.92rem;
      font-weight: 700;
      color: #38bdf8;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .bench-mat-badge {
      font-size: 0.72rem;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
    }

    /* ELECTRONIC MODULE COMPONENT CARDS */
    .comp-card {
      position: absolute;
      background: rgba(15, 23, 42, 0.94);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 14px;
      padding: 12px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      cursor: pointer;
      transition: all 0.25s ease;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .comp-card:hover {
      border-color: var(--cyan);
      box-shadow: 0 0 20px var(--cyan-glow);
      transform: translateY(-4px);
    }

    .comp-card.active {
      border-color: #38bdf8;
      box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
      outline: 2px solid #38bdf8;
    }

    .comp-card-hdr {
      font-size: 0.78rem;
      font-weight: 700;
      color: #e2e8f0;
      margin-bottom: 8px;
      text-align: center;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .comp-card-repo {
      font-size: 0.68rem;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      padding: 2px 6px;
      border-radius: 4px;
      margin-top: 4px;
    }

    /* REAL SENSOR PHOTOS IN CARDS */
    .real-photo-box {
      width: 140px;
      height: 140px;
      border-radius: 10px;
      overflow: hidden;
      background: #000;
      border: 1px solid #334155;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .real-photo-box img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.3s ease;
    }

    .comp-card:hover .real-photo-box img {
      transform: scale(1.06);
    }

    /* PIN LABELS ON CARDS */
    .pin-tag-list {
      display: flex;
      gap: 6px;
      margin-top: 8px;
    }

    .pin-tag {
      font-size: 0.65rem;
      font-family: monospace;
      font-weight: 700;
      background: #1e293b;
      color: #cbd5e1;
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid #334155;
    }

    .pin-tag.i2c { border-color: #38bdf8; color: #38bdf8; }
    .pin-tag.adc { border-color: #f59e0b; color: #f59e0b; }
    .pin-tag.onewire { border-color: #34d399; color: #34d399; }
    .pin-tag.uart { border-color: #a855f7; color: #a855f7; }

    /* SIDEBARS */
    .sidebar-left {
      position: absolute;
      top: 85px;
      left: 20px;
      bottom: 25px;
      width: 290px;
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(56, 189, 248, 0.22);
      border-radius: 16px;
      backdrop-filter: blur(18px);
      z-index: 50;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5);
      overflow: hidden;
    }

    .sidebar-right {
      position: absolute;
      top: 85px;
      right: 20px;
      bottom: 25px;
      width: 420px;
      background: rgba(15, 23, 42, 0.94);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      backdrop-filter: blur(18px);
      z-index: 50;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5);
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
      background: rgba(15, 23, 42, 0.7);
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
      background: linear-gradient(90deg, rgba(6, 182, 212, 0.18), rgba(59, 130, 246, 0.12));
      border-color: var(--cyan);
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.25);
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
      font-size: 0.75rem;
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
      right: 460px;
      height: 60px;
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 14px;
      backdrop-filter: blur(18px);
      z-index: 50;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
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

    /* VIEW TIPS */
    .view-tips {
      position: absolute;
      top: 85px;
      left: 330px;
      z-index: 45;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 0.75rem;
      color: var(--muted);
      pointer-events: none;
      backdrop-filter: blur(10px);
    }
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header>
    <div class="header-title">
      <h1><i class="fa-solid fa-microchip"></i> SƠ ĐỒ THIẾT BỊ THẬT & NỐI DÂY CHI TIẾT (WOKWI PRO)</h1>
      <p>Hệ Thống Cảnh Báo Khí Độc & Thiếu Oxygen Trong Không Gian Kín (THCS)</p>
    </div>
    <div class="header-actions">
      <button class="btn btn-power" id="btn-power">
        <i class="fa-solid fa-power-off"></i> <span id="power-text">BẬT NGUỒN PIN (5.2V)</span>
      </button>
      <button class="btn btn-sound" id="btn-sound">
        <i class="fa-solid fa-volume-high"></i> <span id="sound-text">Âm Thanh: BẬT</span>
      </button>
      <button class="btn" id="btn-schematic">
        <i class="fa-solid fa-diagram-project"></i> Sơ Đồ Nguyên Lý 2D
      </button>
      <button class="btn" id="btn-reset-view">
        <i class="fa-solid fa-arrows-rotate"></i> Reset Khung Nhìn
      </button>
    </div>
  </header>

  <div class="view-tips">
    <i class="fa-solid fa-arrows-up-down-left-right"></i> <b>Kéo chuột:</b> Di chuyển toàn bàn làm việc | <b>Cuộn chuột:</b> Thu phóng mượt mà | <b>Click thiết bị:</b> Bật sáng đường dây & mở code thư viện
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
          <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
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
      <div class="bench-mat" style="left: 60px; top: 120px; width: 1040px; height: 1100px;">
        <div class="bench-mat-title">
          <i class="fa-solid fa-dungeon"></i> KHỐI DƯỚI ĐÁY KHÔNG GIAN KÍN (SLAVE)
          <span class="bench-mat-badge">Thu thập 5 thông số khí & Gom gói JSON</span>
        </div>

        <!-- CẢM BIẾN OXY DFROBOT (SEN0496 / SEN0322) -->
        <div class="comp-card" id="card-o2_sensor" style="left: 40px; top: 70px; width: 230px;" onclick="selectComponent('o2_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-lungs" style="color: #06b6d4;"></i> Cảm Biến Oxy DFRobot</div>
          <div class="real-photo-box">
            <img src="images/sensor_o2.png" alt="DFRobot Gravity O2">
          </div>
          <a class="comp-card-repo" href="https://github.com/DFRobot/DFRobot_OxygenSensor" target="_blank"><i class="fa-brands fa-github"></i> DFRobot/DFRobot_OxygenSensor</a>
          <div class="pin-tag-list">
            <span class="pin-tag">VCC</span>
            <span class="pin-tag">GND</span>
            <span class="pin-tag i2c">SCL (D22)</span>
            <span class="pin-tag i2c">SDA (D21)</span>
          </div>
        </div>

        <!-- CẢM BIẾN KHÍ CO MQ-7 -->
        <div class="comp-card" id="card-mq7_sensor" style="left: 40px; top: 350px; width: 230px;" onclick="selectComponent('mq7_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-skull-crossbones" style="color: #f97316;"></i> Cảm Biến Khí Than CO (MQ-7)</div>
          <div class="real-photo-box">
            <img src="images/sensor_mq7.png" alt="Winsen MQ-7">
          </div>
          <a class="comp-card-repo" href="https://github.com/miguel5612/MQSensorsLib" target="_blank"><i class="fa-brands fa-github"></i> miguel5612/MQSensorsLib</a>
          <div class="pin-tag-list">
            <span class="pin-tag">VCC (5V)</span>
            <span class="pin-tag">GND</span>
            <span class="pin-tag adc">A0 (GPIO 35)</span>
          </div>
        </div>

        <!-- CẢM BIẾN KHÍ GAS/METAN MQ-4 -->
        <div class="comp-card" id="card-mq4_sensor" style="left: 40px; top: 620px; width: 230px;" onclick="selectComponent('mq4_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-fire-flame-simple" style="color: #eab308;"></i> Cảm Biến Khí Metan (MQ-4)</div>
          <div class="real-photo-box">
            <img src="images/sensor_mq4.png" alt="Winsen MQ-4">
          </div>
          <a class="comp-card-repo" href="https://github.com/miguel5612/MQSensorsLib" target="_blank"><i class="fa-brands fa-github"></i> miguel5612/MQSensorsLib</a>
          <div class="pin-tag-list">
            <span class="pin-tag">VCC (5V)</span>
            <span class="pin-tag">GND</span>
            <span class="pin-tag adc">A0 (GPIO 34)</span>
          </div>
        </div>

        <!-- CẢM BIẾN NHIỆT ĐỘ - ĐỘ ẨM DHT22 -->
        <div class="comp-card" id="card-dht22_sensor" style="left: 40px; top: 880px; width: 230px;" onclick="selectComponent('dht22_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-temperature-half" style="color: #3b82f6;"></i> Nhiệt Ẩm DHT22 (AM2302)</div>
          <div style="transform: scale(0.9); margin: -5px 0;">
            <wokwi-dht22></wokwi-dht22>
          </div>
          <a class="comp-card-repo" href="https://github.com/adafruit/DHT-sensor-library" target="_blank"><i class="fa-brands fa-github"></i> adafruit/DHT-sensor-library</a>
          <div class="pin-tag-list">
            <span class="pin-tag">VCC</span>
            <span class="pin-tag onewire">DATA (D4)</span>
            <span class="pin-tag">GND</span>
          </div>
        </div>

        <!-- BO MẠCH VI ĐIỀU KHIỂN ESP32 SLAVE (WOKWI ELEMENT) -->
        <div class="comp-card" id="card-esp32_slave" style="left: 400px; top: 380px; width: 260px;" onclick="selectComponent('esp32_slave')">
          <div class="comp-card-hdr"><i class="fa-solid fa-microchip" style="color: #10b981;"></i> ESP32 SLAVE (DƯỚI ĐÁY)</div>
          <div style="transform: scale(0.92); margin: 5px 0;">
            <wokwi-esp32-devkit-v1></wokwi-esp32-devkit-v1>
          </div>
          <div style="font-size: 0.7rem; color: #a5f3fc; text-align: center; margin-top: 4px;">NodeMCU-32S Dual Core 240MHz</div>
          <div class="pin-tag-list" style="flex-wrap: wrap; justify-content: center;">
            <span class="pin-tag i2c">D21/D22 (I2C)</span>
            <span class="pin-tag adc">GPIO 34/35 (ADC1)</span>
            <span class="pin-tag onewire">D4 (DHT22)</span>
            <span class="pin-tag uart">GPIO 16/17 (UART2)</span>
          </div>
        </div>

        <!-- MODULE MAX485 SLAVE -->
        <div class="comp-card" id="card-max485_slave" style="left: 770px; top: 430px; width: 230px;" onclick="selectComponent('max485_slave')">
          <div class="comp-card-hdr"><i class="fa-solid fa-network-wired" style="color: #a855f7;"></i> MAX485 SLAVE (TRANSMIT)</div>
          <div style="background: #0284c7; width: 150px; height: 95px; border-radius: 8px; border: 2px solid #38bdf8; position: relative; display: flex; flex-direction: column; justify-content: space-between; padding: 6px; box-shadow: inset 0 0 10px rgba(0,0,0,0.5);">
            <div style="font-size: 0.72rem; font-weight: 700; color: #fff; text-align: center;">MAX485 MODULE</div>
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
          <div class="pin-tag-list">
            <span class="pin-tag uart">RO (RX2)</span>
            <span class="pin-tag uart">DI (TX2)</span>
            <span class="pin-tag" style="border-color: #38bdf8; color: #38bdf8;">A & B (RS485)</span>
          </div>
        </div>
      </div>

      <!-- 2. CỤM CÁP MẠNG CAT5E (CỤM 3 - 3 - 2) Ở CHÍNH GIỮA -->
      <div class="comp-card" id="card-cable_cat5e" style="left: 1140px; top: 480px; width: 220px;" onclick="selectComponent('cable_cat5e')">
        <div class="comp-card-hdr"><i class="fa-solid fa-ethernet" style="color: #f59e0b;"></i> Cáp Cat5e (Cụm 3 - 3 - 2)</div>
        <div style="background: #334155; border: 2px solid #64748b; border-radius: 10px; width: 170px; padding: 10px; text-align: left; font-size: 0.72rem; line-height: 1.5;">
          <div style="color: #f97316; font-weight: 700;">• 3 Dương (+): Cam, T-Cam, T-Nâu</div>
          <div style="color: #22c55e; font-weight: 700;">• 3 Mass (-): Nâu, X-Lá, T-X-Lá</div>
          <div style="color: #38bdf8; font-weight: 700;">• 2 RS485: Xanh Dương (A/B)</div>
        </div>
        <div style="font-size: 0.68rem; color: #facc15; margin-top: 6px; text-align: center;">Tăng S gấp 3, giảm R 3 lần chống sụt áp</div>
      </div>

      <!-- 3. BỆ ĐỠ KHỐI TRÊN MẶT ĐẤT (MASTER) -->
      <div class="bench-mat" style="left: 1400px; top: 120px; width: 940px; height: 1100px;">
        <div class="bench-mat-title">
          <i class="fa-solid fa-tower-broadcast"></i> KHỐI TRÊN MẶT ĐẤT (MASTER)
          <span class="bench-mat-badge">Phân tích nồng độ, Phát Wi-Fi Web Server & Báo động</span>
        </div>

        <!-- MODULE MAX485 MASTER -->
        <div class="comp-card" id="card-max485_master" style="left: 40px; top: 430px; width: 220px;" onclick="selectComponent('max485_master')">
          <div class="comp-card-hdr"><i class="fa-solid fa-network-wired" style="color: #a855f7;"></i> MAX485 MASTER (RECEIVE)</div>
          <div style="background: #0284c7; width: 140px; height: 95px; border-radius: 8px; border: 2px solid #38bdf8; position: relative; display: flex; flex-direction: column; justify-content: space-between; padding: 6px;">
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
          <div class="pin-tag-list">
            <span class="pin-tag uart">RO (RX2 Master)</span>
            <span class="pin-tag">RE+DE = GND</span>
          </div>
        </div>

        <!-- NGUỒN XUNG HẠ ÁP LM2596 -->
        <div class="comp-card" id="card-lm2596" style="left: 40px; top: 150px; width: 220px;" onclick="selectComponent('lm2596')">
          <div class="comp-card-hdr"><i class="fa-solid fa-bolt" style="color: #0284c7;"></i> Nguồn Xung LM2596 (5.2V)</div>
          <div style="background: #0369a1; border: 2px solid #38bdf8; border-radius: 8px; width: 140px; height: 100px; padding: 6px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="font-size: 0.68rem; color: #fff; font-weight: 700; text-align: center;">DC-DC BUCK 5.2V</div>
            <div style="display: flex; justify-content: space-around; align-items: center;">
              <div style="background: #1e293b; width: 35px; height: 35px; border-radius: 50%; border: 2px solid #d97706; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #f59e0b;">Cuộn</div>
              <div style="background: #2563eb; width: 25px; height: 35px; border-radius: 4px; border: 1px solid #f59e0b; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #fff;">3296</div>
              <div style="background: #334155; width: 30px; height: 35px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #fff;">Tụ</div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.62rem; color: #fff; font-weight: 700;">
              <span>IN: 7.4-12V</span><span>OUT: 5.2V</span>
            </div>
          </div>
          <div class="pin-tag-list">
            <span class="pin-tag" style="border-color: #f97316; color: #f97316;">OUT+ (5.2V)</span>
            <span class="pin-tag" style="border-color: #22c55e; color: #22c55e;">OUT- (GND)</span>
          </div>
        </div>

        <!-- BO MẠCH VI ĐIỀU KHIỂN ESP32 MASTER (WOKWI ELEMENT) -->
        <div class="comp-card" id="card-esp32_master" style="left: 330px; top: 380px; width: 260px;" onclick="selectComponent('esp32_master')">
          <div class="comp-card-hdr"><i class="fa-solid fa-microchip" style="color: #6366f1;"></i> ESP32 MASTER (MẶT ĐẤT)</div>
          <div style="transform: scale(0.92); margin: 5px 0;">
            <wokwi-esp32-devkit-v1></wokwi-esp32-devkit-v1>
          </div>
          <div style="font-size: 0.7rem; color: #818cf8; text-align: center; margin-top: 4px;">Web Server AP + Phân tích Logic</div>
          <div class="pin-tag-list" style="flex-wrap: wrap; justify-content: center;">
            <span class="pin-tag uart">RX2 (GPIO 16)</span>
            <span class="pin-tag i2c">OLED (D21/D22)</span>
            <span class="pin-tag" style="border-color: #ef4444; color: #ef4444;">Buzzer (D23)</span>
            <span class="pin-tag" style="border-color: #f59e0b; color: #f59e0b;">LEDs (D19,5,18)</span>
          </div>
        </div>

        <!-- MÀN HÌNH OLED 0.96 INCH SSD1306 -->
        <div class="comp-card" id="card-oled_display" style="left: 650px; top: 150px; width: 240px;" onclick="selectComponent('oled_display')">
          <div class="comp-card-hdr"><i class="fa-solid fa-tv" style="color: #38bdf8;"></i> Màn Hình OLED 0.96" SSD1306</div>
          <div style="transform: scale(0.9); margin: -5px 0;">
            <wokwi-ssd1306 id="wokwi-oled"></wokwi-ssd1306>
          </div>
          <div class="pin-tag-list">
            <span class="pin-tag">VCC</span><span class="pin-tag">GND</span>
            <span class="pin-tag i2c">SCL (D22)</span>
            <span class="pin-tag i2c">SDA (D21)</span>
          </div>
        </div>

        <!-- CÒI BUZZER VÀ 3 ĐÈN LED BÁO ĐỘNG -->
        <div class="comp-card" id="card-alarm_system" style="left: 650px; top: 620px; width: 240px;" onclick="selectComponent('alarm_system')">
          <div class="comp-card-hdr"><i class="fa-solid fa-bullhorn" style="color: #ef4444;"></i> Còi Hú & 3 LED Cảnh Báo</div>
          <div style="display: flex; gap: 14px; align-items: center; margin: 8px 0;">
            <wokwi-buzzer id="wokwi-buzz" style="transform: scale(0.85);"></wokwi-buzzer>
            <div style="display: flex; flex-direction: column; gap: 6px;">
              <wokwi-led id="wokwi-led-red" color="red"></wokwi-led>
              <wokwi-led id="wokwi-led-yellow" color="yellow"></wokwi-led>
              <wokwi-led id="wokwi-led-green" color="green" value="1"></wokwi-led>
            </div>
          </div>
          <div class="pin-tag-list" style="flex-wrap: wrap;">
            <span class="pin-tag" style="border-color: #ef4444; color: #ef4444;">Còi: GPIO 23</span>
            <span class="pin-tag" style="border-color: #ef4444; color: #ef4444;">Đỏ: D19</span>
            <span class="pin-tag" style="border-color: #f59e0b; color: #f59e0b;">Vàng: D5</span>
            <span class="pin-tag" style="border-color: #10b981; color: #10b981;">Xanh: D18</span>
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

  <!-- JAVASCRIPT LOGIC TƯƠNG TÁC TOÀN HỆ THỐNG -->
  <script>
    // DỮ LIỆU ĐẦY ĐỦ CÁC THIẾT BỊ, CHÂN NỐI, THƯ VIỆN CHÍNH THỨC VÀ CODE C++
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
          { from: "VCC", to: "3.3V / 5V (ESP32)", note: "Nguồn nuôi mạch cảm biến điện hóa" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" },
          { from: "SDA (Data)", to: "GPIO 21 (D21)", note: "Chân I2C Data phần cứng ESP32" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22)", note: "Chân I2C Clock phần cứng ESP32" }
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
          { from: "VCC", to: "5.0V (Sau LM2596)", note: "Cấp dòng lò nung sấy nhiệt ~150mA" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung toàn mạch" },
          { from: "A0 (Analog)", to: "GPIO 35", note: "Khối ADC1 Input Only độc lập" }
        ],
        codeSnippet: `// Cấu hình thư viện MQUnifiedsensor cho MQ-7\n#include <MQUnifiedsensor.h>\n#define Board "ESP-32"\n#define Pin 35 // ADC1 GPIO 35\n#define Type "MQ-7"\n#define Voltage_Resolution 3.3\n#define ADC_Bit_Resolution 12\nMQUnifiedsensor MQ7(Board, Voltage_Resolution, ADC_Bit_Resolution, Pin, Type);\n\nvoid setup() {\n  MQ7.init();\n  MQ7.setRegressionMethod(1); // PPM = a*ratio^b\n  MQ7.setA(99.042); MQ7.setB(-1.518); // Hệ số chuẩn khí CO\n}\nfloat readCO() {\n  MQ7.update();\n  return MQ7.readSensor();\n}`,
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
          { from: "VCC", to: "5.0V (Sau LM2596)", note: "Cấp lò nung sấy nhiệt" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" },
          { from: "A0 (Analog)", to: "GPIO 34", note: "Khối ADC1 Input Only độc lập" }
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
          { from: "VCC (Chân 1)", to: "3.3V / 5V (ESP32)", note: "Nguồn nuôi cảm biến" },
          { from: "DATA (Chân 2)", to: "GPIO 4 (D4)", note: "Chân 1-Wire số giao tiếp xung" },
          { from: "NC (Chân 3)", to: "Bỏ trống", note: "Không kết nối" },
          { from: "GND (Chân 4)", to: "GND Chung", note: "Chân mass chung" }
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
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Slave)", note: "Cổng nhận nối tiếp UART2" },
          { from: "GPIO 17 (TX2)", to: "DI (MAX485 Slave)", note: "Bắn chuỗi JSON dữ liệu lên mặt đất" },
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
          { from: "RO / DI", to: "GPIO 16 / GPIO 17", note: "Cổng nối tiếp UART2" },
          { from: "RE & DE", to: "3.3V (Kéo HIGH)", note: "Cố định chế độ truyền TRANSMIT" },
          { from: "Chân A (+)", to: "Dây Xanh Dương Cáp Mạng", note: "Tín hiệu vi sai dương RS485" },
          { from: "Chân B (-)", to: "Dây Trắng - Xanh Dương", note: "Tín hiệu vi sai âm RS485" }
        ],
        codeSnippet: `// Cấu hình cổng Serial2 phần cứng cho MAX485\nvoid setup() {\n  // Baudrate 9600, 8-bit data, không parity, 1 stop bit\n  // RX2 = GPIO 16, TX2 = GPIO 17\n  Serial2.begin(9600, SERIAL_8N1, 16, 17);\n}`,
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
          { from: "Cụm 3 Dây Dương (+)", to: "Cam, Trắng-Cam, Trắng-Nâu", note: "Tăng tiết diện S gấp 3, giảm điện trở R 3 lần" },
          { from: "Cụm 3 Dây Mass (GND)", to: "Nâu, Xanh Lá, Trắng-Xanh Lá", note: "Đường hồi tiếp dòng điện nung lớn" },
          { from: "Cụm 2 Dây Tín Hiệu", to: "Xanh Dương (A) & Trắng-Xanh (B)", note: "Cặp xoắn chống nhiễu vi sai RS485" }
        ],
        codeSnippet: `// Định luật Ohm & Điện trở dây (Vật lý 9):\n// R = rho * (l / S)\n// 1 sợi: S = 0.2 mm2 => R_day = 3.5 Ohm => Delta_U = I * R = 0.4A * 3.5 = 1.4V!\n// Chập 3 sợi: S_moi = 3 * S => R_moi = R / 3 = 1.16 Ohm => Delta_U = 0.46V\n// Bù áp: V_nguon = 5.2V => V_day = 5.2V - 0.2V = 5.0V (Chuẩn tuyệt đối!)`,
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
          { from: "RO", to: "GPIO 16 (RX2 Master)", note: "Đưa chuỗi JSON vào ESP32 Master" },
          { from: "RE & DE", to: "GND (Kéo LOW)", note: "Cố định chế độ nhận RECEIVE" }
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
          { from: "IN+ / IN-", to: "Pin Lithium 7.4V - 12V", note: "Điện áp nguồn pin tại chỗ trên mặt đất" },
          { from: "OUT+ (5.2V)", to: "Cụm 3 Dây Dương Cáp Cat5e", note: "Chỉnh chiết áp bù 0.2V sụt áp đường dài" },
          { from: "OUT- (GND)", to: "Cụm 3 Dây Mass Cáp Cat5e", note: "Cực âm chung toàn hệ thống" }
        ],
        codeSnippet: `// Hiệu suất chuyển đổi BUCK xung:\n// P_in = U_in * I_in\n// P_out = U_out * I_out\n// H = P_out / P_in > 90% (Mạch luôn mát, tiết kiệm ắc quy gấp đôi LM7805)`,
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
          { from: "GPIO 21 & 22", to: "OLED SSD1306 (SDA & SCL)", note: "I2C Hiển thị số đo" },
          { from: "GPIO 23", to: "Còi Hú Báo Động (Buzzer)", note: "Bức tường âm thanh ngăn nhảy cứu" },
          { from: "GPIO 19", to: "LED ĐỎ (Nguy hiểm)", note: "Trở hạn dòng 220 Ohm" },
          { from: "GPIO 5", to: "LED VÀNG (Cảnh báo)", note: "Trở hạn dòng 220 Ohm" },
          { from: "GPIO 18", to: "LED XANH (An toàn)", note: "Trở hạn dòng 220 Ohm" }
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
          { from: "VCC / GND", to: "3.3V / 5V & GND", note: "Nguồn nuôi màn hình" },
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

    // DANH SÁCH CÁC ĐƯỜNG DÂY NỐI CỤ THỂ TỪNG CHÂN (WIRING CONNECTIONS)
    const CONNECTIONS = [
      // 1. Cảm biến Oxy -> ESP32 Slave
      { from: "card-o2_sensor", to: "card-esp32_slave", fromX: 230, fromY: 100, toX: 0, toY: 50, color: "#38bdf8", stroke: 3, label: "I2C SDA (D21) & SCL (D22)" },
      // 2. MQ-7 -> ESP32 Slave
      { from: "card-mq7_sensor", to: "card-esp32_slave", fromX: 230, fromY: 100, toX: 0, toY: 120, color: "#f97316", stroke: 3, label: "Analog A0 -> GPIO 35 (ADC1)" },
      // 3. MQ-4 -> ESP32 Slave
      { from: "card-mq4_sensor", to: "card-esp32_slave", fromX: 230, fromY: 100, toX: 0, toY: 150, color: "#eab308", stroke: 3, label: "Analog A0 -> GPIO 34 (ADC1)" },
      // 4. DHT22 -> ESP32 Slave
      { from: "card-dht22_sensor", to: "card-esp32_slave", fromX: 230, fromY: 70, toX: 0, toY: 180, color: "#34d399", stroke: 3, label: "1-Wire DATA -> GPIO 4 (D4)" },
      // 5. ESP32 Slave -> MAX485 Slave
      { from: "card-esp32_slave", to: "card-max485_slave", fromX: 260, fromY: 120, toX: 0, toY: 50, color: "#a855f7", stroke: 3, label: "UART2 TX2(17) & RX2(16)" },

      // 6. CÁP MẠNG CAT5E (CỤM 3 - 3 - 2): LM2596 -> SLAVE & MAX485 -> MAX485
      // Cụm 3 Dây Dương (+5.2V)
      { from: "card-lm2596", to: "card-cable_cat5e", fromX: 0, fromY: 60, toX: 220, toY: 30, color: "#f97316", stroke: 5, label: "Cụm 3 Dây Dương (+5.2V)" },
      { from: "card-cable_cat5e", to: "card-esp32_slave", fromX: 0, fromY: 30, toX: 260, toY: 20, color: "#f97316", stroke: 5, label: "Cụm 3 Dây Dương (+5.2V)" },
      // Cụm 3 Dây Mass (GND)
      { from: "card-lm2596", to: "card-cable_cat5e", fromX: 0, fromY: 85, toX: 220, toY: 55, color: "#22c55e", stroke: 5, label: "Cụm 3 Dây Mass (GND)" },
      { from: "card-cable_cat5e", to: "card-esp32_slave", fromX: 0, fromY: 55, toX: 260, toY: 200, color: "#22c55e", stroke: 5, label: "Cụm 3 Dây Mass (GND)" },
      // Cặp vi sai RS-485 (Xanh Dương)
      { from: "card-max485_slave", to: "card-cable_cat5e", fromX: 230, fromY: 50, toX: 0, toY: 80, color: "#06b6d4", stroke: 4, label: "RS-485 Vi Sai (A/B)" },
      { from: "card-cable_cat5e", to: "card-max485_master", fromX: 220, fromY: 80, toX: 0, toY: 50, color: "#06b6d4", stroke: 4, label: "RS-485 Vi Sai (A/B)" },

      // 7. MAX485 Master -> ESP32 Master
      { from: "card-max485_master", to: "card-esp32_master", fromX: 220, fromY: 50, toX: 0, toY: 80, color: "#a855f7", stroke: 3, label: "RO -> GPIO 16 (RX2 Master)" },
      // 8. ESP32 Master -> OLED SSD1306
      { from: "card-esp32_master", to: "card-oled_display", fromX: 260, fromY: 50, toX: 0, toY: 80, color: "#38bdf8", stroke: 3, label: "I2C SDA(21) & SCL(22)" },
      // 9. ESP32 Master -> Còi & 3 LED
      { from: "card-esp32_master", to: "card-alarm_system", fromX: 260, fromY: 150, toX: 0, toY: 60, color: "#ef4444", stroke: 4, label: "GPIO 23 (Còi) & GPIO 19,5,18 (LED)" }
    ];

    // HỆ THỐNG VẼ ĐƯỜNG DÂY VECTOR SVG VÀ HẠT DÒNG ĐIỆN
    const wireGroup = document.getElementById("wire-group");
    const particlesGroup = document.getElementById("particles-group");
    const activePaths = [];

    function renderWiringPaths() {
      wireGroup.innerHTML = "";
      particlesGroup.innerHTML = "";
      activePaths.length = 0;

      CONNECTIONS.forEach((conn, index) => {
        const fromEl = document.getElementById(conn.from);
        const toEl = document.getElementById(conn.to);
        if (!fromEl || !toEl) return;

        const x1 = fromEl.offsetLeft + conn.fromX;
        const y1 = fromEl.offsetTop + conn.fromY;
        const x2 = toEl.offsetLeft + conn.toX;
        const y2 = toEl.offsetTop + conn.toY;

        // Vẽ đường cong Bezier mềm mại
        const dx = Math.abs(x2 - x1) * 0.55;
        const cp1x = x1 + dx;
        const cp1y = y1;
        const cp2x = x2 - dx;
        const cp2y = y2;
        const d = `M ${x1} ${y1} C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${x2} ${y2}`;

        // Đường dây chính
        const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", d);
        path.setAttribute("fill", "none");
        path.setAttribute("stroke", conn.color);
        path.setAttribute("stroke-width", conn.stroke);
        path.setAttribute("stroke-linecap", "round");
        path.setAttribute("opacity", "0.85");
        path.id = `wire-${index}`;
        wireGroup.appendChild(path);

        // Tạo 4 hạt electron phát sáng trên mỗi đường dây
        const particles = [];
        for (let p = 0; p < 4; p++) {
          const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          circle.setAttribute("r", (conn.stroke >= 4 ? 4.5 : 3.5));
          circle.setAttribute("fill", "#ffffff");
          circle.setAttribute("filter", "url(#glow-cyan)");
          circle.style.display = "none";
          particlesGroup.appendChild(circle);
          particles.push({ circle, progress: p * 0.25 });
        }

        activePaths.push({
          path,
          totalLength: path.getTotalLength(),
          particles,
          conn
        });
      });
    }

    // LOGIC PAN & ZOOM KHÔNG GIAN BÀN LÀM VIỆC
    const stage = document.getElementById("pan-zoom-stage");
    const container = document.getElementById("workspace-container");
    let scale = 0.85;
    let panX = -120;
    let panY = -30;
    let isDragging = false;
    let startX = 0, startY = 0;

    function updateTransform() {
      stage.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
    }

    container.addEventListener("mousedown", (e) => {
      if (e.target.closest(".comp-card") || e.target.closest("button") || e.target.closest(".sidebar-left") || e.target.closest(".sidebar-right")) return;
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
      const newScale = Math.min(Math.max(scale * zoomFactor, 0.45), 1.8);
      scale = newScale;
      updateTransform();
    }, { passive: false });

    document.getElementById("btn-reset-view").onclick = () => {
      scale = 0.85; panX = -120; panY = -30;
      updateTransform();
    };

    // RENDER SIDEBAR TRÁI VÀ CHỌN THIẾT BỊ
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
      const comp = COMPONENTS.find(c => c.id === compId);
      if (!comp) return;

      // Active sidebar list & active component card
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

      // Nổi bật đường dây nối liên quan
      activePaths.forEach(ap => {
        if (ap.conn.from === `card-${comp.id}` || ap.conn.to === `card-${comp.id}`) {
          ap.path.setAttribute("stroke-width", "6");
          ap.path.setAttribute("opacity", "1");
        } else {
          ap.path.setAttribute("stroke-width", ap.conn.stroke);
          ap.path.setAttribute("opacity", "0.35");
        }
      });

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
        activePaths.forEach(ap => ap.particles.forEach(p => p.circle.style.display = "block"));
      } else {
        btnPower.classList.remove("active");
        powerText.textContent = "BẬT NGUỒN PIN (5.2V)";
        flowDot.classList.remove("active");
        flowStatusText.textContent = "Nguồn đang tắt (Chưa có dòng điện)";
        flowDesc.textContent = "Bấm 'BẬT NGUỒN PIN' để kích hoạt dòng điện và truyền nhận RS485";
        activePaths.forEach(ap => ap.particles.forEach(p => p.circle.style.display = "none"));
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
        activePaths.forEach(ap => {
          ap.particles.forEach(p => {
            p.progress = (p.progress + dt * 0.45) % 1.0;
            const pt = ap.path.getPointAtLength(p.progress * ap.totalLength);
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
      renderWiringPaths();
      updateTransform();
      selectComponent("o2_sensor");
      requestAnimationFrame(animate);
    });

    window.addEventListener("resize", () => {
      renderWiringPaths();
    });
  </script>
</body>
</html>
'''

output_path = r"c:\Users\Admin\Downloads\All-Project\canhbaokhi\mo_phong_3d_noi_day\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Successfully generated Ultimate Photorealistic Hardware Wiring Studio at: {output_path}")
