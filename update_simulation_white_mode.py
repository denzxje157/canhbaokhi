import os

html_code = r'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sơ Đồ Đi Dây Kỹ Thuật - Hệ Thống Cảnh Báo Sớm Khí Độc</title>
  <!-- Wokwi Elements Official Web Components -->
  <script src="wokwi-elements.bundle.js"></script>
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      /* CHẾ ĐỘ SÁNG (MẶC ĐỊNH - BẢN VẼ KỸ THUẬT SẠCH SẼ, ĐỠ AI) */
      --bg: #f8fafc;
      --grid-dot: rgba(100, 116, 139, 0.22);
      --mat-bg: rgba(255, 255, 255, 0.95);
      --mat-border: #cbd5e1;
      --mat-shadow: 0 12px 32px rgba(0, 0, 0, 0.06);
      --card-bg: #ffffff;
      --card-border: #cbd5e1;
      --card-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
      --text: #0f172a;
      --text-muted: #64748b;
      --panel-bg: rgba(255, 255, 255, 0.97);
      --panel-border: #cbd5e1;
      --row-bg: #f1f5f9;
      --row-border: #e2e8f0;
      --bus-vcc-bg: #fee2e2;
      --bus-vcc-border: #dc2626;
      --bus-vcc-text: #991b1b;
      --bus-gnd-bg: #dcfce7;
      --bus-gnd-border: #16a34a;
      --bus-gnd-text: #166534;
      --btn-bg: #ffffff;
      --btn-border: #cbd5e1;
      --btn-text: #1e293b;
      
      /* MÀU DÂY KỸ THUẬT TIÊU CHUẨN */
      --w-vcc: #dc2626;
      --w-gnd: #16a34a;
      --w-i2c-sda: #2563eb;
      --w-i2c-scl: #0284c7;
      --w-mq7: #ea580c;
      --w-mq4: #d97706;
      --w-dht: #9333ea;
      --w-rs485-a: #0284c7;
      --w-rs485-b: #1d4ed8;
      --w-uart: #7c3aed;
      --w-buzz: #dc2626;
      --w-led-r: #dc2626;
      --w-led-y: #d97706;
      --w-led-g: #16a34a;
    }

    /* CHẾ ĐỘ TỐI (DARK TECH) */
    body.dark-mode {
      --bg: #070b14;
      --grid-dot: rgba(56, 189, 248, 0.12);
      --mat-bg: rgba(15, 23, 42, 0.88);
      --mat-border: rgba(56, 189, 248, 0.25);
      --mat-shadow: 0 20px 50px rgba(0, 0, 0, 0.65);
      --card-bg: rgba(18, 26, 44, 0.95);
      --card-border: rgba(56, 189, 248, 0.22);
      --card-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --panel-bg: rgba(15, 23, 42, 0.95);
      --panel-border: rgba(56, 189, 248, 0.28);
      --row-bg: rgba(30, 41, 59, 0.6);
      --row-border: rgba(51, 65, 85, 0.5);
      --bus-vcc-bg: rgba(239, 68, 68, 0.2);
      --bus-vcc-border: #ef4444;
      --bus-vcc-text: #fca5a5;
      --bus-gnd-bg: rgba(34, 197, 94, 0.2);
      --bus-gnd-border: #22c55e;
      --bus-gnd-text: #86efac;
      --btn-bg: rgba(30, 41, 59, 0.85);
      --btn-border: #475569;
      --btn-text: #f8fafc;
      
      --w-vcc: #ff3838;
      --w-gnd: #2ed573;
      --w-i2c-sda: #00f2fe;
      --w-i2c-scl: #38bdf8;
      --w-mq7: #ff9f1a;
      --w-mq4: #ffc048;
      --w-dht: #c56cf0;
      --w-rs485-a: #00f2fe;
      --w-rs485-b: #38bdf8;
      --w-uart: #c56cf0;
      --w-buzz: #ff3838;
      --w-led-r: #ff3838;
      --w-led-y: #ffc048;
      --w-led-g: #2ed573;
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
      transition: background 0.25s, color 0.25s;
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
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      backdrop-filter: blur(18px);
      padding: 10px 22px;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
      pointer-events: auto;
    }

    .header-title h1 {
      font-size: 1.12rem;
      font-weight: 800;
      color: #0284c7;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    body.dark-mode .header-title h1 {
      color: #38bdf8;
    }

    .header-title p {
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-top: 3px;
    }

    .header-actions {
      display: flex;
      gap: 10px;
      pointer-events: auto;
    }

    /* BUTTONS */
    .btn {
      background: var(--btn-bg);
      border: 1px solid var(--btn-border);
      color: var(--btn-text);
      padding: 9px 15px;
      border-radius: 9px;
      font-size: 0.83rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      backdrop-filter: blur(12px);
      transition: all 0.2s ease;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .btn:hover {
      border-color: #0284c7;
      transform: translateY(-1.5px);
    }

    .btn-theme {
      background: #0284c7;
      color: #ffffff;
      border-color: #0369a1;
      font-weight: 700;
    }
    .btn-theme:hover {
      background: #0369a1;
    }

    .btn-power {
      background: #e2e8f0;
      border-color: #cbd5e1;
      color: #334155;
    }
    body.dark-mode .btn-power {
      background: #1e293b;
      border-color: #475569;
      color: #f8fafc;
    }

    .btn-power.active {
      background: #16a34a !important;
      border-color: #15803d !important;
      color: #fff !important;
      box-shadow: 0 0 16px rgba(22, 163, 74, 0.45);
    }

    /* FILTER BAR */
    .filter-bar {
      position: absolute;
      top: 85px;
      left: 320px;
      z-index: 45;
      display: flex;
      gap: 6px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      padding: 6px 12px;
      border-radius: 10px;
      backdrop-filter: blur(14px);
      box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    }

    .filter-btn {
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      padding: 5px 11px;
      border-radius: 7px;
      font-size: 0.74rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.18s;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .filter-btn:hover {
      background: #e2e8f0;
      color: #0f172a;
    }
    body.dark-mode .filter-btn:hover {
      background: #334155;
      color: #f8fafc;
    }

    .filter-btn.active {
      background: #0284c7;
      color: #fff;
      border-color: #0369a1;
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
        radial-gradient(circle at 50% 50%, var(--bg) 0%, var(--bg) 100%),
        radial-gradient(var(--grid-dot) 1.5px, transparent 1.5px);
      background-size: 100% 100%, 28px 28px;
    }

    #workspace-container:active {
      cursor: grabbing;
    }

    #pan-zoom-stage {
      position: absolute;
      top: 0;
      left: 0;
      width: 2900px;
      height: 1800px;
      transform-origin: 0 0;
      transition: none; /* KHÔNG DÙNG CSS TRANSITION ĐỂ TRÁNH NHẢY GIẬT */
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
      border-radius: 16px;
      border: 2px solid var(--mat-border);
      background: var(--mat-bg);
      backdrop-filter: blur(12px);
      box-shadow: var(--mat-shadow);
      z-index: 2;
    }

    .bench-mat-title {
      position: absolute;
      top: 16px;
      left: 22px;
      font-size: 0.95rem;
      font-weight: 800;
      color: #0369a1;
      letter-spacing: 0.5px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    body.dark-mode .bench-mat-title {
      color: #38bdf8;
    }

    .bench-mat-badge {
      font-size: 0.72rem;
      padding: 3px 9px;
      border-radius: 5px;
      background: #e0f2fe;
      border: 1px solid #7dd3fc;
      color: #0284c7;
      font-weight: 700;
    }
    body.dark-mode .bench-mat-badge {
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.35);
      color: #7dd3fc;
    }

    /* ELECTRONIC MODULE CARDS */
    .comp-card {
      position: absolute;
      background: var(--card-bg);
      border: 1.5px solid var(--card-border);
      border-radius: 14px;
      padding: 14px 16px;
      box-shadow: var(--card-shadow);
      cursor: pointer;
      transition: border-color 0.18s, box-shadow 0.18s, transform 0.18s;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .comp-card:hover {
      border-color: #0284c7;
      box-shadow: 0 8px 24px rgba(2, 132, 199, 0.18);
      transform: translateY(-2px);
    }

    .comp-card.active {
      border-color: var(--active-color, #0284c7) !important;
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.25), 0 10px 28px rgba(0,0,0,0.12) !important;
    }

    .comp-card-hdr {
      font-size: 0.84rem;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 8px;
      text-align: center;
      display: flex;
      align-items: center;
      gap: 7px;
    }

    .comp-card-repo {
      font-size: 0.68rem;
      color: #0284c7;
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      padding: 3px 8px;
      border-radius: 5px;
      margin-top: 6px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-weight: 600;
      transition: all 0.15s;
    }
    body.dark-mode .comp-card-repo {
      background: rgba(56, 189, 248, 0.12);
      border-color: rgba(56, 189, 248, 0.25);
      color: #38bdf8;
    }
    .comp-card-repo:hover {
      background: #0284c7;
      color: #fff;
    }

    .real-photo-box {
      width: 140px;
      height: 140px;
      border-radius: 9px;
      overflow: hidden;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    body.dark-mode .real-photo-box {
      background: #020617;
      border-color: #1e293b;
    }

    .real-photo-box img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }

    /* CONNECTION TERMINAL PORTS (KHÔNG BỊ CHE KHUẤT, RÕ RÀNG) */
    .terminal-header {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px solid var(--row-border);
    }

    .terminal-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.72rem;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      padding: 5px 8px;
      background: var(--row-bg);
      border-radius: 6px;
      border: 1px solid var(--row-border);
      gap: 8px;
      position: relative;
    }

    .terminal-row span:not(.port-dot) {
      white-space: nowrap;
      font-weight: 600;
      color: var(--text);
    }

    .port-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #94a3b8;
      border: 2px solid #ffffff;
      display: inline-block;
      box-shadow: 0 1px 4px rgba(0,0,0,0.25);
      transition: transform 0.2s, box-shadow 0.2s;
      flex-shrink: 0;
    }

    .comp-card.active .port-dot {
      transform: scale(1.35);
      box-shadow: 0 0 0 2px #0284c7;
    }

    .port-dot.p-red { background: #dc2626; }
    .port-dot.p-green { background: #16a34a; }
    .port-dot.p-blue { background: #2563eb; }
    .port-dot.p-cyan { background: #0284c7; }
    .port-dot.p-orange { background: #ea580c; }
    .port-dot.p-amber { background: #d97706; }
    .port-dot.p-purple { background: #9333ea; }

    /* INDUSTRIAL POWER RAILS (MÁNG NGUỒN KÉP VCC & MASS GND) */
    .bus-rail-column {
      position: absolute;
      top: 60px;
      bottom: 40px;
      width: 46px;
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 12px 0;
      z-index: 4;
    }

    .bus-rail-vcc {
      left: 325px;
      background: var(--bus-vcc-bg);
      border: 2px solid var(--bus-vcc-border);
    }

    .bus-rail-gnd {
      left: 390px;
      background: var(--bus-gnd-bg);
      border: 2px solid var(--bus-gnd-border);
    }

    .bus-rail-label {
      writing-mode: vertical-rl;
      text-orientation: mixed;
      transform: rotate(180deg);
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 2px;
      font-family: monospace;
      padding: 8px 0;
    }

    .bus-rail-vcc .bus-rail-label { color: var(--bus-vcc-text); }
    .bus-rail-gnd .bus-rail-label { color: var(--bus-gnd-text); }

    .bus-tap-dot {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      border: 2px solid #fff;
      margin: 4px 0;
      box-shadow: 0 1px 4px rgba(0,0,0,0.3);
    }

    /* SIDEBARS */
    .sidebar-left {
      position: absolute;
      top: 85px;
      left: 20px;
      bottom: 25px;
      width: 285px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 14px;
      backdrop-filter: blur(16px);
      z-index: 50;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      overflow: hidden;
    }

    .sidebar-right {
      position: absolute;
      top: 85px;
      right: 20px;
      bottom: 25px;
      width: 440px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 14px;
      backdrop-filter: blur(16px);
      z-index: 50;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      overflow: hidden;
    }

    .panel-hdr {
      padding: 13px 16px;
      border-bottom: 1px solid var(--panel-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 800;
      font-size: 0.86rem;
      color: #0284c7;
      background: var(--row-bg);
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
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin: 10px 6px 4px 6px;
    }

    .comp-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 10px;
      border-radius: 8px;
      background: var(--row-bg);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.18s ease;
    }

    .comp-item:hover {
      border-color: #0284c7;
      background: #e2e8f0;
    }
    body.dark-mode .comp-item:hover {
      background: #334155;
    }

    .comp-item.active {
      background: #e0f2fe;
      border-color: #0284c7;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.18);
    }
    body.dark-mode .comp-item.active {
      background: rgba(56, 189, 248, 0.2);
    }

    .comp-icon {
      width: 32px;
      height: 32px;
      border-radius: 7px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      flex-shrink: 0;
      background: #f1f5f9;
      color: #0284c7;
      border: 1px solid #cbd5e1;
    }

    .comp-info { flex: 1; min-width: 0; }
    .comp-name { font-size: 0.8rem; font-weight: 700; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .comp-sub { font-size: 0.7rem; color: var(--text-muted); margin-top: 1px; }

    /* DETAIL PANEL */
    .detail-body {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
    }

    .comp-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 14px;
      font-size: 0.74rem;
      font-weight: 700;
      background: #e0f2fe;
      color: #0284c7;
      border: 1px solid #7dd3fc;
      margin-bottom: 8px;
    }

    .comp-title-large {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text);
      margin-bottom: 4px;
    }

    .repo-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 0.76rem;
      color: #0284c7;
      text-decoration: none;
      margin: 8px 0 12px 0;
      font-weight: 600;
      transition: all 0.18s;
    }
    body.dark-mode .repo-pill {
      background: #1e293b;
      border-color: #334155;
      color: #38bdf8;
    }
    .repo-pill:hover {
      background: #0284c7;
      color: #fff;
    }

    .pin-mapping-box {
      margin-top: 10px;
      background: var(--row-bg);
      border: 1px solid var(--row-border);
      border-radius: 10px;
      padding: 12px;
    }

    .pin-mapping-box h4 {
      font-size: 0.82rem;
      color: #0284c7;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 700;
    }

    .pin-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 0;
      border-bottom: 1px dashed var(--row-border);
      font-size: 0.8rem;
    }
    .pin-row:last-child { border-bottom: none; }

    .pin-from { color: var(--text); font-weight: 700; display: flex; align-items: center; gap: 6px; }
    .pin-arrow { color: var(--text-muted); font-size: 0.72rem; }
    .pin-to {
      color: #0284c7;
      font-family: ui-monospace, SFMono-Regular, monospace;
      font-weight: 700;
      background: #e0f2fe;
      padding: 2px 8px;
      border-radius: 4px;
      border: 1px solid #7dd3fc;
    }
    body.dark-mode .pin-to {
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.35);
      color: #38bdf8;
    }

    .code-snippet-box {
      margin-top: 12px;
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 9px;
      padding: 10px 12px;
      font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
      font-size: 0.74rem;
      color: #38bdf8;
      overflow-x: auto;
      line-height: 1.45;
    }

    .explanation-card {
      margin-top: 14px;
      background: var(--row-bg);
      border: 1px solid var(--row-border);
      border-radius: 10px;
      padding: 12px 14px;
    }

    .explanation-card h4 {
      font-size: 0.84rem;
      color: #d97706;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 800;
    }

    .explanation-card p {
      font-size: 0.8rem;
      line-height: 1.5;
      color: var(--text);
    }

    .highlight-tip {
      margin-top: 10px;
      padding: 8px 10px;
      border-radius: 6px;
      background: #fef3c7;
      border-left: 3px solid #d97706;
      font-size: 0.76rem;
      color: #92400e;
      line-height: 1.4;
    }
    body.dark-mode .highlight-tip {
      background: rgba(245, 158, 11, 0.12);
      color: #fde68a;
    }

    .physicsTip {
      margin-top: 10px;
      padding: 8px 10px;
      border-radius: 6px;
      background: #dcfce7;
      border-left: 3px solid #16a34a;
      font-size: 0.76rem;
      color: #166534;
      line-height: 1.4;
    }
    body.dark-mode .physicsTip {
      background: rgba(16, 185, 129, 0.12);
      color: #a7f3d0;
    }

    /* BOTTOM BAR */
    .bottom-bar {
      position: absolute;
      bottom: 25px;
      left: 320px;
      right: 480px;
      height: 56px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      backdrop-filter: blur(16px);
      z-index: 50;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }

    .flow-status { display: flex; align-items: center; gap: 12px; }
    .status-dot { width: 11px; height: 11px; border-radius: 50%; background: #94a3b8; }
    .status-dot.active { background: #16a34a; box-shadow: 0 0 10px rgba(22, 163, 74, 0.7); }

    .sim-levels { display: flex; gap: 8px; }
    .btn-level {
      padding: 6px 12px;
      font-size: 0.78rem;
      border-radius: 7px;
      border: 1px solid var(--btn-border);
      background: var(--btn-bg);
      color: var(--text);
      cursor: pointer;
      font-weight: 700;
      transition: all 0.15s;
    }

    .btn-level.active-safe { background: #16a34a; border-color: #15803d; color: #fff; }
    .btn-level.active-warn { background: #d97706; border-color: #b45309; color: #fff; }
    .btn-level.active-dang { background: #dc2626; border-color: #b91c1c; color: #fff; }
  </style>
</head>
<body class="light-mode">

  <!-- TOP HEADER -->
  <header>
    <div class="header-title">
      <h1><i class="fa-solid fa-microchip"></i> SƠ ĐỒ ĐI DÂY KỸ THUẬT (CHUẨN BẢN VẼ ĐỒ ÁN)</h1>
      <p>Hệ Thống Cảnh Báo Sớm Khí Độc & Thiếu Oxygen (Đã Khắc Phục Lỗi Nhảy Màn Hình & Trùng Dây)</p>
    </div>
    <div class="header-actions">
      <!-- NÚT CHUYỂN ĐỔI CHẾ ĐỘ SÁNG / TỐI -->
      <button class="btn btn-theme" id="btn-theme-toggle">
        <i class="fa-solid fa-sun"></i> <span id="theme-text">Giao Diện: Sáng (Kỹ Thuật)</span>
      </button>
      <button class="btn btn-power" id="btn-power">
        <i class="fa-solid fa-power-off"></i> <span id="power-text">BẬT NGUỒN PIN (5.2V)</span>
      </button>
      <button class="btn" id="btn-toggle-isolate">
        <i class="fa-solid fa-eye-slash"></i> <span id="isolate-text">Làm Mờ Dây Khác: BẬT</span>
      </button>
      <button class="btn" id="btn-reset-view">
        <i class="fa-solid fa-arrows-rotate"></i> Reset Vị Trí
      </button>
    </div>
  </header>

  <!-- BỘ LỌC TỪNG CỤM DÂY NHANH -->
  <div class="filter-bar">
    <span style="font-size: 0.74rem; color: var(--text-muted); display: flex; align-items: center; gap: 4px; margin-right: 4px;">
      <i class="fa-solid fa-diagram-project"></i> Lọc Mạch:
    </span>
    <button class="filter-btn active" onclick="filterCircuit('all')">Tất Cả</button>
    <button class="filter-btn" onclick="filterCircuit('o2_sensor')"><span class="port-dot p-blue"></span> Oxy (I2C + Nguồn)</button>
    <button class="filter-btn" onclick="filterCircuit('mq7_sensor')"><span class="port-dot p-orange"></span> MQ-7 (CO)</button>
    <button class="filter-btn" onclick="filterCircuit('mq4_sensor')"><span class="port-dot p-amber"></span> MQ-4 (Metan)</button>
    <button class="filter-btn" onclick="filterCircuit('dht22_sensor')"><span class="port-dot p-purple"></span> DHT22 (Nhiệt/Ẩm)</button>
    <button class="filter-btn" onclick="filterCircuit('cable_cat5e')"><span class="port-dot p-orange"></span> Cáp Cat5e 3-3-2</button>
    <button class="filter-btn" onclick="filterCircuit('alarm_system')"><span class="port-dot p-red"></span> Còi & LED</button>
  </div>

  <!-- SIDEBAR TRÁI: DANH SÁCH THIẾT BỊ -->
  <div class="sidebar-left">
    <div class="panel-hdr">
      <span><i class="fa-solid fa-layer-group"></i> THIẾT BỊ HỆ THỐNG</span>
      <span style="font-size: 0.72rem; color: var(--text-muted);">11 Module</span>
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
        <g id="wire-group"></g>
        <g id="particles-group"></g>
      </svg>

      <!-- 1. BỆ ĐỠ KHỐI KHÔNG GIAN KÍN (SLAVE) - KHOẢNG CÁCH RỘNG RÃI 1620px -->
      <div class="bench-mat" style="left: 50px; top: 100px; width: 1100px; height: 1620px;">
        <div class="bench-mat-title">
          <i class="fa-solid fa-dungeon"></i> KHỐI DƯỚI ĐÁY KHÔNG GIAN KÍN (SLAVE)
          <span class="bench-mat-badge">Thu thập 5 thông số khí & Gom gói JSON</span>
        </div>

        <!-- MÁNG NGUỒN KÉP VCC 5V & MASS GND DỌC BẢN VẼ -->
        <div class="bus-rail-column bus-rail-vcc">
          <span class="bus-rail-label"><i class="fa-solid fa-bolt"></i> VCC 5V BUS RAIL</span>
          <div class="bus-tap-dot p-red" id="port-rail-vcc-o2" title="Cấp 5V cho Oxy"></div>
          <div class="bus-tap-dot p-red" id="port-rail-vcc-mq7" title="Cấp 5V nung MQ-7"></div>
          <div class="bus-tap-dot p-red" id="port-rail-vcc-mq4" title="Cấp 5V nung MQ-4"></div>
          <div class="bus-tap-dot p-red" id="port-rail-vcc-dht22" title="Cấp 5V cho DHT22"></div>
          <div class="bus-tap-dot p-red" id="port-rail-vcc-feed" title="Nhận 5.2V từ Cáp Cat5e"></div>
        </div>

        <div class="bus-rail-column bus-rail-gnd">
          <span class="bus-rail-label"><i class="fa-solid fa-shield"></i> GND MASS RAIL</span>
          <div class="bus-tap-dot p-green" id="port-rail-gnd-o2" title="Mass Oxy"></div>
          <div class="bus-tap-dot p-green" id="port-rail-gnd-mq7" title="Mass MQ-7"></div>
          <div class="bus-tap-dot p-green" id="port-rail-gnd-mq4" title="Mass MQ-4"></div>
          <div class="bus-tap-dot p-green" id="port-rail-gnd-dht22" title="Mass DHT22"></div>
          <div class="bus-tap-dot p-green" id="port-rail-gnd-feed" title="Mass chung Cáp Cat5e"></div>
        </div>

        <!-- CẢM BIẾN OXY DFROBOT (SEN0496 / SEN0322) - TOP: 70px -->
        <div class="comp-card" id="card-o2_sensor" style="left: 40px; top: 70px; width: 250px;" onclick="selectComponent('o2_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-lungs" style="color: #0284c7;"></i> Cảm Biến Oxy DFRobot</div>
          <div class="real-photo-box">
            <img src="images/sensor_o2.png" alt="DFRobot Gravity O2">
          </div>
          <a class="comp-card-repo" href="https://github.com/DFRobot/DFRobot_OxygenSensor" target="_blank"><i class="fa-brands fa-github"></i> DFRobot_OxygenSensor</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>SCL (Clock)</span><span class="port-dot p-cyan" id="port-o2-scl"></span></div>
            <div class="terminal-row"><span>SDA (Data)</span><span class="port-dot p-blue" id="port-o2-sda"></span></div>
            <div class="terminal-row"><span>VCC (Nguồn)</span><span class="port-dot p-red" id="port-o2-vcc"></span></div>
            <div class="terminal-row"><span>GND (Mass)</span><span class="port-dot p-green" id="port-o2-gnd"></span></div>
          </div>
        </div>

        <!-- CẢM BIẾN KHÍ CO MQ-7 - TOP: 450px (KHOẢNG CÁCH RỘNG RÃI) -->
        <div class="comp-card" id="card-mq7_sensor" style="left: 40px; top: 450px; width: 250px;" onclick="selectComponent('mq7_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-skull-crossbones" style="color: #ea580c;"></i> Khí Than CO (MQ-7)</div>
          <div class="real-photo-box">
            <img src="images/sensor_mq7.png" alt="Winsen MQ-7">
          </div>
          <a class="comp-card-repo" href="https://github.com/miguel5612/MQSensorsLib" target="_blank"><i class="fa-brands fa-github"></i> miguel5612/MQSensorsLib</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>A0 (Analog)</span><span class="port-dot p-orange" id="port-mq7-a0"></span></div>
            <div class="terminal-row"><span>VCC (5V Nung)</span><span class="port-dot p-red" id="port-mq7-vcc"></span></div>
            <div class="terminal-row"><span>GND (Mass Nung)</span><span class="port-dot p-green" id="port-mq7-gnd"></span></div>
          </div>
        </div>

        <!-- CẢM BIẾN KHÍ GAS/METAN MQ-4 - TOP: 830px (KHOẢNG CÁCH RỘNG RÃI) -->
        <div class="comp-card" id="card-mq4_sensor" style="left: 40px; top: 830px; width: 250px;" onclick="selectComponent('mq4_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-fire-flame-simple" style="color: #d97706;"></i> Khí Gas Metan (MQ-4)</div>
          <div class="real-photo-box">
            <img src="images/sensor_mq4.png" alt="Winsen MQ-4">
          </div>
          <a class="comp-card-repo" href="https://github.com/miguel5612/MQSensorsLib" target="_blank"><i class="fa-brands fa-github"></i> miguel5612/MQSensorsLib</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>A0 (Analog)</span><span class="port-dot p-amber" id="port-mq4-a0"></span></div>
            <div class="terminal-row"><span>VCC (5V Nung)</span><span class="port-dot p-red" id="port-mq4-vcc"></span></div>
            <div class="terminal-row"><span>GND (Mass Nung)</span><span class="port-dot p-green" id="port-mq4-gnd"></span></div>
          </div>
        </div>

        <!-- CẢM BIẾN NHIỆT ĐỘ - ĐỘ ẨM DHT22 - TOP: 1210px (KHOẢNG CÁCH RỘNG RÃI) -->
        <div class="comp-card" id="card-dht22_sensor" style="left: 40px; top: 1210px; width: 250px;" onclick="selectComponent('dht22_sensor')">
          <div class="comp-card-hdr"><i class="fa-solid fa-temperature-half" style="color: #9333ea;"></i> Nhiệt Ẩm DHT22</div>
          <div style="transform: scale(0.92); margin: -4px 0;">
            <wokwi-dht22></wokwi-dht22>
          </div>
          <a class="comp-card-repo" href="https://github.com/adafruit/DHT-sensor-library" target="_blank"><i class="fa-brands fa-github"></i> adafruit/DHT-sensor-library</a>
          <div class="terminal-header">
            <div class="terminal-row"><span>DATA (1-Wire)</span><span class="port-dot p-purple" id="port-dht22-data"></span></div>
            <div class="terminal-row"><span>VCC (3.3-5V)</span><span class="port-dot p-red" id="port-dht22-vcc"></span></div>
            <div class="terminal-row"><span>GND (Mass)</span><span class="port-dot p-green" id="port-dht22-gnd"></span></div>
          </div>
        </div>

        <!-- BO MẠCH VI ĐIỀU KHIỂN ESP32 SLAVE (CHÂN TRÁI NHẬN CẢM BIẾN, CHÂN PHẢI XUẤT MAX485) -->
        <div class="comp-card" id="card-esp32_slave" style="left: 460px; top: 520px; width: 300px;" onclick="selectComponent('esp32_slave')">
          <div class="comp-card-hdr"><i class="fa-solid fa-microchip" style="color: #16a34a;"></i> ESP32 SLAVE (DƯỚI ĐÁY)</div>
          <div style="transform: scale(0.96); margin: 6px 0;">
            <wokwi-esp32-devkit-v1></wokwi-esp32-devkit-v1>
          </div>
          <div style="font-size: 0.7rem; color: #0284c7; text-align: center; margin-top: 4px; font-weight: 700;">NodeMCU-32S Dual Core 240MHz</div>
          
          <div class="terminal-header">
            <!-- CHÂN ĐẦU VÀO BÊN TRÁI (TỪ CẢM BIẾN & MÁNG NGUỒN) -->
            <div class="terminal-row"><span class="port-dot p-blue" id="port-esp32s-d21"></span><span>GPIO 21 (I2C SDA Oxy)</span></div>
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-esp32s-d22"></span><span>GPIO 22 (I2C SCL Oxy)</span></div>
            <div class="terminal-row"><span class="port-dot p-orange" id="port-esp32s-gpio35"></span><span>GPIO 35 (ADC1 MQ-7)</span></div>
            <div class="terminal-row"><span class="port-dot p-amber" id="port-esp32s-gpio34"></span><span>GPIO 34 (ADC1 MQ-4)</span></div>
            <div class="terminal-row"><span class="port-dot p-purple" id="port-esp32s-d4"></span><span>GPIO 4 (1-Wire DHT22)</span></div>
            <div class="terminal-row"><span class="port-dot p-red" id="port-esp32s-vin"></span><span>VIN (+5.2V Nguồn Cáp)</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-esp32s-gnd"></span><span>GND (Mass Chung)</span></div>
            
            <!-- CHÂN ĐẦU RA BÊN PHẢI (SANG MAX485 - KHÔNG ĐÈ LÊN CHỮ) -->
            <div class="terminal-row"><span>UART2 TX2 (GPIO 17)</span><span class="port-dot p-purple" id="port-esp32s-tx2"></span></div>
            <div class="terminal-row"><span>UART2 RX2 (GPIO 16)</span><span class="port-dot p-purple" id="port-esp32s-rx2"></span></div>
            <div class="terminal-row"><span>5V Nuôi MAX485</span><span class="port-dot p-red" id="port-esp32s-vcc-out"></span></div>
            <div class="terminal-row"><span>GND Mass MAX485</span><span class="port-dot p-green" id="port-esp32s-gnd-out"></span></div>
          </div>
        </div>

        <!-- MODULE MAX485 SLAVE -->
        <div class="comp-card" id="card-max485_slave" style="left: 830px; top: 580px; width: 240px;" onclick="selectComponent('max485_slave')">
          <div class="comp-card-hdr"><i class="fa-solid fa-network-wired" style="color: #9333ea;"></i> MAX485 SLAVE (TX)</div>
          <div style="background: #0284c7; width: 160px; height: 95px; border-radius: 8px; border: 2px solid #0369a1; display: flex; flex-direction: column; justify-content: space-between; padding: 6px;">
            <div style="font-size: 0.72rem; font-weight: 800; color: #fff; text-align: center;">MAX485 TRANSMITTER</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div style="background: #1e293b; width: 55px; height: 35px; border-radius: 4px; border: 1px solid #475569; color: #e2e8f0; font-size: 0.62rem; display: flex; align-items: center; justify-content: center; font-family: monospace;">MAX485</div>
              <div style="background: #15803d; width: 45px; height: 42px; border-radius: 4px; border: 1px solid #22c55e; display: flex; flex-direction: column; justify-content: space-around; align-items: center; color: #fff; font-size: 0.65rem; font-weight: 800;">
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
            <div class="terminal-row"><span class="port-dot p-red" id="port-max485s-vcc"></span><span>VCC (5V)</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-max485s-gnd"></span><span>GND</span></div>
            <div class="terminal-row"><span>Chân A (Vi Sai +)</span><span class="port-dot p-cyan" id="port-max485s-a"></span></div>
            <div class="terminal-row"><span>Chân B (Vi Sai -)</span><span class="port-dot p-blue" id="port-max485s-b"></span></div>
          </div>
        </div>
      </div>

      <!-- 2. CỤM CÁP MẠNG CAT5E (CỤM 3 - 3 - 2) Ở CHÍNH GIỮA -->
      <div class="comp-card" id="card-cable_cat5e" style="left: 1200px; top: 620px; width: 260px;" onclick="selectComponent('cable_cat5e')">
        <div class="comp-card-hdr"><i class="fa-solid fa-ethernet" style="color: #ea580c;"></i> Cáp Cat5e (Cụm 3 - 3 - 2)</div>
        <div style="background: var(--row-bg); border: 1.5px solid var(--row-border); border-radius: 10px; width: 230px; padding: 12px; text-align: left; font-size: 0.72rem; line-height: 1.7;">
          <div style="color: #dc2626; font-weight: 800; display: flex; justify-content: space-between; align-items: center;">
            <span class="port-dot p-red" id="port-cat5-pwr-left"></span>
            <span>3 Dây Dương (+5.2V)</span>
            <span class="port-dot p-red" id="port-cat5-pwr-right"></span>
          </div>
          <div style="color: #16a34a; font-weight: 800; display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
            <span class="port-dot p-green" id="port-cat5-gnd-left"></span>
            <span>3 Dây Mass (GND)</span>
            <span class="port-dot p-green" id="port-cat5-gnd-right"></span>
          </div>
          <div style="color: #0284c7; font-weight: 800; display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
            <span class="port-dot p-cyan" id="port-cat5-rs485-left"></span>
            <span>2 Dây Vi Sai RS-485</span>
            <span class="port-dot p-cyan" id="port-cat5-rs485-right"></span>
          </div>
        </div>
        <div style="font-size: 0.68rem; color: #d97706; margin-top: 8px; text-align: center; font-weight: 700;">Vật lý 9: R = &rho;&middot;(l / S) &rarr; Tăng S gấp 3, giảm R 3 lần</div>
      </div>

      <!-- 3. BỆ ĐỠ KHỐI TRÊN MẶT ĐẤT (MASTER) -->
      <div class="bench-mat" style="left: 1510px; top: 100px; width: 1060px; height: 1620px;">
        <div class="bench-mat-title">
          <i class="fa-solid fa-tower-broadcast"></i> KHỐI TRÊN MẶT ĐẤT (MASTER)
          <span class="bench-mat-badge">Phân tích nồng độ, Phát Wi-Fi Web Server & Báo động</span>
        </div>

        <!-- NGUỒN XUNG HẠ ÁP LM2596 (5.2V) -->
        <div class="comp-card" id="card-lm2596" style="left: 40px; top: 220px; width: 240px;" onclick="selectComponent('lm2596')">
          <div class="comp-card-hdr"><i class="fa-solid fa-bolt" style="color: #0284c7;"></i> Nguồn Xung LM2596 (5.2V)</div>
          <div style="background: #0284c7; border: 2px solid #0369a1; border-radius: 8px; width: 150px; height: 100px; padding: 6px; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="font-size: 0.68rem; color: #fff; font-weight: 800; text-align: center;">DC-DC BUCK 5.2V</div>
            <div style="display: flex; justify-content: space-around; align-items: center;">
              <div style="background: #1e293b; width: 34px; height: 34px; border-radius: 50%; border: 2px solid #d97706; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #ff9f1a; font-weight: 700;">Cuộn</div>
              <div style="background: #2563eb; width: 25px; height: 35px; border-radius: 4px; border: 1px solid #ff9f1a; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #fff; font-weight: 700;">3296</div>
              <div style="background: #334155; width: 30px; height: 35px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.55rem; color: #fff; font-weight: 700;">Tụ</div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.62rem; color: #fff; font-weight: 800;">
              <span>PIN 7.4-12V</span><span>OUT 5.2V</span>
            </div>
          </div>
          <div class="terminal-header">
            <div class="terminal-row"><span>OUT+ (5.2V Cấp Cáp)</span><span class="port-dot p-red" id="port-lm2596-out-pos"></span></div>
            <div class="terminal-row"><span>OUT- (Mass GND)</span><span class="port-dot p-green" id="port-lm2596-out-neg"></span></div>
          </div>
        </div>

        <!-- MODULE MAX485 MASTER -->
        <div class="comp-card" id="card-max485_master" style="left: 40px; top: 620px; width: 240px;" onclick="selectComponent('max485_master')">
          <div class="comp-card-hdr"><i class="fa-solid fa-network-wired" style="color: #9333ea;"></i> MAX485 MASTER (RX)</div>
          <div style="background: #0284c7; width: 150px; height: 95px; border-radius: 8px; border: 2px solid #0369a1; display: flex; flex-direction: column; justify-content: space-between; padding: 6px;">
            <div style="font-size: 0.72rem; font-weight: 800; color: #fff; text-align: center;">MAX485 RECEIVER</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
              <div style="background: #15803d; width: 42px; height: 40px; border-radius: 4px; border: 1px solid #22c55e; display: flex; flex-direction: column; justify-content: space-around; align-items: center; color: #fff; font-size: 0.65rem; font-weight: 800;">
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
            <div class="terminal-row"><span class="port-dot p-blue" id="port-max485m-b"></span><span>Chân B (Từ Cáp)</span></div>
            <div class="terminal-row"><span>RO (Chuỗi JSON ra)</span><span class="port-dot p-purple" id="port-max485m-ro"></span></div>
            <div class="terminal-row"><span>VCC (5V)</span><span class="port-dot p-red" id="port-max485m-vcc"></span></div>
            <div class="terminal-row"><span>GND</span><span class="port-dot p-green" id="port-max485m-gnd"></span></div>
          </div>
        </div>

        <!-- BO MẠCH VI ĐIỀU KHIỂN ESP32 MASTER (CÁC CHÂN TÁCH BIỆT TRÁI - PHẢI, ZERO TRÙNG DÂY) -->
        <div class="comp-card" id="card-esp32_master" style="left: 360px; top: 520px; width: 300px;" onclick="selectComponent('esp32_master')">
          <div class="comp-card-hdr"><i class="fa-solid fa-microchip" style="color: #2563eb;"></i> ESP32 MASTER (MẶT ĐẤT)</div>
          <div style="transform: scale(0.96); margin: 6px 0;">
            <wokwi-esp32-devkit-v1></wokwi-esp32-devkit-v1>
          </div>
          <div style="font-size: 0.7rem; color: #2563eb; text-align: center; margin-top: 4px; font-weight: 700;">Web Server AP + Phân tích Logic</div>
          
          <div class="terminal-header">
            <!-- PHÍA TRÁI: NHẬN DỮ LIỆU VÀ NGUỒN TỪ MAX485 & LM2596 -->
            <div class="terminal-row"><span class="port-dot p-purple" id="port-esp32m-rx2"></span><span>GPIO 16 (RX2 Nhận JSON)</span></div>
            <div class="terminal-row"><span class="port-dot p-red" id="port-esp32m-vin-in"></span><span>VIN (5.2V Nguồn Vào)</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-esp32m-gnd-in"></span><span>GND (Mass Chung Vào)</span></div>

            <!-- PHÍA PHẢI: XUẤT RA OLED VÀ CÒI ĐÈN (ĐƯỜNG DÂY ĐI SANG PHẢI, TUYỆT ĐỐI KHÔNG ĐÈ LÊN CHỮ) -->
            <div class="terminal-row"><span>GPIO 21 (I2C SDA OLED)</span><span class="port-dot p-blue" id="port-esp32m-d21"></span></div>
            <div class="terminal-row"><span>GPIO 22 (I2C SCL OLED)</span><span class="port-dot p-cyan" id="port-esp32m-d22"></span></div>
            <div class="terminal-row"><span>3.3V Cấp OLED</span><span class="port-dot p-red" id="port-esp32m-3v3-out"></span></div>
            <div class="terminal-row"><span>GND Cấp OLED & Đèn</span><span class="port-dot p-green" id="port-esp32m-gnd-out"></span></div>
            <div class="terminal-row"><span>GPIO 23 (Còi Buzzer)</span><span class="port-dot p-red" id="port-esp32m-d23"></span></div>
            <div class="terminal-row"><span>GPIO 19 (LED ĐỎ)</span><span class="port-dot p-red" id="port-esp32m-d19"></span></div>
            <div class="terminal-row"><span>GPIO 5 (LED VÀNG)</span><span class="port-dot p-amber" id="port-esp32m-d5"></span></div>
            <div class="terminal-row"><span>GPIO 18 (LED XANH)</span><span class="port-dot p-green" id="port-esp32m-d18"></span></div>
          </div>
        </div>

        <!-- MÀN HÌNH OLED 0.96 INCH SSD1306 -->
        <div class="comp-card" id="card-oled_display" style="left: 730px; top: 240px; width: 250px;" onclick="selectComponent('oled_display')">
          <div class="comp-card-hdr"><i class="fa-solid fa-tv" style="color: #0284c7;"></i> Màn Hình OLED 0.96" SSD1306</div>
          <div style="transform: scale(0.92); margin: -4px 0;">
            <wokwi-ssd1306 id="wokwi-oled"></wokwi-ssd1306>
          </div>
          <div class="terminal-header">
            <div class="terminal-row"><span class="port-dot p-blue" id="port-oled-sda"></span><span>SDA (Data)</span></div>
            <div class="terminal-row"><span class="port-dot p-cyan" id="port-oled-scl"></span><span>SCL (Clock)</span></div>
            <div class="terminal-row"><span class="port-dot p-red" id="port-oled-vcc"></span><span>VCC (3.3V)</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-oled-gnd"></span><span>GND</span></div>
          </div>
        </div>

        <!-- CÒI BUZZER VÀ 3 ĐÈN LED BÁO ĐỘNG -->
        <div class="comp-card" id="card-alarm_system" style="left: 730px; top: 760px; width: 250px;" onclick="selectComponent('alarm_system')">
          <div class="comp-card-hdr"><i class="fa-solid fa-bullhorn" style="color: #dc2626;"></i> Còi Hú & 3 LED Cảnh Báo</div>
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
            <div class="terminal-row"><span class="port-dot p-amber" id="port-alarm-yel"></span><span>LED VÀNG (+) &larr; GPIO 5</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-alarm-grn"></span><span>LED XANH (+) &larr; GPIO 18</span></div>
            <div class="terminal-row"><span class="port-dot p-green" id="port-alarm-gnd"></span><span>GND (Mass Chung)</span></div>
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
        <div class="status-text" id="flow-status-text" style="font-weight: 700; font-size: 0.8rem;">Nguồn đang tắt (Chưa có dòng điện)</div>
        <div style="font-size: 0.7rem; color: var(--text-muted);" id="flow-desc">Bấm 'BẬT NGUỒN PIN' để dòng điện và xung tín hiệu RS485 chuyển động</div>
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
      <span style="font-size: 0.75rem; color: #0284c7; font-weight: 800;" id="detail-category">SLAVE</span>
    </div>
    <div class="detail-body" id="detail-body">
      <!-- Sẽ render động khi click linh kiện -->
    </div>
  </div>

  <!-- JAVASCRIPT ĐI DÂY KỸ THUẬT VÀ TƯƠNG TÁC -->
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
        color: "#0284c7",
        icon: "fa-lungs",
        pins: [
          { from: "SDA (Data)", to: "GPIO 21 (D21)", note: "Chân I2C Data phần cứng ESP32" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22)", note: "Chân I2C Clock phần cứng ESP32" },
          { from: "VCC (Nguồn)", to: "VCC 5V Power Rail", note: "Nối vào Bus 5V nguồn nuôi mạch điện hóa" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Nối vào Bus Mass chung hệ thống" }
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
        color: "#ea580c",
        icon: "fa-skull-crossbones",
        pins: [
          { from: "A0 (Analog)", to: "GPIO 35", note: "Khối ADC1 Input Only độc lập" },
          { from: "VCC (5V Nung)", to: "VCC 5V Power Rail", note: "Lấy dòng sấy nhiệt ~150mA từ Bus Nguồn 5V" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp dòng sấy lớn về Bus Mass" }
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
        color: "#d97706",
        icon: "fa-fire-flame-simple",
        pins: [
          { from: "A0 (Analog)", to: "GPIO 34", note: "Khối ADC1 Input Only độc lập" },
          { from: "VCC (5V Nung)", to: "VCC 5V Power Rail", note: "Lấy dòng lò nung sấy từ Bus Nguồn 5V" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Hồi tiếp dòng về Bus Mass" }
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
        color: "#9333ea",
        icon: "fa-temperature-half",
        pins: [
          { from: "DATA (1-Wire)", to: "GPIO 4 (D4)", note: "Chân 1-Wire số giao tiếp xung" },
          { from: "VCC (Nguồn)", to: "VCC 5V Power Rail", note: "Nguồn nuôi cảm biến" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Chân mass chung" }
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
        color: "#16a34a",
        icon: "fa-microchip",
        pins: [
          { from: "VIN (Nguồn)", to: "VCC 5V Power Rail", note: "Nhận điện từ LM2596 mặt đất cấp xuống" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp mass chung" },
          { from: "GPIO 17 (TX2)", to: "DI (MAX485 Slave)", note: "Bắn chuỗi JSON dữ liệu lên mặt đất" },
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Slave)", note: "Cổng nhận nối tiếp UART2" }
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
        color: "#9333ea",
        icon: "fa-network-wired",
        pins: [
          { from: "DI", to: "GPIO 17 (TX2)", note: "Nhận luồng dữ liệu từ ESP32" },
          { from: "RO", to: "GPIO 16 (RX2)", note: "Cổng nối tiếp UART2" },
          { from: "VCC & GND", to: "5V & GND Out (ESP32)", note: "Nguồn nuôi IC vi sai" },
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
        color: "#ea580c",
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
        color: "#9333ea",
        icon: "fa-network-wired",
        pins: [
          { from: "Chân A & B", to: "Nhận từ Cáp Cat5e", note: "Tín hiệu vi sai từ dưới đáy đưa lên" },
          { from: "RO", to: "GPIO 16 (RX2 Master)", note: "Đưa chuỗi JSON vào ESP32 Master" },
          { from: "VCC & GND", to: "5V & GND Nguồn", note: "Nguồn nuôi module" }
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
          { from: "OUT+ (5.2V)", to: "Cụm 3 Dây Dương Cáp Cat5e & VIN Master", note: "Chỉnh chiết áp bù 0.2V sụt áp đường dài" },
          { from: "OUT- (GND)", to: "Cụm 3 Dây Mass Cáp Cat5e & GND Master", note: "Cực âm chung toàn hệ thống" }
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
        color: "#2563eb",
        icon: "fa-microchip",
        pins: [
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Master)", note: "Nhận chuỗi dữ liệu JSON" },
          { from: "GPIO 21 & 22", to: "OLED SSD1306 (SDA & SCL)", note: "I2C Hiển thị số đo" },
          { from: "GPIO 23", to: "Còi Hú Báo Động (Buzzer)", note: "Bức tường âm thanh ngăn nhảy cứu" },
          { from: "GPIO 19, 5, 18", to: "LED Đỏ - Vàng - Xanh", note: "Báo động 3 cấp độ an toàn" },
          { from: "VIN & GND", to: "5.2V Nguồn & GND Chung", note: "Nuôi Master từ LM2596" }
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
        color: "#0284c7",
        icon: "fa-tv",
        pins: [
          { from: "SDA (Data)", to: "GPIO 21 (D21 Master)", note: "Chân I2C Data" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22 Master)", note: "Chân I2C Clock" },
          { from: "VCC & GND", to: "3.3V & GND (ESP32 Master)", note: "Nguồn nuôi màn hình" }
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
        color: "#dc2626",
        icon: "fa-bullhorn",
        pins: [
          { from: "Còi Buzzer (+)", to: "GPIO 23", note: "Âm lượng > 85dB hú ngắt quãng" },
          { from: "LED ĐỎ (+)", to: "GPIO 19", note: "Sáng khi Oxy < 18% hoặc có độc" },
          { from: "LED VÀNG (+)", to: "GPIO 5", note: "Sáng khi tiệm cận ngưỡng chú ý" },
          { from: "LED XANH (+)", to: "GPIO 18", note: "Sáng khi môi trường an toàn" },
          { from: "GND (Mass)", to: "GND Chung Master", note: "Cực âm chung" }
        ],
        codeSnippet: `// Kích hoạt còi hú ngắt quãng dồn dập (250ms bật / 250ms tắt)\nif (isDanger) {\n  digitalWrite(BUZZER_PIN, (millis() / 250) % 2 == 0 ? HIGH : LOW);\n}`,
        why: "TẠI SAO LẠI PHẢI ĐẶT CÒI HÚ VÀ ĐÈN NGAY TẠI MIỆNG CỬA HẦM?",
        whyContent: "ĐÂY LÀ ĐIỂM CỐT LÕI CỨU SỐNG CON NGƯỜI: Các máy đo hiện nay chỉ báo khi người đã cầm máy bước xuống hầm. Khi người dưới ngất, người trên bờ không biết gì sẽ nhảy xuống cứu và chết chùm. Còi hú công suất lớn đặt ngay tại miệng cửa hầm đóng vai trò như 'BỨC TƯỜNG ÂM THANH' đanh thép, cảnh báo trực diện làm người trên bờ giật mình khựng lại, dứt khoát không bước xuống!",
        physicsTip: "💡 Hàm handleAlarm điều khiển còi hú ngắt quãng 250ms bật / 250ms tắt để tạo âm thanh cảnh báo khẩn cấp dồn dập nhất."
      }
    ];

    // =========================================================================
    // DANH SÁCH TẤT CẢ CÁC ĐƯỜNG DÂY (KHÔNG BAO GIỜ ĐÈ LÊN CHỮ - MANHATTAN CHUẨN)
    // =========================================================================
    const WIRE_DEFINITIONS = [
      // 1. KHỐI SLAVE: ĐẤU NỐI BUS NGUỒN VCC (5V) & MASS GND
      { fromPort: "port-cat5-pwr-left", toPort: "port-rail-vcc-feed", gutterX: 1130, color: "var(--w-vcc)", stroke: 4.5, fromComponent: "cable_cat5e", toComponent: "esp32_slave", group: "cable_cat5e" },
      { fromPort: "port-cat5-gnd-left", toPort: "port-rail-gnd-feed", gutterX: 1110, color: "var(--w-gnd)", stroke: 4.5, fromComponent: "cable_cat5e", toComponent: "esp32_slave", group: "cable_cat5e" },

      // Bus Nguồn cấp cho ESP32 Slave VIN & GND (phía trái ESP32)
      { fromPort: "port-rail-vcc-feed", toPort: "port-esp32s-vin", gutterX: 430, color: "var(--w-vcc)", stroke: 3.5, fromComponent: "esp32_slave", toComponent: "esp32_slave", group: "esp32_slave" },
      { fromPort: "port-rail-gnd-feed", toPort: "port-esp32s-gnd", gutterX: 440, color: "var(--w-gnd)", stroke: 3.5, fromComponent: "esp32_slave", toComponent: "esp32_slave", group: "esp32_slave" },

      // CẢM BIẾN OXY DFROBOT
      { fromPort: "port-o2-vcc", toPort: "port-rail-vcc-o2", gutterX: 310, color: "var(--w-vcc)", stroke: 2.8, fromComponent: "o2_sensor", toComponent: "esp32_slave", group: "o2_sensor" },
      { fromPort: "port-o2-gnd", toPort: "port-rail-gnd-o2", gutterX: 375, color: "var(--w-gnd)", stroke: 2.8, fromComponent: "o2_sensor", toComponent: "esp32_slave", group: "o2_sensor" },
      { fromPort: "port-o2-sda", toPort: "port-esp32s-d21", gutterX: 425, color: "var(--w-i2c-sda)", stroke: 3.0, fromComponent: "o2_sensor", toComponent: "esp32_slave", group: "o2_sensor" },
      { fromPort: "port-o2-scl", toPort: "port-esp32s-d22", gutterX: 440, color: "var(--w-i2c-scl)", stroke: 3.0, fromComponent: "o2_sensor", toComponent: "esp32_slave", group: "o2_sensor" },

      // CẢM BIẾN MQ-7 KHÍ CO
      { fromPort: "port-mq7-vcc", toPort: "port-rail-vcc-mq7", gutterX: 310, color: "var(--w-vcc)", stroke: 2.8, fromComponent: "mq7_sensor", toComponent: "esp32_slave", group: "mq7_sensor" },
      { fromPort: "port-mq7-gnd", toPort: "port-rail-gnd-mq7", gutterX: 375, color: "var(--w-gnd)", stroke: 2.8, fromComponent: "mq7_sensor", toComponent: "esp32_slave", group: "mq7_sensor" },
      { fromPort: "port-mq7-a0", toPort: "port-esp32s-gpio35", gutterX: 425, color: "var(--w-mq7)", stroke: 3.2, fromComponent: "mq7_sensor", toComponent: "esp32_slave", group: "mq7_sensor" },

      // CẢM BIẾN MQ-4 KHÍ METAN
      { fromPort: "port-mq4-vcc", toPort: "port-rail-vcc-mq4", gutterX: 310, color: "var(--w-vcc)", stroke: 2.8, fromComponent: "mq4_sensor", toComponent: "esp32_slave", group: "mq4_sensor" },
      { fromPort: "port-mq4-gnd", toPort: "port-rail-gnd-mq4", gutterX: 375, color: "var(--w-gnd)", stroke: 2.8, fromComponent: "mq4_sensor", toComponent: "esp32_slave", group: "mq4_sensor" },
      { fromPort: "port-mq4-a0", toPort: "port-esp32s-gpio34", gutterX: 425, color: "var(--w-mq4)", stroke: 3.2, fromComponent: "mq4_sensor", toComponent: "esp32_slave", group: "mq4_sensor" },

      // CẢM BIẾN DHT22
      { fromPort: "port-dht22-vcc", toPort: "port-rail-vcc-dht22", gutterX: 310, color: "var(--w-vcc)", stroke: 2.8, fromComponent: "dht22_sensor", toComponent: "esp32_slave", group: "dht22_sensor" },
      { fromPort: "port-dht22-gnd", toPort: "port-rail-gnd-dht22", gutterX: 375, color: "var(--w-gnd)", stroke: 2.8, fromComponent: "dht22_sensor", toComponent: "esp32_slave", group: "dht22_sensor" },
      { fromPort: "port-dht22-data", toPort: "port-esp32s-d4", gutterX: 425, color: "var(--w-dht)", stroke: 3.2, fromComponent: "dht22_sensor", toComponent: "esp32_slave", group: "dht22_sensor" },

      // ESP32 SLAVE SANG MAX485 (PHÍA PHẢI ESP32 -> TRÁI MAX485, ZERO CROSSING)
      { fromPort: "port-esp32s-tx2", toPort: "port-max485s-di", gutterX: 790, color: "var(--w-uart)", stroke: 3.2, fromComponent: "max485_slave", toComponent: "esp32_slave", group: "max485_slave" },
      { fromPort: "port-esp32s-rx2", toPort: "port-max485s-ro", gutterX: 805, color: "var(--w-uart)", stroke: 3.2, fromComponent: "max485_slave", toComponent: "esp32_slave", group: "max485_slave" },
      { fromPort: "port-esp32s-vcc-out", toPort: "port-max485s-vcc", gutterX: 775, color: "var(--w-vcc)", stroke: 2.8, fromComponent: "max485_slave", toComponent: "esp32_slave", group: "max485_slave" },
      { fromPort: "port-esp32s-gnd-out", toPort: "port-max485s-gnd", gutterX: 760, color: "var(--w-gnd)", stroke: 2.8, fromComponent: "max485_slave", toComponent: "esp32_slave", group: "max485_slave" },

      // MAX485 SLAVE -> CÁP CAT5E
      { fromPort: "port-max485s-a", toPort: "port-cat5-rs485-left", gutterX: 1145, color: "var(--w-rs485-a)", stroke: 3.6, fromComponent: "max485_slave", toComponent: "cable_cat5e", group: "cable_cat5e" },
      { fromPort: "port-max485s-b", toPort: "port-cat5-rs485-left", gutterX: 1160, color: "var(--w-rs485-b)", stroke: 3.6, fromComponent: "max485_slave", toComponent: "cable_cat5e", group: "cable_cat5e" },

      // 2. KHỐI MASTER: LM2596 -> CÁP CAT5E & ESP32 MASTER
      { fromPort: "port-lm2596-out-pos", toPort: "port-cat5-pwr-right", gutterX: 1450, color: "var(--w-vcc)", stroke: 4.5, fromComponent: "lm2596", toComponent: "cable_cat5e", group: "cable_cat5e" },
      { fromPort: "port-lm2596-out-neg", toPort: "port-cat5-gnd-right", gutterX: 1470, color: "var(--w-gnd)", stroke: 4.5, fromComponent: "lm2596", toComponent: "cable_cat5e", group: "cable_cat5e" },

      { fromPort: "port-lm2596-out-pos", toPort: "port-esp32m-vin-in", gutterX: 320, color: "var(--w-vcc)", stroke: 3.2, fromComponent: "lm2596", toComponent: "esp32_master", group: "esp32_master" },
      { fromPort: "port-lm2596-out-neg", toPort: "port-esp32m-gnd-in", gutterX: 335, color: "var(--w-gnd)", stroke: 3.0, fromComponent: "lm2596", toComponent: "esp32_master", group: "esp32_master" },

      // Cáp Cat5e -> MAX485 Master
      { fromPort: "port-cat5-rs485-right", toPort: "port-max485m-a", gutterX: 1520, color: "var(--w-rs485-a)", stroke: 3.6, fromComponent: "cable_cat5e", toComponent: "max485_master", group: "cable_cat5e" },
      { fromPort: "port-cat5-rs485-right", toPort: "port-max485m-b", gutterX: 1535, color: "var(--w-rs485-b)", stroke: 3.6, fromComponent: "cable_cat5e", toComponent: "max485_master", group: "cable_cat5e" },

      // MAX485 Master -> ESP32 Master RX2 & Nguồn
      { fromPort: "port-max485m-ro", toPort: "port-esp32m-rx2", gutterX: 305, color: "var(--w-uart)", stroke: 3.2, fromComponent: "max485_master", toComponent: "esp32_master", group: "max485_master" },
      { fromPort: "port-esp32m-vin-in", toPort: "port-max485m-vcc", gutterX: 290, color: "var(--w-vcc)", stroke: 2.6, fromComponent: "max485_master", toComponent: "esp32_master", group: "max485_master" },
      { fromPort: "port-esp32m-gnd-in", toPort: "port-max485m-gnd", gutterX: 275, color: "var(--w-gnd)", stroke: 2.6, fromComponent: "max485_master", toComponent: "esp32_master", group: "max485_master" },

      // ESP32 MASTER RA OLED (XUẤT TỪ BÊN PHẢI SANG BÊN PHẢI - ZERO CROSSING)
      { fromPort: "port-esp32m-d21", toPort: "port-oled-sda", gutterX: 2240, color: "var(--w-i2c-sda)", stroke: 3.0, fromComponent: "esp32_master", toComponent: "oled_display", group: "oled_display" },
      { fromPort: "port-esp32m-d22", toPort: "port-oled-scl", gutterX: 2255, color: "var(--w-i2c-scl)", stroke: 3.0, fromComponent: "esp32_master", toComponent: "oled_display", group: "oled_display" },
      { fromPort: "port-esp32m-3v3-out", toPort: "port-oled-vcc", gutterX: 2225, color: "var(--w-vcc)", stroke: 2.8, fromComponent: "esp32_master", toComponent: "oled_display", group: "oled_display" },
      { fromPort: "port-esp32m-gnd-out", toPort: "port-oled-gnd", gutterX: 2210, color: "var(--w-gnd)", stroke: 2.8, fromComponent: "esp32_master", toComponent: "oled_display", group: "oled_display" },

      // ESP32 MASTER RA CÒI BUZZER & 3 ĐÈN LED (XUẤT TỪ PHÍA PHẢI - ZERO CROSSING)
      { fromPort: "port-esp32m-d23", toPort: "port-alarm-buzz", gutterX: 2240, color: "var(--w-buzz)", stroke: 3.5, fromComponent: "esp32_master", toComponent: "alarm_system", group: "alarm_system" },
      { fromPort: "port-esp32m-d19", toPort: "port-alarm-red", gutterX: 2255, color: "var(--w-led-r)", stroke: 3.2, fromComponent: "esp32_master", toComponent: "alarm_system", group: "alarm_system" },
      { fromPort: "port-esp32m-d5", toPort: "port-alarm-yel", gutterX: 2270, color: "var(--w-led-y)", stroke: 3.2, fromComponent: "esp32_master", toComponent: "alarm_system", group: "alarm_system" },
      { fromPort: "port-esp32m-d18", toPort: "port-alarm-grn", gutterX: 2285, color: "var(--w-led-g)", stroke: 3.2, fromComponent: "esp32_master", toComponent: "alarm_system", group: "alarm_system" },
      { fromPort: "port-esp32m-gnd-out", toPort: "port-alarm-gnd", gutterX: 2210, color: "var(--w-gnd)", stroke: 2.8, fromComponent: "esp32_master", toComponent: "alarm_system", group: "alarm_system" }
    ];

    // HỆ THỐNG VẼ ĐƯỜNG DÂY VUÔNG GÓC MANHATTAN ROUTING
    const wireGroup = document.getElementById("wire-group");
    const particlesGroup = document.getElementById("particles-group");
    const stage = document.getElementById("pan-zoom-stage");
    const container = document.getElementById("workspace-container");

    let currentFilter = "all";
    let isIsolateMode = true;
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

    function buildManhattanPath(p1, p2, gutterX, radius = 10) {
      const x1 = p1.x, y1 = p1.y;
      const x2 = p2.x, y2 = p2.y;

      const dirX1 = gutterX >= x1 ? 1 : -1;
      const dirX2 = x2 >= gutterX ? 1 : -1;
      const dirY = y2 >= y1 ? 1 : -1;

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

        let gutterX = wDef.gutterX;
        const pathD = buildManhattanPath(p1, p2, gutterX, 10);

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
        for (let p = 0; p < 2; p++) {
          const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          circle.setAttribute("r", wDef.stroke >= 4 ? 4 : 3);
          circle.setAttribute("fill", "#ffffff");
          circle.setAttribute("stroke", "#0f172a");
          circle.setAttribute("stroke-width", "1");
          circle.style.display = "none";
          particlesGroup.appendChild(circle);
          particles.push({ circle, progress: p * 0.5 });
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
          isHighlighted = (
            w.wDef.group === selectedCompId || 
            w.wDef.fromComponent === selectedCompId || 
            w.wDef.toComponent === selectedCompId ||
            selectedCompId === "all"
          );
        } else {
          isHighlighted = (
            w.wDef.group === currentFilter ||
            w.wDef.fromComponent === currentFilter ||
            w.wDef.toComponent === currentFilter
          );
        }

        if (isHighlighted) {
          w.path.setAttribute("stroke-width", w.wDef.stroke + 2.2);
          w.path.setAttribute("opacity", "1");
        } else {
          w.path.setAttribute("stroke-width", w.wDef.stroke);
          w.path.setAttribute("opacity", isIsolateMode ? "0.1" : "0.38");
        }
      });
    }

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

    const btnToggleIsolate = document.getElementById("btn-toggle-isolate");
    const isolateText = document.getElementById("isolate-text");
    btnToggleIsolate.onclick = () => {
      isIsolateMode = !isIsolateMode;
      isolateText.textContent = isIsolateMode ? "Làm Mờ Dây Khác: BẬT" : "Làm Mờ Dây Khác: TẮT";
      btnToggleIsolate.classList.toggle("active", isIsolateMode);
      applyWireVisibility();
    };

    // PAN & ZOOM BÀN LÀM VIỆC (MẶC ĐỊNH VIEW TOÀN CẢNH ĐẸP MẮT)
    let scale = 0.58;
    let panX = 180;
    let panY = 10;
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
      scale = Math.min(Math.max(scale * zoomFactor, 0.35), 1.6);
      updateTransform();
    }, { passive: false });

    document.getElementById("btn-reset-view").onclick = () => {
      scale = 0.58; panX = 180; panY = 10;
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
        <div class="comp-icon" style="color: ${comp.color};">
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

    // HÀM CHỌN THIẾT BỊ: TUYỆT ĐỐI KHÔNG LÀM NHẢY MÀN HÌNH (NO SCREEN JUMP!)
    function selectComponent(compId) {
      selectedCompId = compId;
      const comp = COMPONENTS.find(c => c.id === compId);
      if (!comp) return;

      document.querySelectorAll(".comp-item").forEach(el => el.classList.remove("active"));
      const selectedItem = document.getElementById(`item-${comp.id}`);
      if (selectedItem) selectedItem.classList.add("active");

      document.querySelectorAll(".comp-card").forEach(el => {
        el.classList.remove("active");
        el.style.removeProperty("--active-color");
      });

      const cardEl = document.getElementById(`card-${comp.id}`);
      if (cardEl) {
        cardEl.style.setProperty("--active-color", comp.color);
        cardEl.classList.add("active");
        // CHÚ Ý: ĐÃ XÓA BỎ LỆNH GÂY NHẢY MÀN HÌNH (panX/panY giữ nguyên vị trí cố định)
      }

      applyWireVisibility();

      // Render nội dung bảng thông tin chi tiết
      detailCategory.textContent = comp.group;
      detailCategory.style.color = comp.color;
      detailBody.innerHTML = `
        <div class="comp-badge" style="color: ${comp.color}; border-color: ${comp.color};">
          <i class="fa-solid ${comp.icon}"></i> ${comp.badge}
        </div>
        <div class="comp-title-large">${comp.name}</div>
        <div style="font-size: 0.82rem; color: var(--text-muted); font-weight: 500;">${comp.sub}</div>

        <a class="repo-pill" href="${comp.repoUrl}" target="_blank">
          <i class="fa-brands fa-github"></i> <b>Repo thư viện:</b> ${comp.repo}
        </a>

        <div class="pin-mapping-box">
          <h4><i class="fa-solid fa-arrows-split-up-and-left"></i> Sơ đồ chân kết nối đầy đủ (Tín hiệu + Nguồn + Mass)</h4>
          ${comp.pins.map(p => `
            <div class="pin-row">
              <span class="pin-from"><i class="fa-solid fa-plug"></i> ${p.from}</span>
              <span class="pin-arrow"><i class="fa-solid fa-arrow-right"></i></span>
              <span class="pin-to" style="color: ${comp.color}; border-color: ${comp.color}55;">${p.to}</span>
            </div>
            <div style="font-size: 0.72rem; color: var(--text-muted); margin: -2px 0 6px 12px;">• ${p.note}</div>
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

    // NÚT CHUYỂN ĐỔI CHẾ ĐỘ SÁNG / TỐI (LIGHT / DARK THEME)
    const btnTheme = document.getElementById("btn-theme-toggle");
    const themeText = document.getElementById("theme-text");
    let isDarkMode = false; // Mặc định là chế độ Sáng (White Technical Mode)

    btnTheme.onclick = () => {
      isDarkMode = !isDarkMode;
      document.body.classList.toggle("dark-mode", isDarkMode);
      document.body.classList.toggle("light-mode", !isDarkMode);
      if (isDarkMode) {
        btnTheme.innerHTML = '<i class="fa-solid fa-moon"></i> <span id="theme-text">Giao Diện: Tối (Dark Tech)</span>';
      } else {
        btnTheme.innerHTML = '<i class="fa-solid fa-sun"></i> <span id="theme-text">Giao Diện: Sáng (Kỹ Thuật)</span>';
      }
      renderAllWires();
    };

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
      } else {
        ledGreen.value = 0;
        ledYellow.value = 0;
        ledRed.value = 1;
      }
    }

    btnSafe.onclick = () => setAlarmLevel("safe");
    btnWarn.onclick = () => setAlarmLevel("warn");
    btnDang.onclick = () => setAlarmLevel("dang");

    // ANIMATION LOOP: DI CHUYỂN ELECTRON DÒNG ĐIỆN VÀ CHỚP NHÁY BÁO ĐỘNG
    let lastTime = performance.now();
    let blinkTimer = 0;

    function animate(time) {
      requestAnimationFrame(animate);
      const dt = (time - lastTime) / 1000;
      lastTime = time;

      if (isPowerOn) {
        activeWires.forEach(w => {
          w.particles.forEach(p => {
            p.progress = (p.progress + dt * 0.45) % 1.0;
            const pt = w.path.getPointAtLength(p.progress * w.totalLength);
            p.circle.setAttribute("cx", pt.x);
            p.circle.setAttribute("cy", pt.y);
          });
        });

        if (currentAlarmLevel === "dang") {
          blinkTimer += dt;
          if (blinkTimer > 0.25) {
            blinkTimer = 0;
            const isRedOn = ledRed.value === 1;
            ledRed.value = isRedOn ? 0 : 1;
          }
        }
      }
    }

    // KHỞI ĐỘNG HỆ THỐNG (KHÔNG JUMP, GIỮ VỊ TRÍ VIEW CHUẨN)
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

output_path = os.path.abspath(r'mo_phong_3d_noi_day\index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_code)

print(f"Successfully updated {output_path} with White Technical Mode and Fixed Jump/Crossings!")
