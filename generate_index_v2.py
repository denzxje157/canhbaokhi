# -*- coding: utf-8 -*-
"""
Script to generate the updated index.html with:
1. Real 3D GLB model for ESP32 boards (via esp32_glb_data.js)
2. Professional CAD-precision procedural models for all sensors and modules
3. High-performance OrbitControls tuning (buttery smooth 60+ FPS navigation)
4. Clean modern electronics lab workbench environment (no ugly dark/muddy look)
5. Refined UI with smooth transitions and audio feedback
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mô Phỏng 3D Nối Dây & Thiết Bị Thật - Cảnh Báo Khí Độc</title>
  <!-- Three.js, OrbitControls & GLTFLoader -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
  <!-- Embedded Real ESP32 3D Model Data -->
  <script src="esp32_glb_data.js"></script>
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg-gradient: radial-gradient(circle at 50% 30%, #151f32 0%, #0a0f1d 100%);
      --panel-bg: rgba(15, 23, 42, 0.88);
      --panel-border: rgba(56, 189, 248, 0.22);
      --cyan: #06b6d4;
      --cyan-glow: rgba(6, 182, 212, 0.35);
      --blue: #3b82f6;
      --red: #ef4444;
      --yellow: #f59e0b;
      --green: #10b981;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg-gradient);
      color: var(--text-main);
      overflow: hidden;
      width: 100vw;
      height: 100vh;
    }

    #canvas-container {
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0;
      left: 0;
      z-index: 1;
      cursor: grab;
    }
    #canvas-container:active {
      cursor: grabbing;
    }

    /* TOP HEADER */
    header {
      position: absolute;
      top: 15px;
      left: 20px;
      right: 20px;
      z-index: 10;
      display: flex;
      justify-content: space-between;
      align-items: center;
      pointer-events: none;
    }

    .header-title {
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      backdrop-filter: blur(16px);
      padding: 10px 22px;
      border-radius: 14px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.45);
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
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      color: var(--text-main);
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
      color: var(--text-muted);
      opacity: 0.7;
    }

    /* LEFT SIDEBAR: LINH KIỆN */
    .sidebar-left {
      position: absolute;
      top: 85px;
      left: 20px;
      bottom: 25px;
      width: 300px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 16px;
      backdrop-filter: blur(18px);
      z-index: 10;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.45);
      overflow: hidden;
    }

    .panel-hdr {
      padding: 13px 16px;
      border-bottom: 1px solid var(--panel-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 700;
      font-size: 0.86rem;
      color: #38bdf8;
      letter-spacing: 0.5px;
      background: rgba(15, 23, 42, 0.6);
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
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .comp-item {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 8px 12px;
      border-radius: 10px;
      background: rgba(30, 41, 59, 0.35);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .comp-item:hover {
      background: rgba(30, 41, 59, 0.85);
      border-color: rgba(56, 189, 248, 0.3);
      transform: translateX(3px);
    }

    .comp-item.active {
      background: linear-gradient(90deg, rgba(6, 182, 212, 0.18), rgba(59, 130, 246, 0.12));
      border-color: var(--cyan);
      box-shadow: 0 0 14px rgba(6, 182, 212, 0.25);
    }

    .comp-icon {
      width: 34px;
      height: 34px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.05rem;
      flex-shrink: 0;
    }

    .comp-info {
      flex: 1;
      min-width: 0;
    }

    .comp-name {
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-main);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .comp-sub {
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 1px;
    }

    /* RIGHT SIDEBAR: CHI TIẾT NỐI CHÂN */
    .sidebar-right {
      position: absolute;
      top: 85px;
      right: 20px;
      bottom: 25px;
      width: 390px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 16px;
      backdrop-filter: blur(18px);
      z-index: 10;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.45);
      overflow: hidden;
    }

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

    .pin-mapping-box {
      margin-top: 14px;
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

    .pin-row:last-child {
      border-bottom: none;
    }

    .pin-from {
      color: #e2e8f0;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .pin-arrow {
      color: #64748b;
      font-size: 0.7rem;
    }

    .pin-to {
      color: #38bdf8;
      font-family: monospace;
      font-weight: 600;
      background: rgba(56, 189, 248, 0.12);
      padding: 2px 7px;
      border-radius: 5px;
      border: 1px solid rgba(56, 189, 248, 0.25);
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
      left: 340px;
      right: 430px;
      height: 60px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 14px;
      backdrop-filter: blur(18px);
      z-index: 10;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.45);
    }

    .flow-status {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .status-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #64748b;
      box-shadow: 0 0 8px rgba(100, 116, 139, 0.4);
    }

    .status-dot.active {
      background: var(--green);
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.8);
      animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.7; }
    }

    .status-text {
      font-size: 0.82rem;
      font-weight: 600;
    }

    .sim-levels {
      display: flex;
      gap: 8px;
    }

    .btn-level {
      padding: 6px 12px;
      font-size: 0.78rem;
      border-radius: 8px;
      border: 1px solid #334155;
      background: rgba(30, 41, 59, 0.6);
      color: var(--text-main);
      cursor: pointer;
      font-weight: 600;
      transition: all 0.2s;
    }

    .btn-level.active-safe {
      background: var(--green);
      border-color: #34d399;
      color: #fff;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
    }

    .btn-level.active-warn {
      background: var(--yellow);
      border-color: #fbbf24;
      color: #000;
      box-shadow: 0 0 12px rgba(245, 158, 11, 0.4);
    }

    .btn-level.active-dang {
      background: var(--red);
      border-color: #f87171;
      color: #fff;
      box-shadow: 0 0 12px rgba(239, 68, 68, 0.5);
    }

    /* 3D LABEL HOVER */
    .view-tips {
      position: absolute;
      top: 85px;
      left: 340px;
      z-index: 5;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(56, 189, 248, 0.2);
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 0.75rem;
      color: var(--text-muted);
      pointer-events: none;
      backdrop-filter: blur(10px);
    }

    /* SCROLLBAR */
    ::-webkit-scrollbar {
      width: 5px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(15, 23, 42, 0.5);
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #475569;
    }
  </style>
</head>
<body>

  <!-- 3D CANVAS -->
  <div id="canvas-container"></div>

  <!-- TOP HEADER -->
  <header>
    <div class="header-title">
      <h1><i class="fa-solid fa-microchip"></i> MÔ PHỎNG 3D THIẾT BỊ THẬT & ĐƯỜNG NỐI DÂY</h1>
      <p>Hệ Thống Cảnh Báo Sớm Khí Độc & Thiếu Oxygen Trong Không Gian Kín (THCS)</p>
    </div>
    <div class="header-actions">
      <button class="btn btn-power" id="btn-power">
        <i class="fa-solid fa-power-off"></i> <span id="power-text">BẬT NGUỒN PIN</span>
      </button>
      <button class="btn" id="btn-labels">
        <i class="fa-solid fa-tags"></i> <span id="label-text">Tắt Nhãn 3D</span>
      </button>
      <button class="btn btn-sound" id="btn-sound">
        <i class="fa-solid fa-volume-high"></i> <span id="sound-text">Âm Thanh: BẬT</span>
      </button>
      <button class="btn" id="btn-schematic">
        <i class="fa-solid fa-diagram-project"></i> Sơ Đồ 2D
      </button>
      <button class="btn" id="btn-reset-view">
        <i class="fa-solid fa-arrows-rotate"></i> Đặt Lại Góc Nhìn
      </button>
    </div>
  </header>

  <div class="view-tips">
    <i class="fa-solid fa-hand-pointer"></i> <b>Kéo chuột:</b> Xoay 360° mượt mà | <b>Cuộn chuột:</b> Phóng to/Thu nhỏ | <b>Click thiết bị:</b> Xem lý do kỹ thuật nối chân
  </div>

  <!-- SIDEBAR TRÁI: DANH SÁCH LINH KIỆN -->
  <div class="sidebar-left">
    <div class="panel-hdr">
      <span><i class="fa-solid fa-layer-group"></i> LINH KIỆN HỆ THỐNG</span>
      <span style="font-size: 0.72rem; color: var(--text-muted);">11 Thiết bị</span>
    </div>
    <div class="component-list" id="comp-list">
      <!-- Render bằng Javascript -->
    </div>
  </div>

  <!-- BOTTOM BAR: MÔ PHỎNG DÒNG ĐIỆN & CẤP ĐỘ KHÍ -->
  <div class="bottom-bar">
    <div class="flow-status">
      <div class="status-dot" id="flow-dot"></div>
      <div>
        <div class="status-text" id="flow-status-text">Nguồn đang tắt (Chưa có dòng điện)</div>
        <div style="font-size: 0.7rem; color: var(--text-muted);" id="flow-desc">Bấm 'BẬT NGUỒN PIN' để kích hoạt dòng điện và truyền nhận RS485</div>
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
      <span><i class="fa-solid fa-circle-info"></i> THÔNG TIN KẾT NỐI CHI TIẾT</span>
      <span style="font-size: 0.75rem; color: var(--cyan);" id="detail-category">SLAVE</span>
    </div>
    <div class="detail-body" id="detail-body">
      <!-- Sẽ render động khi click linh kiện -->
    </div>
  </div>

  <script>
    // =========================================================================
    // 1. DỮ LIỆU ĐẦY ĐỦ CÁC THIẾT BỊ, NỐI CHÂN & GIẢI THÍCH "TẠI SAO NỐI NHƯ VẬY"
    // =========================================================================
    const COMPONENTS = [
      // --- KHỐI DƯỚI ĐÁY KHÔNG GIAN KÍN (SLAVE) ---
      {
        id: "o2_sensor",
        name: "Cảm Biến Oxygen (O2)",
        sub: "DFRobot Gravity I2C (0x73)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Cảm biến điện hóa I2C",
        color: "#06b6d4",
        icon: "fa-lungs",
        pos: { x: -3.8, y: -1.2, z: 2.1 },
        pins: [
          { from: "VCC", to: "3.3V / 5V (ESP32)", note: "Nguồn nuôi mạch cảm biến" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" },
          { from: "SDA (Data)", to: "GPIO 21 (D21)", note: "Chân I2C Data phần cứng" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22)", note: "Chân I2C Clock phần cứng" }
        ],
        why: "TẠI SAO NỐI VÀO D21 (SDA) VÀ D22 (SCL)?",
        whyContent: "Trên vi điều khiển ESP32, chân GPIO 21 và GPIO 22 được thiết kế sẵn phần cứng chuyên dụng cho bus truyền thông I2C (Wire). Cảm biến Oxy DFRobot có sẵn chip ADC 16-bit nội bộ, xuất dữ liệu số qua địa chỉ hex 0x73. Nối đúng vào D21/D22 giúp ESP32 đọc nồng độ Oxy với tốc độ cao, hoàn toàn không bị trễ nhịp và không cần viết code giả lập I2C mềm bằng phần mềm.",
        physicsTip: "💡 Quy chuẩn QCVN 34: Khi Oxy < 18.0%, não bộ bị tê liệt ngạt thở sau 30-45 giây. Bình thường không khí đạt 20.9%."
      },
      {
        id: "mq7_sensor",
        name: "Cảm Biến Khí Than Độc (CO)",
        sub: "Module Winsen MQ-7 (AO)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Lò nung sấy SnO2 bán dẫn",
        color: "#f97316",
        icon: "fa-skull-crossbones",
        pos: { x: -3.8, y: -1.2, z: 0.5 },
        pins: [
          { from: "VCC", to: "5.0V (Sau LM2596)", note: "Cấp lò nung sấy nhiệt" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" },
          { from: "A0 (Analog)", to: "GPIO 35", note: "Khối ADC1 Input Only" }
        ],
        why: "TẠI SAO NỐI VÀO CHÂN GPIO 35?",
        whyContent: "GPIO 35 là chân Analog thuần túy (Input-Only) thuộc khối ADC1 của ESP32. Nếu nối nhầm sang khối ADC2 (như GPIO 0, 2, 4, 12, 13, 14, 15), việc đọc cảm biến sẽ BỊ TREO HOẶC SAI LỆCH NẶNG khi chip bật sóng Wi-Fi/Bluetooth do phần cứng ADC2 bị chiếm dụng. Nối GPIO 35 đảm bảo đo đạc khí CO liên tục, tuyệt đối chính xác.",
        physicsTip: "💡 Khí CO ái lực với hemoglobin gấp 250 lần Oxy. Ngưỡng 30 ppm là mức nguy hại phải kích hoạt còi báo ngay lập tức."
      },
      {
        id: "mq4_sensor",
        name: "Cảm Biến Khí Gas/Metan (CH4)",
        sub: "Module Winsen MQ-4 (AO)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Cảm biến nung khí cháy",
        color: "#eab308",
        icon: "fa-fire-flame-simple",
        pos: { x: -3.8, y: -1.2, z: -1.1 },
        pins: [
          { from: "VCC", to: "5.0V (Sau LM2596)", note: "Cấp lò nung sấy nhiệt" },
          { from: "GND", to: "GND Chung", note: "Chân mass chung" },
          { from: "A0 (Analog)", to: "GPIO 34", note: "Khối ADC1 Input Only" }
        ],
        why: "TẠI SAO NỐI VÀO CHÂN GPIO 34?",
        whyContent: "Tương tự như MQ-7, GPIO 34 thuộc bộ chuyển đổi ADC1 nội bộ độc lập. Cảm biến MQ-4 tiêu thụ dòng sấy lớn (~150mA), khi nung nóng điện trở SnO2 giảm tỉ lệ với mật độ khí Metan bốc lên từ bùn rác thối. Đo điện áp qua GPIO 34 giúp cập nhật %LEL (Giới hạn nổ dưới) ổn định nhất.",
        physicsTip: "💡 Giới hạn nổ dưới (LEL) của CH4 là 5% thể tích. Khi đạt >= 10% LEL, tia lửa nhỏ từ giày dép hay kim loại cũng có thể gây nổ hầm."
      },
      {
        id: "dht22_sensor",
        name: "Cảm Biến Nhiệt Độ - Độ Ẩm",
        sub: "Aosong AM2302 (DHT22)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Bù nhiệt ẩm môi trường",
        color: "#3b82f6",
        icon: "fa-temperature-half",
        pos: { x: -3.8, y: -1.2, z: -2.5 },
        pins: [
          { from: "VCC (Chân 1)", to: "3.3V / 5V (ESP32)", note: "Nguồn nuôi cảm biến" },
          { from: "DATA (Chân 2)", to: "GPIO 4 (D4)", note: "Chân 1-Wire số giao tiếp" },
          { from: "NC (Chân 3)", to: "Bỏ trống", note: "Không kết nối" },
          { from: "GND (Chân 4)", to: "GND Chung", note: "Chân mass chung" }
        ],
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
        color: "#10b981",
        icon: "fa-microchip",
        pos: { x: -1.8, y: -1.2, z: 0.0 },
        pins: [
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Slave)", note: "Nhận lệnh từ mặt đất (nếu có)" },
          { from: "GPIO 17 (TX2)", to: "DI (MAX485 Slave)", note: "Bắn chuỗi JSON dữ liệu lên mặt đất" },
          { from: "GPIO 2", to: "LED Xanh Báo Nhịp", note: "Nhấp nháy báo chip còn sống" },
          { from: "VIN & GND", to: "5.2V Nguồn Cáp & GND", note: "Nhận điện từ LM2596 mặt đất cấp xuống" }
        ],
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
        color: "#a855f7",
        icon: "fa-network-wired",
        pos: { x: -0.3, y: -1.2, z: 0.0 },
        pins: [
          { from: "RO / DI", to: "GPIO 16 / GPIO 17", note: "Cổng nối tiếp UART2" },
          { from: "RE & DE", to: "GND / 3.3V (hoặc GPIO)", note: "Chế độ truyền Transmit (TX)" },
          { from: "Chân A (+)", to: "Dây Xanh Dương Cáp Mạng", note: "Tín hiệu vi sai dương RS485" },
          { from: "Chân B (-)", to: "Dây Trắng - Xanh Dương", note: "Tín hiệu vi sai âm RS485" }
        ],
        why: "TẠI SAO PHẢI DÙNG MAX485 THAY VÌ KÉO DÂY UART TRỰC TIẾP?",
        whyContent: "Tín hiệu UART chỉ có biên độ 3.3V và dựa vào mass đất. Nếu kéo dây đi xa 10-30m trong môi trường ẩm ướt đầy sóng điện trường, xung điện áp sẽ bị méo mó hoàn toàn. MAX485 biến đổi thành tín hiệu vi sai (hiệu điện thế giữa 2 dây A và B). Mọi xung nhiễu đánh vào cả 2 dây sẽ tự động triệt tiêu nhau, giúp đường truyền không mất một bit dữ liệu nào.",
        physicsTip: "💡 Nguyên lý vi sai: V_out = V_A - V_B. Nhiễu đánh vào cả 2 dây như nhau nên (V_A + noise) - (V_B + noise) = V_A - V_B (Triệt nhiễu tuyệt đối)."
      },

      // --- ĐƯỜNG TRUYỀN DẪN VẬT LÝ ---
      {
        id: "cable_cat5e",
        name: "Cáp Mạng Cat5e (Cụm 3 - 3 - 2)",
        sub: "Chiều dài thực tế 10m - 50m",
        group: "ĐƯỜNG TRUYỀN VẬT LÝ",
        badge: "Giải pháp Vật lý 9 chống sụt áp",
        color: "#f59e0b",
        icon: "fa-ethernet",
        pos: { x: 1.1, y: 0.0, z: 0.0 },
        pins: [
          { from: "Cụm 3 Dây Dương (+)", to: "Cam, Trắng-Cam, Trắng-Nâu", note: "Tăng tiết diện S gấp 3, giảm điện trở R 3 lần" },
          { from: "Cụm 3 Dây Mass (GND)", to: "Nâu, Xanh Lá, Trắng-Xanh Lá", note: "Đường hồi tiếp dòng điện nung lớn" },
          { from: "Cụm 2 Dây Tín Hiệu", to: "Xanh Dương (A) & Trắng-Xanh (B)", note: "Cặp xoắn chống nhiễu vi sai RS485" }
        ],
        why: "TẠI SAO LẠI PHẢI CHẬP CỤM 3 SỢI VÀ CHỈNH NGUỒN LÊN 5.2V?",
        whyContent: "Theo công thức Vật lý 9: R = rho * (l / S). Một sợi lõi đồng cáp Cat5e rất mảnh (S = 0.2 mm2). Với chiều dài 20m cả đi và về, điện trở dây lên tới 3.5 Ohm. Các cảm biến nung nhiệt MQ dưới đáy ngốn dòng 0.4A, gây sụt áp Delta U = I * R = 0.4 * 3.5 = 1.4V! Nếu cấp 5V ở trên, xuống đáy chỉ còn 3.6V làm cảm biến chết đứng. Bằng cách chập 3 sợi làm 1, ta tăng tiết diện S gấp 3 lần, làm giảm R đi 3 lần, kết hợp vặn LM2596 lên 5.2V bù trừ, điện áp dưới đáy luôn duy trì chuẩn 4.95V - 5.05V.",
        physicsTip: "💡 Đây là điểm sáng kiến kỹ thuật đạt điểm tối đa trước ban giám khảo vì áp dụng định luật Ohm và công thức điện trở thuần túy."
      },

      // --- KHỐI TRÊN MẶT ĐẤT (MASTER) ---
      {
        id: "max485_master",
        name: "Module Chuyển Đổi MAX485 (Master)",
        sub: "RS-485 sang UART Vi Điều Khiển",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Bộ thu tín hiệu từ đáy giếng",
        color: "#a855f7",
        icon: "fa-network-wired",
        pos: { x: 2.3, y: 1.2, z: 0.0 },
        pins: [
          { from: "Chân A & B", to: "Nhận từ Cáp Cat5e", note: "Tín hiệu vi sai từ dưới đáy đưa lên" },
          { from: "RO", to: "GPIO 16 (RX2 Master)", note: "Đưa dữ liệu vào ESP32 Master" },
          { from: "VCC / GND", to: "5V & GND Nguồn Chung", note: "Nguồn nuôi module" }
        ],
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
        color: "#0284c7",
        icon: "fa-bolt",
        pos: { x: 2.3, y: 1.2, z: 1.9 },
        pins: [
          { from: "IN+ / IN-", to: "Pin Lithium 7.4V - 12V", note: "Điện áp nguồn pin tại chỗ trên mặt đất" },
          { from: "OUT+ (5.2V)", to: "Cụm 3 Dây Dương Cáp Cat5e", note: "Chỉnh chiết áp bù 0.2V sụt áp đường dài" },
          { from: "OUT- (GND)", to: "Cụm 3 Dây Mass Cáp Cat5e", note: "Cực âm chung toàn hệ thống" }
        ],
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
        color: "#6366f1",
        icon: "fa-microchip",
        pos: { x: 4.0, y: 1.2, z: 0.0 },
        pins: [
          { from: "GPIO 21 & 22", to: "OLED SSD1306 (SDA & SCL)", note: "I2C Hiển thị số đo" },
          { from: "GPIO 23", to: "Còi Hú Báo Động (Buzzer)", note: "Bức tường âm thanh ngăn nhảy cứu" },
          { from: "GPIO 19", to: "LED ĐỎ (Nguy hiểm)", note: "Trở hạn dòng 220 Ohm" },
          { from: "GPIO 5", to: "LED VÀNG (Cảnh báo)", note: "Trở hạn dòng 220 Ohm" },
          { from: "GPIO 18", to: "LED XANH (An toàn)", note: "Trở hạn dòng 220 Ohm" }
        ],
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
        color: "#38bdf8",
        icon: "fa-tv",
        pos: { x: 4.0, y: 1.2, z: 1.9 },
        pins: [
          { from: "VCC / GND", to: "3.3V / 5V & GND", note: "Nguồn nuôi màn hình" },
          { from: "SDA (Data)", to: "GPIO 21 (D21 Master)", note: "Chân I2C Data" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22 Master)", note: "Chân I2C Clock" }
        ],
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
        color: "#ef4444",
        icon: "fa-bullhorn",
        pos: { x: 4.0, y: 1.2, z: -1.9 },
        pins: [
          { from: "Còi Buzzer (+)", to: "GPIO 23", note: "Âm lượng > 85dB hú ngắt quãng" },
          { from: "LED ĐỎ (+)", to: "GPIO 19", note: "Sáng khi Oxy < 18% hoặc có độc" },
          { from: "LED VÀNG (+)", to: "GPIO 5", note: "Sáng khi tiệm cận ngưỡng chú ý" },
          { from: "LED XANH (+)", to: "GPIO 18", note: "Sáng khi môi trường an toàn" }
        ],
        why: "TẠI SAO LẠI PHẢI ĐẶT CÒI HÚ VÀ ĐÈN NGAY TẠI MIỆNG CỬA HẦM?",
        whyContent: "ĐÂY LÀ ĐIỂM CỐT LÕI CỨU SỐNG CON NGƯỜI: Các máy đo hiện nay chỉ báo khi người đã cầm máy bước xuống hầm. Khi người dưới ngất, người trên bờ không biết gì sẽ nhảy xuống cứu và chết chùm. Còi hú công suất lớn đặt ngay tại miệng cửa hầm đóng vai trò như 'BỨC TƯỜNG ÂM THANH' đanh thép, cảnh báo trực diện làm người trên bờ giật mình khựng lại, dứt khoát không bước xuống!",
        physicsTip: "💡 Hàm handleAlarm điều khiển còi hú ngắt quãng 250ms bật / 250ms tắt để tạo âm thanh cảnh báo khẩn cấp dồn dập nhất."
      }
    ];

    // =========================================================================
    // 2. KHỞI TẠO KHÔNG GIAN 3D TỐI ƯU HIỆU NĂNG CAO (60+ FPS)
    // =========================================================================
    const container = document.getElementById("canvas-container");
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0e1726);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.set(0, 9.0, 13.0);

    const renderer = new THREE.WebGLRenderer({
      antialias: true,
      powerPreference: "high-performance"
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5)); // Tránh lag giật trên màn hình 4K/Retina
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.BasicShadowMap; // Tối ưu mượt mà tuyệt đối
    renderer.outputEncoding = THREE.sRGBEncoding;
    container.appendChild(renderer.domElement);

    // BỘ ĐIỀU KHIỂN CAMERA MƯỢT MÀ, VUỐT ĐÂU THEO ĐÓ
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.12; // Độ trễ thấp, vuốt cực nhạy và dừng êm
    controls.rotateSpeed = 0.85;
    controls.zoomSpeed = 1.2;
    controls.panSpeed = 0.8;
    controls.screenSpacePanning = true;
    controls.maxPolarAngle = Math.PI / 2 + 0.02;
    controls.minDistance = 3.0;
    controls.maxDistance = 25;
    controls.target.set(0, 0, 0);

    // HỆ THỐNG ÁNH SÁNG STUDIO CHUYÊN NGHIỆP CHO ĐIỆN TỬ
    // Ánh sáng môi trường hai màu (Hemisphere Light)
    const hemiLight = new THREE.HemisphereLight(0xe0f2fe, 0x1e293b, 1.15);
    scene.add(hemiLight);

    // Đèn rọi chính (Key Directional Light)
    const keyLight = new THREE.DirectionalLight(0xffffff, 1.3);
    keyLight.position.set(6, 14, 8);
    keyLight.castShadow = true;
    keyLight.shadow.mapSize.width = 1024;
    keyLight.shadow.mapSize.height = 1024;
    keyLight.shadow.camera.near = 1;
    keyLight.shadow.camera.far = 30;
    keyLight.shadow.camera.left = -9;
    keyLight.shadow.camera.right = 9;
    keyLight.shadow.camera.top = 9;
    keyLight.shadow.camera.bottom = -9;
    scene.add(keyLight);

    // Đèn viền phản chiếu mềm mại (Soft Fill Light)
    const fillLight = new THREE.DirectionalLight(0x38bdf8, 0.45);
    fillLight.position.set(-6, 8, -6);
    scene.add(fillLight);

    // MẶT BÀN LÀM VIỆC ĐIỆN TỬ CHỐNG TĨNH ĐIỆN (ESD WORKBENCH MATS)
    function createEsdMat(x, y, z, width, length, colorHex, borderHex) {
      const group = new THREE.Group();
      group.position.set(x, y, z);

      // Tấm thảm cao su ESD
      const matMat = new THREE.MeshStandardMaterial({
        color: colorHex,
        roughness: 0.7,
        metalness: 0.15
      });
      const mat = new THREE.Mesh(new THREE.BoxGeometry(width, 0.25, length), matMat);
      mat.receiveShadow = true;
      group.add(mat);

      // Viền cao su bo mép
      const borderMat = new THREE.MeshStandardMaterial({
        color: borderHex,
        roughness: 0.5,
        metalness: 0.3
      });
      const border = new THREE.Mesh(new THREE.BoxGeometry(width + 0.15, 0.2, length + 0.15), borderMat);
      border.position.y = -0.05;
      border.receiveShadow = true;
      group.add(border);

      // Lưới tọa độ vạch kẻ trên thảm
      const grid = new THREE.GridHelper(Math.max(width, length), 10, 0x334155, 0x1e293b);
      grid.position.y = 0.13;
      group.add(grid);

      scene.add(group);
      return group;
    }

    // Thảm 1: Khối Không Gian Kín (Slave - Đáy)
    createEsdMat(-2.8, -1.6, 0.0, 5.6, 6.8, 0x182032, 0x3b82f6);
    // Thảm 2: Khối Mặt Đất (Master)
    createEsdMat(3.4, 0.8, 0.0, 5.2, 6.8, 0x162438, 0x06b6d4);

    // =========================================================================
    // 3. TẠO CÁC TEXTURE PROCEDURAL CHẤT LƯỢNG CAO
    // =========================================================================

    // Texture lưới thép không gỉ (MQ Sensor Mesh)
    function makeMeshTexture() {
      const cv = document.createElement("canvas");
      cv.width = 128; cv.height = 128;
      const c = cv.getContext("2d");
      c.fillStyle = "#8a94a6";
      c.fillRect(0, 0, 128, 128);

      c.strokeStyle = "#475569";
      c.lineWidth = 2;
      for (let i = 0; i < 128; i += 6) {
        c.beginPath(); c.moveTo(i, 0); c.lineTo(i, 128); c.stroke();
        c.beginPath(); c.moveTo(0, i); c.lineTo(128, i); c.stroke();
      }
      c.fillStyle = "#cbd5e1";
      for (let x = 1; x < 128; x += 6) {
        for (let y = 1; y < 128; y += 6) {
          c.fillRect(x, y, 2.5, 2.5);
        }
      }
      const tex = new THREE.CanvasTexture(cv);
      tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
      tex.repeat.set(4, 2);
      return tex;
    }

    // Dynamic Canvas Texture cho OLED Display
    const oledCanvas = document.createElement("canvas");
    oledCanvas.width = 256; oledCanvas.height = 128;
    const oledTexture = new THREE.CanvasTexture(oledCanvas);

    function updateOledDisplay(lvl) {
      const c = oledCanvas.getContext("2d");
      c.fillStyle = "#020617";
      c.fillRect(0, 0, 256, 128);

      c.strokeStyle = "#1e3a8a";
      c.lineWidth = 2;
      c.strokeRect(2, 2, 252, 124);

      c.fillStyle = "#facc15";
      c.font = "bold 13px monospace";
      c.fillText("GIAM SAT KHONG GIAN KIN", 10, 20);

      c.strokeStyle = "#334155";
      c.beginPath(); c.moveTo(5, 26); c.lineTo(251, 26); c.stroke();

      c.fillStyle = "#38bdf8";
      c.font = "bold 13px monospace";

      if (lvl === "safe") {
        c.fillText("O2 : 20.9 %  (Chuan)", 10, 46);
        c.fillText("CO : 2.0 ppm (An toan)", 10, 66);
        c.fillText("CH4: 0.0 %LEL(Khong chay)", 10, 86);
        c.fillStyle = "#4ade80";
        c.fillText("TRANG THAI: AN TOAN [XANH]", 10, 112);
      } else if (lvl === "warn") {
        c.fillText("O2 : 19.1 %  (Giam nhe)", 10, 46);
        c.fillText("CO : 18.0 ppm(Chu y!)", 10, 66);
        c.fillText("CH4: 6.5 %LEL(Theo doi)", 10, 86);
        c.fillStyle = "#facc15";
        c.fillText("TRANG THAI: CANH BAO [VANG]", 10, 112);
      } else {
        c.fillText("O2 : 16.2 %  (NGAT THO!)", 10, 46);
        c.fillText("CO : 48.0 ppm(RAT DOC!)", 10, 66);
        c.fillText("CH4: 15.0 %LEL(NGUY NO!)", 10, 86);
        c.fillStyle = "#f87171";
        c.fillText("NGUY HIEM! COI HU DUMP!!", 10, 112);
      }
      oledTexture.needsUpdate = true;
    }

    // Nhãn 3D dạng Billboard Tag
    function createBillboardTag(text, colorHex = "#38bdf8") {
      const cv = document.createElement("canvas");
      cv.width = 512; cv.height = 110;
      const c = cv.getContext("2d");

      c.fillStyle = "rgba(15, 23, 42, 0.94)";
      c.strokeStyle = colorHex;
      c.lineWidth = 5;
      c.beginPath();
      c.roundRect(6, 6, 500, 98, 22);
      c.fill();
      c.stroke();

      c.fillStyle = "#ffffff";
      c.font = "bold 32px sans-serif";
      c.textAlign = "center";
      c.textBaseline = "middle";
      c.fillText(text, 256, 55);

      const tex = new THREE.CanvasTexture(cv);
      const mat = new THREE.SpriteMaterial({ map: tex, depthTest: false });
      const sprite = new THREE.Sprite(mat);
      sprite.renderOrder = 999;
      return sprite;
    }

    // =========================================================================
    // 4. MÔ HÌNH HÓA THIẾT BỊ ĐIỆN TỬ CHUẨN THẬT (PBR CAD QUALITY)
    // =========================================================================
    const componentMeshes = {};
    const floatingLabels = [];
    const sharedMeshTex = makeMeshTexture();

    // 1. CẢM BIẾN OXY DFROBOT GRAVITY I2C (O2)
    function buildO2Sensor(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bo mạch PCB màu đen mờ (Black Matte FR4)
      const pcbMat = new THREE.MeshStandardMaterial({ color: 0x18181b, roughness: 0.45, metalness: 0.2 });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.08, 1.4), pcbMat);
      pcb.castShadow = true;
      g.add(pcb);

      // 4 vòng mạ vàng ENIG tại 4 lỗ bắt ốc góc
      const goldMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.9, roughness: 0.25 });
      [[-0.52, -0.52], [0.52, -0.52], [-0.52, 0.52], [0.52, 0.52]].forEach(([x, z]) => {
        const ring = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.09, 16), goldMat);
        ring.position.set(x, 0, z);
        g.add(ring);
      });

      // Hộp cảm biến điện hóa tròn kim loại màu xanh nhôm ở đáy
      const cellMat = new THREE.MeshStandardMaterial({ color: 0x60a5fa, metalness: 0.85, roughness: 0.3 });
      const cell = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.45, 32), cellMat);
      cell.position.y = -0.25;
      cell.castShadow = true;
      g.add(cell);

      // Jack cắm trắng Gravity JST-PH 4-pin
      const jstMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.5 });
      const jst = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.35, 0.28), jstMat);
      jst.position.set(0, 0.18, 0.5);
      g.add(jst);

      // 4 chân tiếp xúc vàng trong jack
      for (let i = 0; i < 4; i++) {
        const p = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.015, 0.12), goldMat);
        p.rotation.x = Math.PI / 2;
        p.position.set(-0.18 + i * 0.12, 0.18, 0.55);
        g.add(p);
      }

      // Huy hiệu Gravity màu đỏ trên mặt bo
      const redBadge = new THREE.Mesh(new THREE.BoxGeometry(0.48, 0.02, 0.16), new THREE.MeshStandardMaterial({ color: 0xdc2626 }));
      redBadge.position.set(0, 0.05, -0.45);
      g.add(redBadge);

      return g;
    }

    // 2 & 3. CẢM BIẾN NUNG BÁN DẪN MQ (MQ-7 & MQ-4)
    function buildMQSensor(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bo mạch xanh dương đặc trưng của dòng cảm biến MQ
      const pcbMat = new THREE.MeshStandardMaterial({ color: 0x0a58ca, roughness: 0.4, metalness: 0.2 });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.08, 1.1), pcbMat);
      pcb.castShadow = true;
      g.add(pcb);

      // Vành khuyên chrome sáng bóng ở chân nắp chụp lưới
      const collarMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.95, roughness: 0.15 });
      const collar = new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.45, 0.1, 32), collarMat);
      collar.position.set(-0.35, 0.09, 0);
      g.add(collar);

      // Thân nắp chụp lưới thép kim loại không gỉ
      const domeMat = new THREE.MeshStandardMaterial({
        color: 0xcccccc,
        metalness: 0.88,
        roughness: 0.3,
        map: sharedMeshTex
      });
      const dome = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 0.55, 32), domeMat);
      dome.position.set(-0.35, 0.38, 0);
      g.add(dome);

      // Đỉnh vòm lưới
      const domeTop = new THREE.Mesh(new THREE.SphereGeometry(0.42, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2), domeMat);
      domeTop.position.set(-0.35, 0.65, 0);
      g.add(domeTop);

      // Chiết áp vi chỉnh màu xanh dương vuông (Bourns trimmer)
      const pot = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.3, 0.32), new THREE.MeshStandardMaterial({ color: 0x0284c7 }));
      pot.position.set(0.45, 0.2, 0.22);
      g.add(pot);

      // Ốc vít đồng vi chỉnh có rãnh trên đỉnh
      const screw = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.04, 16), new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.9 }));
      screw.position.set(0.45, 0.36, 0.22);
      g.add(screw);

      // Chip IC so sánh LM393 màu đen
      const ic = new THREE.Mesh(new THREE.BoxGeometry(0.35, 0.08, 0.22), new THREE.MeshStandardMaterial({ color: 0x1f2937 }));
      ic.position.set(0.42, 0.08, -0.22);
      g.add(ic);

      // 4 chân cắm bẻ góc 90 độ (A0, D0, GND, VCC)
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.9 });
      for (let i = 0; i < 4; i++) {
        const pin = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.35), pinMat);
        pin.rotation.z = Math.PI / 2;
        pin.position.set(0.92, 0.04, -0.28 + i * 0.18);
        g.add(pin);
      }

      return g;
    }

    // 4. CẢM BIẾN NHIỆT ĐỘ - ĐỘ ẨM DHT22 (AM2302)
    function buildDHT22Sensor(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Thân nhựa ABS trắng kem bo vát
      const whiteMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.5 });
      const body = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.45, 1.4), whiteMat);
      body.castShadow = true;
      g.add(body);

      // Ma trận khe tản gió dạng rãnh nổi
      const slotMat = new THREE.MeshBasicMaterial({ color: 0x334155 });
      for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 3; c++) {
          const slot = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.04, 0.08), slotMat);
          slot.position.set(-0.25 + c * 0.25, 0.23, -0.4 + r * 0.18);
          g.add(slot);
        }
      }

      // Tai treo bắt ốc ở đỉnh
      const ear = new THREE.Mesh(new THREE.BoxGeometry(0.48, 0.2, 0.35), whiteMat);
      ear.position.set(0, 0, -0.85);
      g.add(ear);

      const hole = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.22, 16), new THREE.MeshBasicMaterial({ color: 0x0f172a }));
      hole.position.set(0, 0, -0.85);
      g.add(hole);

      // 4 chân kim loại dài
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.9, roughness: 0.2 });
      for (let i = 0; i < 4; i++) {
        const pin = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.018, 0.65), pinMat);
        pin.rotation.x = Math.PI / 2;
        pin.position.set(-0.25 + i * 0.17, -0.05, 0.95);
        g.add(pin);
      }

      return g;
    }

    // 5 & 10. BO MẠCH ESP32 NODEMCU (SỬ DỤNG MODEL CAD GLB NGUYÊN BẢN)
    let esp32CadTemplate = null;

    function buildProceduralESP32(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.08, 2.9), new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.4 }));
      pcb.castShadow = true;
      g.add(pcb);

      const shield = new THREE.Mesh(new THREE.BoxGeometry(1.15, 0.16, 1.3), new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.88, roughness: 0.25 }));
      shield.position.set(0, 0.12, 0.15);
      g.add(shield);

      const usb = new THREE.Mesh(new THREE.BoxGeometry(0.48, 0.18, 0.35), new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.9 }));
      usb.position.set(0, 0.12, 1.35);
      g.add(usb);

      return g;
    }

    function buildESP32Board(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      if (esp32CadTemplate) {
        const clone = esp32CadTemplate.clone(true);
        // Tinh chỉnh góc xoay & tỉ lệ chuẩn
        clone.scale.set(1.5, 1.5, 1.5);
        clone.rotation.x = -Math.PI / 2;
        clone.position.y = 0.05;
        g.add(clone);
      } else {
        const fallback = buildProceduralESP32(comp);
        g.add(fallback);
      }

      return g;
    }

    // 6 & 8. MODULE CHUYỂN ĐỔI MAX485
    function buildMAX485Module(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bo mạch xanh dương
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.08, 1.6), new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.4 }));
      pcb.castShadow = true;
      g.add(pcb);

      // Chip DIP-8
      const ic = new THREE.Mesh(new THREE.BoxGeometry(0.45, 0.2, 0.65), new THREE.MeshStandardMaterial({ color: 0x111827 }));
      ic.position.set(0, 0.14, 0);
      g.add(ic);

      // Cầu đấu dây ốc vít màu xanh lá (Screw Terminal Block cho A & B)
      const term = new THREE.Mesh(new THREE.BoxGeometry(0.7, 0.45, 0.45), new THREE.MeshStandardMaterial({ color: 0x16a34a, roughness: 0.4 }));
      term.position.set(0, 0.25, 0.52);
      g.add(term);

      [-0.18, 0.18].forEach(x => {
        const s = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 0.05, 16), new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.9 }));
        s.position.set(x, 0.48, 0.52);
        g.add(s);
      });

      return g;
    }

    // 7. CỤM CÁP MẠNG CAT5E (CỤM 3 - 3 - 2)
    function buildCat5eModule(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      const sheath = new THREE.Mesh(new THREE.CylinderGeometry(0.24, 0.24, 1.8, 24), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.5 }));
      sheath.rotation.z = Math.PI / 2.3;
      sheath.castShadow = true;
      g.add(sheath);

      const wireColors = [
        0xf97316, 0xfed7aa, 0x78350f, // 3 Dương (+)
        0x15803d, 0xbbf7d0, 0x451a03, // 3 Mass (-)
        0x2563eb, 0xbfdbfe             // 2 Tín hiệu RS485 (A, B)
      ];

      wireColors.forEach((col, idx) => {
        const angle = (idx / 8) * Math.PI * 2;
        const w = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, 0.8), new THREE.MeshStandardMaterial({ color: col }));
        w.position.set(Math.cos(angle) * 0.22 - 0.7, Math.sin(angle) * 0.22, (idx % 2 === 0 ? 0.15 : -0.15));
        w.rotation.z = Math.PI / 2.8;
        g.add(w);
      });

      return g;
    }

    // 9. MODULE NGUỒN XUNG HẠ ÁP LM2596 (5.2V)
    function buildLM2596Module(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.08, 2.2), new THREE.MeshStandardMaterial({ color: 0x0369a1, roughness: 0.35 }));
      pcb.castShadow = true;
      g.add(pcb);

      // Cuộn cảm lõi xuyến quấn dây đồng ánh kim
      const choke = new THREE.Mesh(new THREE.CylinderGeometry(0.38, 0.38, 0.45, 24), new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.7 }));
      choke.position.set(-0.25, 0.25, -0.3);
      g.add(choke);

      const coil = new THREE.Mesh(new THREE.TorusGeometry(0.38, 0.06, 12, 24), new THREE.MeshStandardMaterial({ color: 0xd97706, metalness: 0.85, roughness: 0.2 }));
      coil.rotation.x = Math.PI / 2;
      coil.position.set(-0.25, 0.25, -0.3);
      g.add(coil);

      // 2 Tụ lọc nhôm
      [-0.75, 0.65].forEach(z => {
        const cap = new THREE.Mesh(new THREE.CylinderGeometry(0.24, 0.24, 0.55, 20), new THREE.MeshStandardMaterial({ color: 0x334155 }));
        cap.position.set(0.35, 0.3, z);
        g.add(cap);

        const capTop = new THREE.Mesh(new THREE.CylinderGeometry(0.23, 0.23, 0.05, 20), new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.9 }));
        capTop.position.set(0.35, 0.58, z);
        g.add(capTop);
      });

      // Chiết áp 3296 chỉnh áp
      const pot = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.45, 0.55), new THREE.MeshStandardMaterial({ color: 0x2563eb }));
      pot.position.set(-0.35, 0.26, 0.55);
      g.add(pot);

      const screw = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.08, 16), new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.95 }));
      screw.position.set(-0.35, 0.5, 0.7);
      g.add(screw);

      return g;
    }

    // 11. MÀN HÌNH OLED 0.96" SSD1306
    function buildOLEDModule(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.08, 1.4), new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.35 }));
      pcb.castShadow = true;
      g.add(pcb);

      const screen = new THREE.Mesh(new THREE.BoxGeometry(1.26, 0.04, 1.05), new THREE.MeshBasicMaterial({ map: oledTexture }));
      screen.position.set(0, 0.07, 0.1);
      g.add(screen);

      return g;
    }

    // 12. CÒI HÚ & 3 ĐÈN LED
    let ledGreenMesh, ledYellowMesh, ledRedMesh;
    let alarmPointLight;

    function buildAlarmModule(comp) {
      const g = new THREE.Group();
      g.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      const base = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.12, 1.2), new THREE.MeshStandardMaterial({ color: 0x1e293b }));
      base.castShadow = true;
      g.add(base);

      // Còi hú đen tròn
      const buzzer = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 0.45, 32), new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.5 }));
      buzzer.position.set(-0.4, 0.28, 0);
      g.add(buzzer);

      const hole = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.06, 16), new THREE.MeshBasicMaterial({ color: 0x000000 }));
      hole.position.set(-0.4, 0.51, 0);
      g.add(hole);

      // 3 LED vòm 5mm
      const createLed = (colorHex, x, z) => {
        const mat = new THREE.MeshStandardMaterial({
          color: colorHex,
          emissive: colorHex,
          emissiveIntensity: 0.35,
          roughness: 0.2,
          transparent: true,
          opacity: 0.95
        });
        const dome = new THREE.Mesh(new THREE.SphereGeometry(0.14, 16, 16, 0, Math.PI * 2, 0, Math.PI / 2), mat);
        dome.position.set(x, 0.24, z);
        const col = new THREE.Mesh(new THREE.CylinderGeometry(0.14, 0.14, 0.16, 16), mat);
        col.position.set(x, 0.14, z);
        g.add(dome);
        g.add(col);
        return mat;
      };

      ledRedMesh = createLed(0xef4444, 0.35, -0.32);
      ledYellowMesh = createLed(0xf59e0b, 0.35, 0.0);
      ledGreenMesh = createLed(0x10b981, 0.35, 0.32);

      alarmPointLight = new THREE.PointLight(0x10b981, 1.6, 4.5);
      alarmPointLight.position.set(0.35, 0.5, 0.32);
      g.add(alarmPointLight);

      return g;
    }

    // =========================================================================
    // 5. NẠP MODEL CAD THẬT VÀ KHỞI TẠO SCENE
    // =========================================================================
    function initAllComponents() {
      COMPONENTS.forEach(comp => {
        let obj;
        switch(comp.id) {
          case "o2_sensor": obj = buildO2Sensor(comp); break;
          case "mq7_sensor": obj = buildMQSensor(comp); break;
          case "mq4_sensor": obj = buildMQSensor(comp); break;
          case "dht22_sensor": obj = buildDHT22Sensor(comp); break;
          case "esp32_slave": obj = buildESP32Board(comp); break;
          case "max485_slave": obj = buildMAX485Module(comp); break;
          case "cable_cat5e": obj = buildCat5eModule(comp); break;
          case "max485_master": obj = buildMAX485Module(comp); break;
          case "lm2596": obj = buildLM2596Module(comp); break;
          case "esp32_master": obj = buildESP32Board(comp); break;
          case "oled_display": obj = buildOLEDModule(comp); break;
          case "alarm_system": obj = buildAlarmModule(comp); break;
          default: obj = new THREE.Group();
        }

        obj.userData = { id: comp.id, name: comp.name };
        scene.add(obj);
        componentMeshes[comp.id] = obj;

        // Hitbox click nhạy
        const hitBox = new THREE.Mesh(new THREE.BoxGeometry(2.0, 1.4, 2.0), new THREE.MeshBasicMaterial({ visible: false }));
        hitBox.userData = { id: comp.id };
        obj.add(hitBox);

        // Nhãn nổi 3D
        const label = createBillboardTag(comp.name, comp.color);
        label.position.set(comp.pos.x, comp.pos.y + 0.95, comp.pos.z);
        label.scale.set(1.9, 0.45, 1.0);
        scene.add(label);
        floatingLabels.push(label);
      });

      updateOledDisplay("safe");
      createAllWires();
      selectComponent("o2_sensor");
    }

    // Nạp model GLB CAD của ESP32 nếu có
    if (window.ESP32_GLB_BASE64) {
      try {
        const binStr = window.atob(window.ESP32_GLB_BASE64);
        const len = binStr.length;
        const bytes = new Uint8Array(len);
        for (let i = 0; i < len; i++) bytes[i] = binStr.charCodeAt(i);

        const gltfLoader = new THREE.GLTFLoader();
        gltfLoader.parse(bytes.buffer, '', function(gltf) {
          esp32CadTemplate = gltf.scene;
          initAllComponents();
        }, function(err) {
          console.warn("Parse GLB failed, using fallback:", err);
          initAllComponents();
        });
      } catch(e) {
        console.warn("Init GLB error:", e);
        initAllComponents();
      }
    } else {
      initAllComponents();
    }

    // =========================================================================
    // 6. XÂY DỰNG ĐƯỜNG DÂY NỐI VÀ HẠT DÒNG ĐIỆN
    // =========================================================================
    const wireCurves = [];

    function createAllWires() {
      // Dây Nguồn Dương (Cam)
      createCurvedWire(new THREE.Vector3(2.3, 1.3, 1.9), new THREE.Vector3(-1.8, -1.1, 0.0), 0xf97316, 0.045, "wire_power");
      // Dây Mass GND (Xanh Lá)
      createCurvedWire(new THREE.Vector3(2.3, 1.1, 1.9), new THREE.Vector3(-1.8, -1.3, 0.0), 0x10b981, 0.045, "wire_gnd");
      // Dây Tín Hiệu RS485 (Xanh Dương)
      createCurvedWire(new THREE.Vector3(2.3, 1.3, 0.0), new THREE.Vector3(-0.3, -1.1, 0.0), 0x06b6d4, 0.035, "wire_rs485");

      // Dây nội bộ dưới đáy
      createCurvedWire(new THREE.Vector3(-3.8, -1.1, 2.1), new THREE.Vector3(-1.8, -1.1, 0.0), 0x38bdf8, 0.025, "wire_o2");
      createCurvedWire(new THREE.Vector3(-3.8, -1.1, 0.5), new THREE.Vector3(-1.8, -1.1, 0.0), 0xf97316, 0.025, "wire_mq7");
      createCurvedWire(new THREE.Vector3(-3.8, -1.1, -1.1), new THREE.Vector3(-1.8, -1.1, 0.0), 0xeab308, 0.025, "wire_mq4");
      createCurvedWire(new THREE.Vector3(-3.8, -1.1, -2.5), new THREE.Vector3(-1.8, -1.1, 0.0), 0x3b82f6, 0.025, "wire_dht22");
      createCurvedWire(new THREE.Vector3(-1.8, -1.1, 0.0), new THREE.Vector3(-0.3, -1.1, 0.0), 0xa855f7, 0.03, "wire_uart_slave");

      // Dây nội bộ mặt đất
      createCurvedWire(new THREE.Vector3(4.0, 1.3, 0.0), new THREE.Vector3(2.3, 1.3, 0.0), 0xa855f7, 0.03, "wire_uart_master");
      createCurvedWire(new THREE.Vector3(4.0, 1.3, 0.0), new THREE.Vector3(4.0, 1.3, 1.9), 0x38bdf8, 0.025, "wire_oled");
      createCurvedWire(new THREE.Vector3(4.0, 1.3, 0.0), new THREE.Vector3(4.0, 1.3, -1.9), 0xef4444, 0.03, "wire_alarm");
    }

    function createCurvedWire(start, end, colorHex, radius, wireId) {
      const mid = new THREE.Vector3().addVectors(start, end).multiplyScalar(0.5);
      mid.y += (start.y > 0 ? 0.65 : -0.25);

      const curve = new THREE.QuadraticBezierCurve3(start, mid, end);
      const tubeGeo = new THREE.TubeGeometry(curve, 32, radius, 8, false);
      const tubeMat = new THREE.MeshStandardMaterial({
        color: colorHex,
        roughness: 0.35,
        metalness: 0.3,
        emissive: colorHex,
        emissiveIntensity: 0.25
      });
      const tubeMesh = new THREE.Mesh(tubeGeo, tubeMat);
      scene.add(tubeMesh);

      wireCurves.push({
        id: wireId,
        curve: curve,
        mesh: tubeMesh,
        particles: createParticlesAlongCurve(curve)
      });
    }

    function createParticlesAlongCurve(curve) {
      const count = 16;
      const geo = new THREE.SphereGeometry(0.065, 8, 8);
      const mat = new THREE.MeshBasicMaterial({ color: 0xffffff });
      const group = new THREE.Group();

      const particles = [];
      for (let i = 0; i < count; i++) {
        const p = new THREE.Mesh(geo, mat);
        p.visible = false;
        group.add(p);
        particles.push({ mesh: p, offset: i / count });
      }
      scene.add(group);
      return { group, particles };
    }

    // =========================================================================
    // 7. ÂM THANH CÒI HÚ WEB AUDIO API
    // =========================================================================
    let audioCtx = null;
    let isSoundMuted = false;

    function playBuzzerBeep(freq = 2400, duration = 0.18) {
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

    // =========================================================================
    // 8. LOGIC GIAO DIỆN & TƯƠNG TÁC
    // =========================================================================
    const compListContainer = document.getElementById("comp-list");
    const detailBody = document.getElementById("detail-body");
    const detailCategory = document.getElementById("detail-category");
    const btnPower = document.getElementById("btn-power");
    const powerText = document.getElementById("power-text");
    const flowDot = document.getElementById("flow-dot");
    const flowStatusText = document.getElementById("flow-status-text");
    const flowDesc = document.getElementById("flow-desc");
    const btnLabels = document.getElementById("btn-labels");
    const labelText = document.getElementById("label-text");
    const btnSound = document.getElementById("btn-sound");
    const soundText = document.getElementById("sound-text");

    let isPowerOn = false;
    let currentAlarmLevel = "safe";
    let showLabels = true;

    // Render danh sách bên trái
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

      document.querySelectorAll(".comp-item").forEach(el => el.classList.remove("active"));
      const selectedItem = document.getElementById(`item-${comp.id}`);
      if (selectedItem) selectedItem.classList.add("active");

      // Scale hiệu ứng nhẹ
      Object.keys(componentMeshes).forEach(k => {
        const g = componentMeshes[k];
        if (k === comp.id) {
          g.scale.set(1.15, 1.15, 1.15);
        } else {
          g.scale.set(1, 1, 1);
        }
      });

      // Lướt camera mượt mà
      const targetPos = new THREE.Vector3(comp.pos.x, comp.pos.y, comp.pos.z);
      controls.target.lerp(targetPos, 0.55);

      // Render nội dung bảng thông tin bên phải
      detailCategory.textContent = comp.group;
      detailBody.innerHTML = `
        <div class="comp-badge"><i class="fa-solid ${comp.icon}"></i> ${comp.badge}</div>
        <div class="comp-title-large">${comp.name}</div>
        <div style="font-size: 0.82rem; color: #94a3b8; margin-top: -6px;">${comp.sub}</div>

        <div class="pin-mapping-box">
          <h4><i class="fa-solid fa-arrows-split-up-and-left"></i> Sơ đồ chân kết nối với ESP32</h4>
          ${comp.pins.map(p => `
            <div class="pin-row">
              <span class="pin-from"><i class="fa-solid fa-plug"></i> ${p.from}</span>
              <span class="pin-arrow"><i class="fa-solid fa-arrow-right"></i></span>
              <span class="pin-to">${p.to}</span>
            </div>
            <div style="font-size: 0.72rem; color: #64748b; margin: -2px 0 6px 12px;">• ${p.note}</div>
          `).join('')}
        </div>

        <div class="explanation-card">
          <h4><i class="fa-solid fa-circle-question"></i> ${comp.why}</h4>
          <p>${comp.whyContent}</p>
          <div class="highlight-tip">
            <strong>Ghi nhớ cốt lõi:</strong> Thiết kế phân định rõ ràng giữa các kênh phần cứng (UART2, I2C, ADC1) giúp hệ thống không bao giờ bị nghẽn sóng hay gián đoạn.
          </div>
          <div class="physicsTip">
            ${comp.physicsTip}
          </div>
        </div>
      `;
    }

    // Toggle Nhãn 3D
    btnLabels.onclick = () => {
      showLabels = !showLabels;
      floatingLabels.forEach(lbl => lbl.visible = showLabels);
      labelText.textContent = showLabels ? "Tắt Nhãn 3D" : "Bật Nhãn 3D";
    };

    // Toggle Âm thanh
    btnSound.onclick = () => {
      isSoundMuted = !isSoundMuted;
      btnSound.classList.toggle("muted", isSoundMuted);
      soundText.textContent = isSoundMuted ? "Âm Thanh: TẮT" : "Âm Thanh: BẬT";
    };

    // Nút Bật/Tắt nguồn
    btnPower.onclick = () => {
      isPowerOn = !isPowerOn;
      if (isPowerOn) {
        btnPower.classList.add("active");
        powerText.textContent = "NGUỒN ĐANG BẬT (5.2V)";
        flowDot.classList.add("active");
        flowStatusText.textContent = "Dòng điện đang chạy từ Pin -> LM2596 (5.2V) -> Cụm 3-3-2 -> Cảm Biến";
        flowDesc.textContent = "Hạt electron phát sáng chuyển động dọc theo cáp nguồn và tín hiệu RS485";
        wireCurves.forEach(w => w.particles.particles.forEach(p => p.mesh.visible = true));
      } else {
        btnPower.classList.remove("active");
        powerText.textContent = "BẬT NGUỒN PIN";
        flowDot.classList.remove("active");
        flowStatusText.textContent = "Nguồn đang tắt (Chưa có dòng điện)";
        flowDesc.textContent = "Bấm 'BẬT NGUỒN PIN' để kích hoạt dòng điện và truyền nhận RS485";
        wireCurves.forEach(w => w.particles.particles.forEach(p => p.mesh.visible = false));
      }
    };

    // 3 Mức cảnh báo
    const btnSafe = document.getElementById("btn-lvl-safe");
    const btnWarn = document.getElementById("btn-lvl-warn");
    const btnDang = document.getElementById("btn-lvl-dang");

    function setAlarmLevel(lvl) {
      currentAlarmLevel = lvl;
      btnSafe.className = "btn-level" + (lvl === "safe" ? " active-safe" : "");
      btnWarn.className = "btn-level" + (lvl === "warn" ? " active-warn" : "");
      btnDang.className = "btn-level" + (lvl === "dang" ? " active-dang" : "");

      updateOledDisplay(lvl);

      if (lvl === "safe") {
        ledGreenMesh.emissiveIntensity = 1.6;
        ledYellowMesh.emissiveIntensity = 0.1;
        ledRedMesh.emissiveIntensity = 0.1;
        alarmPointLight.color.setHex(0x10b981);
        alarmPointLight.intensity = 1.8;
      } else if (lvl === "warn") {
        ledGreenMesh.emissiveIntensity = 0.1;
        ledYellowMesh.emissiveIntensity = 1.8;
        ledRedMesh.emissiveIntensity = 0.1;
        alarmPointLight.color.setHex(0xf59e0b);
        alarmPointLight.intensity = 2.0;
        playBuzzerBeep(1800, 0.12);
      } else {
        ledGreenMesh.emissiveIntensity = 0.1;
        ledYellowMesh.emissiveIntensity = 0.1;
        ledRedMesh.emissiveIntensity = 2.0;
        alarmPointLight.color.setHex(0xef4444);
        alarmPointLight.intensity = 2.5;
        playBuzzerBeep(2600, 0.25);
      }
    }

    btnSafe.onclick = () => setAlarmLevel("safe");
    btnWarn.onclick = () => setAlarmLevel("warn");
    btnDang.onclick = () => setAlarmLevel("dang");

    document.getElementById("btn-reset-view").onclick = () => {
      camera.position.set(0, 9.0, 13.0);
      controls.target.set(0, 0, 0);
    };

    // Click chọn trực tiếp trên không gian 3D
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    window.addEventListener("click", (e) => {
      if (e.target.closest(".sidebar-left") || e.target.closest(".sidebar-right") || e.target.closest("header") || e.target.closest(".bottom-bar") || e.target.closest("#modal-schematic")) {
        return;
      }
      mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
      raycaster.setFromCamera(mouse, camera);

      const targetList = [];
      Object.values(componentMeshes).forEach(group => {
        group.traverse(child => {
          if (child.isMesh) targetList.push(child);
        });
      });

      const intersects = raycaster.intersectObjects(targetList, false);
      if (intersects.length > 0) {
        let obj = intersects[0].object;
        while (obj && (!obj.userData || !obj.userData.id)) {
          obj = obj.parent;
        }
        if (obj && obj.userData && obj.userData.id) {
          selectComponent(obj.userData.id);
        }
      }
    });

    // =========================================================================
    // 9. VÒNG LẶP RENDER HOẠT HÌNH 3D (ANIMATION LOOP)
    // =========================================================================
    const clock = new THREE.Clock();
    let lastBeepTime = 0;

    function animate() {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();
      const time = clock.getElapsedTime();

      // Di chuyển các hạt dòng điện khi bật nguồn
      if (isPowerOn) {
        wireCurves.forEach(w => {
          const speed = (w.id === "wire_power" || w.id === "wire_gnd") ? 0.35 : 0.55;
          w.particles.particles.forEach(p => {
            p.offset = (p.offset + delta * speed) % 1.0;
            const pt = w.curve.getPoint(p.offset);
            p.mesh.position.copy(pt);
          });
        });

        // Chớp nháy báo động nguy hiểm
        if (currentAlarmLevel === "dang") {
          const isBlink = Math.sin(time * 14) > 0;
          ledRedMesh.emissiveIntensity = isBlink ? 2.5 : 0.2;
          alarmPointLight.intensity = isBlink ? 3.0 : 0.2;

          if (isBlink && time - lastBeepTime > 0.35) {
            playBuzzerBeep(2600, 0.15);
            lastBeepTime = time;
          }
        }
      }

      controls.update();
      renderer.render(scene, camera);
    }

    animate();

    window.addEventListener("resize", () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // Modal Sơ đồ Mạch 2D
    const modalSchematic = document.getElementById("modal-schematic");
    document.getElementById("btn-schematic").onclick = () => modalSchematic.style.display = "flex";
    document.getElementById("btn-close-modal").onclick = () => modalSchematic.style.display = "none";
    modalSchematic.onclick = (e) => { if (e.target === modalSchematic) modalSchematic.style.display = "none"; };
    window.addEventListener("keydown", (e) => { if (e.key === "Escape") modalSchematic.style.display = "none"; });
  </script>

  <!-- MODAL SƠ ĐỒ MẠCH 2D -->
  <div id="modal-schematic" style="display: none; position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(7, 10, 19, 0.88); backdrop-filter: blur(16px); z-index: 100; justify-content: center; align-items: center; padding: 30px;">
    <div style="background: #0f172a; border: 1px solid #334155; border-radius: 16px; max-width: 90vw; max-height: 90vh; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.8);">
      <div style="padding: 14px 20px; border-bottom: 1px solid #1e293b; display: flex; justify-content: space-between; align-items: center;">
        <h3 style="font-size: 1.1rem; color: #38bdf8; display: flex; align-items: center; gap: 8px;">
          <i class="fa-solid fa-diagram-project"></i> Sơ Đồ Nguyên Lý Mạch Điện 2D Chi Tiết
        </h3>
        <button id="btn-close-modal" style="background: none; border: none; color: #94a3b8; font-size: 1.4rem; cursor: pointer;">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div style="padding: 16px; overflow: auto; text-align: center;">
        <img src="../images/hinh2_so_do_mach_dien.png" alt="Sơ đồ mạch điện" style="max-width: 100%; max-height: 75vh; border-radius: 8px; border: 1px solid #334155;">
        <p style="font-size: 0.82rem; color: #94a3b8; margin-top: 10px;">
          Hình 2: Sơ đồ nối dây chi tiết giữa Khối Không Gian Kín (Slave) và Khối Mặt Đất (Master) qua cụm cáp Cat5e 3 - 3 - 2
        </p>
      </div>
    </div>
  </div>
</body>
</html>
'''

output_path = r"c:\Users\Admin\Downloads\All-Project\canhbaokhi\mo_phong_3d_noi_day\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Successfully generated updated 3D simulation v2 at: {output_path}")
