# -*- coding: utf-8 -*-
"""
Script to generate the photorealistic 3D wiring simulation index.html
with exact physical appearances of sensors and boards.
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mô Phỏng 3D Thiết Bị Thật & Nối Dây - Cảnh Báo Khí Độc</title>
  <!-- Three.js & OrbitControls -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg-dark: #070a13;
      --panel-bg: rgba(13, 20, 36, 0.92);
      --panel-border: #1e293b;
      --cyan: #06b6d4;
      --cyan-glow: rgba(6, 182, 212, 0.4);
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
      background: var(--bg-dark);
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
      backdrop-filter: blur(14px);
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
      backdrop-filter: blur(14px);
      transition: all 0.25s ease;
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
      backdrop-filter: blur(16px);
      z-index: 10;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5);
      overflow: hidden;
    }

    .panel-hdr {
      padding: 14px 16px;
      border-bottom: 1px solid var(--panel-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 700;
      font-size: 0.88rem;
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
      padding: 9px 12px;
      border-radius: 10px;
      background: rgba(30, 41, 59, 0.35);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .comp-item:hover {
      background: rgba(30, 41, 59, 0.8);
      border-color: rgba(56, 189, 248, 0.3);
      transform: translateX(3px);
    }

    .comp-item.active {
      background: linear-gradient(90deg, rgba(6, 182, 212, 0.15), rgba(59, 130, 246, 0.1));
      border-color: var(--cyan);
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.25);
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
      backdrop-filter: blur(16px);
      z-index: 10;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5);
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
      backdrop-filter: blur(16px);
      z-index: 10;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
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
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(51, 65, 85, 0.5);
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 0.75rem;
      color: var(--text-muted);
      pointer-events: none;
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
    <i class="fa-solid fa-mouse"></i> Chuột trái: Xoay 360° | Chuột phải: Kéo dời | Cuộn chuột: Phóng to/Thu nhỏ | Click trực tiếp vào linh kiện 3D để xem phân tích chân
  </div>

  <!-- SIDEBAR TRÁI: DANH SÁCH LINH KIỆN -->
  <div class="sidebar-left">
    <div class="panel-hdr">
      <span><i class="fa-solid fa-layer-group"></i> LINH KIỆN HỆ THỐNG</span>
      <span style="font-size: 0.72rem; color: var(--text-muted);">11 Thiết bị thật</span>
    </div>
    <div class="component-list" id="comp-list">
      <!-- Sẽ được render bằng Javascript -->
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
    // 2. KHỞI TẠO THREE.JS VÀ KHÔNG GIAN 3D
    // =========================================================================
    const container = document.getElementById("canvas-container");
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x070a13);
    scene.fog = new THREE.FogExp2(0x070a13, 0.038);

    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
    camera.position.set(0, 8.5, 12);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxPolarAngle = Math.PI / 2 + 0.05;
    controls.minDistance = 2.5;
    controls.maxDistance = 26;
    controls.target.set(0, 0, 0);

    // ÁNH SÁNG STUDIO CHUYÊN NGHIỆP
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.85);
    scene.add(ambientLight);

    const mainLight = new THREE.DirectionalLight(0xffffff, 1.3);
    mainLight.position.set(6, 14, 8);
    mainLight.castShadow = true;
    mainLight.shadow.mapSize.width = 2048;
    mainLight.shadow.mapSize.height = 2048;
    scene.add(mainLight);

    const blueRimLight = new THREE.PointLight(0x38bdf8, 2.2, 18);
    blueRimLight.position.set(-4, 3, 3);
    scene.add(blueRimLight);

    const cyanRimLight = new THREE.PointLight(0x818cf8, 2.0, 18);
    cyanRimLight.position.set(4, 3, -3);
    scene.add(cyanRimLight);

    // NỀN CÔNG NGHỆ LAB VỚI LƯỚI TỌA ĐỘ
    const gridHelper = new THREE.GridHelper(32, 32, 0x1e293b, 0x0f172a);
    gridHelper.position.y = -2.2;
    scene.add(gridHelper);

    // HAI BỆ ĐỠ THIẾT BỊ
    // Bệ dưới đáy (Khối Không Gian Kín - Màu than tím đậm)
    const baseSlaveGeo = new THREE.BoxGeometry(5.6, 0.4, 6.8);
    const baseSlaveMat = new THREE.MeshStandardMaterial({
      color: 0x141829,
      roughness: 0.6,
      metalness: 0.25
    });
    const baseSlave = new THREE.Mesh(baseSlaveGeo, baseSlaveMat);
    baseSlave.position.set(-2.8, -1.6, 0.0);
    baseSlave.receiveShadow = true;
    scene.add(baseSlave);

    // Bệ trên mặt đất (Khối Master - Màu xanh thép)
    const baseMasterGeo = new THREE.BoxGeometry(5.2, 0.4, 6.8);
    const baseMasterMat = new THREE.MeshStandardMaterial({
      color: 0x0f1f33,
      roughness: 0.6,
      metalness: 0.25
    });
    const baseMaster = new THREE.Mesh(baseMasterGeo, baseMasterMat);
    baseMaster.position.set(3.4, 0.8, 0.0);
    baseMaster.receiveShadow = true;
    scene.add(baseMaster);

    // Nhãn 3D tên 2 bệ đỡ
    const platformLabel1 = createTextSprite("KHỐI ĐÁY KHÔNG GIAN KÍN (SLAVE)", "#818cf8");
    platformLabel1.position.set(-2.8, -1.2, 3.2);
    platformLabel1.scale.set(3.2, 0.65, 1);
    scene.add(platformLabel1);

    const platformLabel2 = createTextSprite("KHỐI TRÊN MẶT ĐẤT (MASTER)", "#38bdf8");
    platformLabel2.position.set(3.4, 1.2, 3.2);
    platformLabel2.scale.set(3.0, 0.65, 1);
    scene.add(platformLabel2);

    // =========================================================================
    // 3. HÀM TẠO TEXTURE PROCEDURAL BẰNG HTML CANVAS
    // =========================================================================

    // Texture lưới thép không gỉ cho cảm biến khí MQ
    function makeStainlessSteelMeshTexture() {
      const canvas = document.createElement("canvas");
      canvas.width = 256;
      canvas.height = 256;
      const ctx = canvas.getContext("2d");

      ctx.fillStyle = "#8a939d";
      ctx.fillRect(0, 0, 256, 256);

      // Lưới đan chéo
      ctx.strokeStyle = "#47515b";
      ctx.lineWidth = 2.5;
      for (let i = 0; i < 256; i += 8) {
        ctx.beginPath();
        ctx.moveTo(i, 0);
        ctx.lineTo(i, 256);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(0, i);
        ctx.lineTo(256, i);
        ctx.stroke();
      }

      // Đốm kim loại phản chiếu ánh sáng
      ctx.fillStyle = "#d1d5db";
      for (let x = 2; x < 256; x += 8) {
        for (let y = 2; y < 256; y += 8) {
          ctx.fillRect(x, y, 4, 4);
        }
      }

      const texture = new THREE.CanvasTexture(canvas);
      texture.wrapS = THREE.RepeatWrapping;
      texture.wrapT = THREE.RepeatWrapping;
      texture.repeat.set(4, 2);
      return texture;
    }

    // Texture mặt trên cảm biến Oxy DFRobot Gravity
    function makeO2SensorTexture() {
      const canvas = document.createElement("canvas");
      canvas.width = 512;
      canvas.height = 512;
      const ctx = canvas.getContext("2d");

      // Mặt bo màu đen mờ
      ctx.fillStyle = "#121214";
      ctx.fillRect(0, 0, 512, 512);

      // Vòng đồng 4 lỗ ốc ở 4 góc
      ctx.strokeStyle = "#eab308";
      ctx.lineWidth = 8;
      const corners = [[50, 50], [462, 50], [50, 462], [462, 462]];
      corners.forEach(([cx, cy]) => {
        ctx.beginPath();
        ctx.arc(cx, cy, 32, 0, Math.PI * 2);
        ctx.stroke();
        ctx.fillStyle = "#070a13";
        ctx.beginPath();
        ctx.arc(cx, cy, 20, 0, Math.PI * 2);
        ctx.fill();
      });

      // Logo Gravity đỏ
      ctx.fillStyle = "#dc2626";
      ctx.fillRect(160, 40, 192, 45);
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 26px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("Gravity", 256, 72);

      // Chữ IIC & chân I2C
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 22px monospace";
      ctx.fillText("IIC O2 SENSOR", 256, 120);

      ctx.fillStyle = "#fbbf24";
      ctx.font = "bold 20px monospace";
      ctx.fillText("SDA  SCL  GND  VCC", 256, 470);

      // Đường mạch in mạ vàng
      ctx.strokeStyle = "rgba(234, 179, 8, 0.4)";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(100, 200); ctx.lineTo(200, 200); ctx.lineTo(256, 256);
      ctx.moveTo(412, 200); ctx.lineTo(312, 200); ctx.lineTo(256, 256);
      ctx.stroke();

      return new THREE.CanvasTexture(canvas);
    }

    // Texture mặt trước cảm biến DHT22 (Aosong AM2302)
    function makeDHT22Texture() {
      const canvas = document.createElement("canvas");
      canvas.width = 256;
      canvas.height = 384;
      const ctx = canvas.getContext("2d");

      ctx.fillStyle = "#f8fafc";
      ctx.fillRect(0, 0, 256, 384);

      // Khe tản gió cảm biến (3 cột x 6 hàng khe hở)
      ctx.fillStyle = "#334155";
      for (let row = 0; row < 6; row++) {
        for (let col = 0; col < 3; col++) {
          const x = 50 + col * 55;
          const y = 80 + row * 34;
          // Vẽ khe bo tròn
          ctx.beginPath();
          ctx.roundRect(x, y, 42, 18, 6);
          ctx.fill();
        }
      }

      // Khắc laser chữ ASAIR AM2302
      ctx.fillStyle = "#64748b";
      ctx.font = "bold 16px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("ASAIR AM2302", 128, 320);
      ctx.font = "12px monospace";
      ctx.fillText("SN: 202610DHT-OK", 128, 342);

      return new THREE.CanvasTexture(canvas);
    }

    // Texture mặt kim loại ESP-WROOM-32
    function makeEspShieldTexture() {
      const canvas = document.createElement("canvas");
      canvas.width = 512;
      canvas.height = 512;
      const ctx = canvas.getContext("2d");

      // Nền kim loại phay xước
      ctx.fillStyle = "#d1d5db";
      ctx.fillRect(0, 0, 512, 512);

      // Viền vát cạnh
      ctx.strokeStyle = "#9ca3af";
      ctx.lineWidth = 12;
      ctx.strokeRect(6, 6, 500, 500);

      // Chữ khắc laser ESPRESSIF & ESP32
      ctx.fillStyle = "#374151";
      ctx.textAlign = "center";
      ctx.font = "bold 38px sans-serif";
      ctx.fillText("ESPRESSIF", 256, 120);

      ctx.font = "bold 64px sans-serif";
      ctx.fillText("ESP-WROOM-32", 256, 210);

      ctx.font = "20px monospace";
      ctx.fillText("FCC ID: 2AC7Z-ESPWROOM32", 256, 280);
      ctx.fillText("Wi-Fi & Bluetooth 4.2 BLE", 256, 320);

      // Biểu tượng CE & Wi-Fi
      ctx.font = "bold 42px sans-serif";
      ctx.fillText("CE 1588", 256, 410);

      return new THREE.CanvasTexture(canvas);
    }

    // Texture ăng-ten PCB meander mạ vàng của ESP32
    function makeAntennaTexture() {
      const canvas = document.createElement("canvas");
      canvas.width = 256;
      canvas.height = 128;
      const ctx = canvas.getContext("2d");

      ctx.fillStyle = "#1e293b";
      ctx.fillRect(0, 0, 256, 128);

      // Vệt ăng-ten vàng uốn lượn (Meandering Inverted-F)
      ctx.strokeStyle = "#fbbf24";
      ctx.lineWidth = 8;
      ctx.beginPath();
      ctx.moveTo(20, 100);
      ctx.lineTo(20, 25);
      ctx.lineTo(60, 25);
      ctx.lineTo(60, 95);
      ctx.lineTo(100, 95);
      ctx.lineTo(100, 25);
      ctx.lineTo(140, 25);
      ctx.lineTo(140, 95);
      ctx.lineTo(180, 95);
      ctx.lineTo(180, 25);
      ctx.lineTo(230, 25);
      ctx.stroke();

      return new THREE.CanvasTexture(canvas);
    }

    // Dynamic Canvas Texture cho Màn Hình OLED SSD1306
    let oledCanvas = document.createElement("canvas");
    oledCanvas.width = 256;
    oledCanvas.height = 128;
    let oledTexture = new THREE.CanvasTexture(oledCanvas);

    function updateOledDisplay(lvl) {
      const ctx = oledCanvas.getContext("2d");
      ctx.fillStyle = "#030712";
      ctx.fillRect(0, 0, 256, 128);

      // Khung viền màn hình
      ctx.strokeStyle = "#1e3a8a";
      ctx.lineWidth = 2;
      ctx.strokeRect(2, 2, 252, 124);

      // Tiêu đề vàng OLED
      ctx.fillStyle = "#facc15";
      ctx.font = "bold 13px monospace";
      ctx.fillText("CANH BAO KHONG GIAN KIN", 10, 20);

      ctx.strokeStyle = "#334155";
      ctx.beginPath();
      ctx.moveTo(5, 26); ctx.lineTo(251, 26);
      ctx.stroke();

      // Thông số màu xanh Cyan OLED
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 13px monospace";

      if (lvl === "safe") {
        ctx.fillText("O2 : 20.9 %  (Chuan)", 10, 46);
        ctx.fillText("CO : 2.0 ppm (An toan)", 10, 66);
        ctx.fillText("CH4: 0.0 %LEL(Khong chay)", 10, 86);
        ctx.fillStyle = "#4ade80";
        ctx.fillText("TRANG THAI: AN TOAN [XANH]", 10, 112);
      } else if (lvl === "warn") {
        ctx.fillText("O2 : 19.1 %  (Dang giam)", 10, 46);
        ctx.fillText("CO : 18.0 ppm(Chu y!)", 10, 66);
        ctx.fillText("CH4: 6.5 %LEL(Theo doi)", 10, 86);
        ctx.fillStyle = "#facc15";
        ctx.fillText("TRANG THAI: CANH BAO [VANG]", 10, 112);
      } else {
        ctx.fillText("O2 : 16.2 %  (NGAT THO!)", 10, 46);
        ctx.fillText("CO : 48.0 ppm(RAT DOC!)", 10, 66);
        ctx.fillText("CH4: 15.0 %LEL(NGUY NO!)", 10, 86);
        ctx.fillStyle = "#f87171";
        ctx.fillText("NGUY HIEM! COI HU DUMP!!", 10, 112);
      }

      oledTexture.needsUpdate = true;
    }

    // =========================================================================
    // 4. XÂY DỰNG MÔ HÌNH 3D CHI TIẾT TỪNG LINH KIỆN THẬT
    // =========================================================================
    const componentMeshes = {}; // Lưu trữ để raycasting và quản lý
    const meshTextureShared = makeStainlessSteelMeshTexture();
    const espShieldTex = makeEspShieldTexture();
    const espAntennaTex = makeAntennaTexture();
    const dht22Tex = makeDHT22Texture();
    const o2Tex = makeO2SensorTexture();

    // 1. CẢM BIẾN OXY DFROBOT GRAVITY (O2)
    function buildO2Sensor(comp) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bo mạch PCB màu đen
      const pcbMat = new THREE.MeshStandardMaterial({
        color: 0x18181b,
        roughness: 0.35,
        metalness: 0.2,
        map: o2Tex
      });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.08, 1.4), pcbMat);
      pcb.castShadow = true;
      group.add(pcb);

      // Hộp cảm biến điện hóa tròn bên dưới
      const canisterMat = new THREE.MeshStandardMaterial({
        color: 0x93c5fd,
        metalness: 0.85,
        roughness: 0.25
      });
      const canister = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.45, 32), canisterMat);
      canister.position.y = -0.25;
      group.add(canister);

      // Đầu cắm trắng Gravity JST-PH 4-pin
      const connMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.5 });
      const conn = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.35, 0.3), connMat);
      conn.position.set(0, 0.2, 0.5);
      group.add(conn);

      // 4 chân kim loại bên trong jack cắm
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.9, roughness: 0.2 });
      for (let i = 0; i < 4; i++) {
        const pin = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.015, 0.15), pinMat);
        pin.rotation.x = Math.PI / 2;
        pin.position.set(-0.18 + i * 0.12, 0.2, 0.55);
        group.add(pin);
      }

      // 2 chân kiểm tra mạ vàng trên mặt
      for (let i = 0; i < 2; i++) {
        const probe = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 0.18), pinMat);
        probe.position.set(-0.25 + i * 0.5, 0.12, 0.0);
        group.add(probe);
      }

      return group;
    }

    // 2 & 3. CẢM BIẾN KHÍ NUNG NHIỆT MQ (MQ-7 & MQ-4)
    function buildMQSensor(comp, gasType) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bo mạch PCB màu xanh cảm biến
      const pcbMat = new THREE.MeshStandardMaterial({
        color: 0x0f5fa8,
        roughness: 0.35,
        metalness: 0.25
      });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.08, 1.1), pcbMat);
      pcb.castShadow = true;
      group.add(pcb);

      // Chụp lưới thép kim loại hình vòm (Stainless Steel Mesh Dome)
      // Vành kim loại sáng bóng ở chân nắp chụp
      const rimMat = new THREE.MeshStandardMaterial({
        color: 0xe2e8f0,
        metalness: 0.95,
        roughness: 0.15
      });
      const rim = new THREE.Mesh(new THREE.CylinderGeometry(0.44, 0.44, 0.1, 32), rimMat);
      rim.position.set(-0.35, 0.1, 0);
      group.add(rim);

      // Thân lưới thép đan
      const meshMat = new THREE.MeshStandardMaterial({
        color: 0xcccccc,
        metalness: 0.88,
        roughness: 0.3,
        map: meshTextureShared
      });
      const dome = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 0.55, 32), meshMat);
      dome.position.set(-0.35, 0.38, 0);
      group.add(dome);

      // Đỉnh vòm lưới
      const domeTop = new THREE.Mesh(new THREE.SphereGeometry(0.42, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2), meshMat);
      domeTop.position.set(-0.35, 0.65, 0);
      group.add(domeTop);

      // Chiết áp vi chỉnh màu xanh dương (Trimmer Potentiometer)
      const potMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.4 });
      const pot = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.3, 0.32), potMat);
      pot.position.set(0.45, 0.2, 0.22);
      group.add(pot);

      // Ốc vít đồng vi chỉnh trên chiết áp
      const screwMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.9, roughness: 0.2 });
      const screw = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.04, 16), screwMat);
      screw.position.set(0.45, 0.36, 0.22);
      group.add(screw);

      // Chip so sánh LM393 màu đen
      const icMat = new THREE.MeshStandardMaterial({ color: 0x1f2937, roughness: 0.6 });
      const ic = new THREE.Mesh(new THREE.BoxGeometry(0.35, 0.08, 0.22), icMat);
      ic.position.set(0.42, 0.08, -0.22);
      group.add(ic);

      // 4 chân cắm góc (A0, D0, GND, VCC)
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.9, roughness: 0.2 });
      for (let i = 0; i < 4; i++) {
        const pin = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.35), pinMat);
        pin.rotation.z = Math.PI / 2;
        pin.position.set(0.92, 0.04, -0.28 + i * 0.18);
        group.add(pin);
      }

      return group;
    }

    // 4. CẢM BIẾN NHIỆT ĐỘ - ĐỘ ẨM DHT22 (AM2302)
    function buildDHT22Sensor(comp) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Vỏ nhựa ABS màu trắng tinh tế
      const plasticMat = new THREE.MeshStandardMaterial({
        color: 0xf8fafc,
        roughness: 0.45,
        map: dht22Tex
      });
      const body = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.45, 1.4), plasticMat);
      body.castShadow = true;
      group.add(body);

      // Tai treo bắt vít ở đỉnh
      const earMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.5 });
      const ear = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.2, 0.35), earMat);
      ear.position.set(0, 0, -0.85);
      group.add(ear);

      // Lỗ vít tai treo
      const hole = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.22, 16), new THREE.MeshBasicMaterial({ color: 0x070a13 }));
      hole.position.set(0, 0, -0.85);
      group.add(hole);

      // 4 chân kim loại dài vươn ra ngoài
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.9, roughness: 0.2 });
      for (let i = 0; i < 4; i++) {
        const pin = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.018, 0.65), pinMat);
        pin.rotation.x = Math.PI / 2;
        pin.position.set(-0.25 + i * 0.17, -0.05, 0.95);
        group.add(pin);
      }

      return group;
    }

    // 5 & 10. BO MẠCH VI ĐIỀU KHIỂN ESP32 NODEMCU (SLAVE & MASTER)
    function buildESP32Board(comp, isMaster) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // PCB màu đen sẫm
      const pcbMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.4 });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.08, 2.9), pcbMat);
      pcb.castShadow = true;
      group.add(pcb);

      // Khối chắn sóng kim loại nhôm bạc ESP-WROOM-32
      const shieldMat = new THREE.MeshStandardMaterial({
        color: 0xe2e8f0,
        metalness: 0.88,
        roughness: 0.25,
        map: espShieldTex
      });
      const shield = new THREE.Mesh(new THREE.BoxGeometry(1.15, 0.16, 1.3), shieldMat);
      shield.position.set(0, 0.12, 0.15);
      group.add(shield);

      // Ăng-ten PCB mạ vàng meander ở đầu bo mạch
      const antMat = new THREE.MeshStandardMaterial({ map: espAntennaTex, roughness: 0.5 });
      const antenna = new THREE.Mesh(new THREE.BoxGeometry(1.15, 0.04, 0.45), antMat);
      antenna.position.set(0, 0.05, -0.95);
      group.add(antenna);

      // Cổng Micro-USB kim loại ở đuôi bo
      const usbMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.9, roughness: 0.2 });
      const usb = new THREE.Mesh(new THREE.BoxGeometry(0.48, 0.18, 0.35), usbMat);
      usb.position.set(0, 0.12, 1.35);
      group.add(usb);

      // 2 hàng chân cắm pin header màu đen dọc 2 bên sườn bo mạch
      const headerMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.7 });
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.9, roughness: 0.2 });

      [-0.72, 0.72].forEach(sideX => {
        const headerBar = new THREE.Mesh(new THREE.BoxGeometry(0.14, 0.3, 2.6), headerMat);
        headerBar.position.set(sideX, -0.15, 0);
        group.add(headerBar);

        // Chân kim loại nhô bên dưới
        for (let p = 0; p < 15; p++) {
          const pinTip = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.015, 0.35), pinMat);
          pinTip.position.set(sideX, -0.35, -1.15 + p * 0.165);
          group.add(pinTip);
        }
      });

      // 2 Nút bấm vi mô EN và BOOT
      const btnMat = new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.8 });
      [-0.45, 0.45].forEach(btnX => {
        const b = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.08, 16), btnMat);
        b.position.set(btnX, 0.1, 1.15);
        group.add(b);
      });

      // LED nhịp tim GPIO 2 màu xanh dương
      const ledMat = new THREE.MeshStandardMaterial({
        color: 0x3b82f6,
        emissive: 0x3b82f6,
        emissiveIntensity: 0.8
      });
      const led = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.04, 0.06), ledMat);
      led.position.set(0.35, 0.07, 0.95);
      group.add(led);

      return group;
    }

    // 6 & 8. MODULE CHUYỂN ĐỔI MAX485 (SLAVE & MASTER)
    function buildMAX485Module(comp) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bo mạch PCB màu xanh
      const pcbMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.35 });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.08, 1.6), pcbMat);
      pcb.castShadow = true;
      group.add(pcb);

      // Chip MAX485 DIP-8 màu đen
      const icMat = new THREE.MeshStandardMaterial({ color: 0x111827, roughness: 0.6 });
      const ic = new THREE.Mesh(new THREE.BoxGeometry(0.45, 0.2, 0.65), icMat);
      ic.position.set(0, 0.14, 0);
      group.add(ic);

      // Cầu đấu dây 2 cổng màu xanh lá cây (Screw Terminal Block cho A & B)
      const termMat = new THREE.MeshStandardMaterial({ color: 0x16a34a, roughness: 0.4 });
      const term = new THREE.Mesh(new THREE.BoxGeometry(0.7, 0.45, 0.45), termMat);
      term.position.set(0, 0.25, 0.52);
      group.add(term);

      // 2 ốc vít kim loại trên cầu đấu
      const screwMat = new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.9 });
      [-0.18, 0.18].forEach(x => {
        const s = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 0.05, 16), screwMat);
        s.position.set(x, 0.48, 0.52);
        group.add(s);
      });

      // 4 chân cắm header phía đối diện (VCC, GND, RO, DI...)
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.9 });
      for (let i = 0; i < 4; i++) {
        const p = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.3), pinMat);
        p.position.set(-0.35 + i * 0.23, 0.15, -0.65);
        group.add(p);
      }

      return group;
    }

    // 7. CỤM CÁP MẠNG CAT5E 3 - 3 - 2
    function buildCat5eModule(comp) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Vỏ cáp mạng màu xám công nghiệp
      const sheathMat = new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.5 });
      const sheath = new THREE.Mesh(new THREE.CylinderGeometry(0.24, 0.24, 1.8, 24), sheathMat);
      sheath.rotation.z = Math.PI / 2.3;
      sheath.castShadow = true;
      group.add(sheath);

      // 8 lõi dây đồng bọc màu xòe ra ở 2 đầu
      const wireColors = [
        0xf97316, 0xfed7aa, 0x78350f, // 3 Dương (+)
        0x15803d, 0xbbf7d0, 0x451a03, // 3 Mass GND (-)
        0x2563eb, 0xbfdbfe             // 2 Tín hiệu RS485 (A, B)
      ];

      wireColors.forEach((col, idx) => {
        const angle = (idx / 8) * Math.PI * 2;
        const wMat = new THREE.MeshStandardMaterial({ color: col, roughness: 0.3 });
        const wire = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, 0.8), wMat);
        wire.position.set(
          Math.cos(angle) * 0.22 - 0.7,
          Math.sin(angle) * 0.22,
          (idx % 2 === 0 ? 0.15 : -0.15)
        );
        wire.rotation.z = Math.PI / 2.8;
        group.add(wire);
      });

      return group;
    }

    // 9. MODULE NGUỒN XUNG HẠ ÁP LM2596 (5.2V)
    function buildLM2596Module(comp) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bo mạch PCB màu xanh đậm
      const pcbMat = new THREE.MeshStandardMaterial({ color: 0x0369a1, roughness: 0.35 });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.08, 2.2), pcbMat);
      pcb.castShadow = true;
      group.add(pcb);

      // Cuộn cảm cuộn dây đồng hình xuyến (Toroidal Choke Inductor)
      const chokeMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.7 });
      const choke = new THREE.Mesh(new THREE.CylinderGeometry(0.38, 0.38, 0.45, 24), chokeMat);
      choke.position.set(-0.25, 0.25, -0.3);
      group.add(choke);

      // Vòng cuộn dây đồng ánh kim quấn quanh cuộn cảm
      const copperMat = new THREE.MeshStandardMaterial({ color: 0xd97706, metalness: 0.8, roughness: 0.3 });
      const coil = new THREE.Mesh(new THREE.TorusGeometry(0.38, 0.06, 12, 24), copperMat);
      coil.rotation.x = Math.PI / 2;
      coil.position.set(-0.25, 0.25, -0.3);
      group.add(coil);

      // 2 Tụ điện hóa vỏ nhôm xám/đen (Electrolytic Capacitors)
      const capMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4 });
      const topCapMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.85 });

      [-0.75, 0.65].forEach(z => {
        const cap = new THREE.Mesh(new THREE.CylinderGeometry(0.24, 0.24, 0.55, 20), capMat);
        cap.position.set(0.35, 0.3, z);
        group.add(cap);

        const capTop = new THREE.Mesh(new THREE.CylinderGeometry(0.23, 0.23, 0.05, 20), topCapMat);
        capTop.position.set(0.35, 0.58, z);
        group.add(capTop);
      });

      // Chiết áp đa vòng vi chỉnh màu xanh dương (Precision Trimmer 3296)
      const potMat = new THREE.MeshStandardMaterial({ color: 0x2563eb, roughness: 0.4 });
      const pot = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.45, 0.55), potMat);
      pot.position.set(-0.35, 0.26, 0.55);
      group.add(pot);

      // Vít xoay vi chỉnh bằng đồng thau trên góc chiết áp
      const screwMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.95 });
      const screw = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.08, 16), screwMat);
      screw.position.set(-0.35, 0.5, 0.7);
      group.add(screw);

      // IC công suất LM2596 kèm cánh tản nhiệt
      const icMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.5 });
      const ic = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.15, 0.4), icMat);
      ic.position.set(0.35, 0.12, 0.0);
      group.add(ic);

      return group;
    }

    // 11. MÀN HÌNH OLED 0.96 INCH SSD1306 (DYNAMIC DISPLAY)
    function buildOLEDModule(comp) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // PCB màu xanh
      const pcbMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.35 });
      const pcb = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.08, 1.4), pcbMat);
      pcb.castShadow = true;
      group.add(pcb);

      // Tấm kính OLED phát sáng hiển thị số liệu thực tế
      const screenMat = new THREE.MeshBasicMaterial({ map: oledTexture });
      const screen = new THREE.Mesh(new THREE.BoxGeometry(1.26, 0.04, 1.05), screenMat);
      screen.position.set(0, 0.07, 0.1);
      group.add(screen);

      // 4 chân cắm header phía trên (GND, VCC, SCL, SDA)
      const pinMat = new THREE.MeshStandardMaterial({ color: 0xfbbf24, metalness: 0.9 });
      for (let i = 0; i < 4; i++) {
        const p = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.28), pinMat);
        p.position.set(-0.3 + i * 0.2, 0.15, -0.55);
        group.add(p);
      }

      return group;
    }

    // 12. HỆ THỐNG CÒI HÚ & 3 ĐÈN BÁO ĐỘNG
    let ledGreenMesh, ledYellowMesh, ledRedMesh;
    let alarmPointLight;

    function buildAlarmModule(comp) {
      const group = new THREE.Group();
      group.position.set(comp.pos.x, comp.pos.y, comp.pos.z);

      // Bảng gá mạch nhỏ
      const baseMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.6 });
      const base = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.12, 1.2), baseMat);
      base.castShadow = true;
      group.add(base);

      // Còi hú đen tròn công suất cao (Piezo Buzzer)
      const buzzerMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.5 });
      const buzzer = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.42, 0.45, 32), buzzerMat);
      buzzer.position.set(-0.4, 0.28, 0);
      group.add(buzzer);

      // Lỗ thoát âm giữa tâm còi
      const hole = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.06, 16), new THREE.MeshBasicMaterial({ color: 0x000000 }));
      hole.position.set(-0.4, 0.51, 0);
      group.add(hole);

      // 3 Đèn LED vòm 5mm (Đỏ - Vàng - Xanh)
      const createLed = (colorHex, x, z) => {
        const mat = new THREE.MeshStandardMaterial({
          color: colorHex,
          emissive: colorHex,
          emissiveIntensity: 0.3,
          roughness: 0.2,
          metalness: 0.1,
          transparent: true,
          opacity: 0.95
        });
        const dome = new THREE.Mesh(new THREE.SphereGeometry(0.14, 16, 16, 0, Math.PI * 2, 0, Math.PI / 2), mat);
        dome.position.set(x, 0.24, z);
        const col = new THREE.Mesh(new THREE.CylinderGeometry(0.14, 0.14, 0.16, 16), mat);
        col.position.set(x, 0.14, z);
        group.add(dome);
        group.add(col);
        return mat;
      };

      ledRedMesh = createLed(0xef4444, 0.35, -0.32);
      ledYellowMesh = createLed(0xf59e0b, 0.35, 0.0);
      ledGreenMesh = createLed(0x10b981, 0.35, 0.32);

      // Đèn phụ trợ tỏa sáng môi trường
      alarmPointLight = new THREE.PointLight(0x10b981, 1.5, 4);
      alarmPointLight.position.set(0.35, 0.5, 0.32);
      group.add(alarmPointLight);

      return group;
    }

    // Nhãn chữ 3D (Billboard Floating Text Sprite)
    function createTextSprite(text, borderColor = "#38bdf8") {
      const canvas = document.createElement("canvas");
      canvas.width = 512;
      canvas.height = 128;
      const ctx = canvas.getContext("2d");

      ctx.fillStyle = "rgba(15, 23, 42, 0.92)";
      ctx.strokeStyle = borderColor;
      ctx.lineWidth = 6;
      ctx.beginPath();
      ctx.roundRect(8, 8, 496, 112, 28);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 34px -apple-system, sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(text, 256, 64);

      const texture = new THREE.CanvasTexture(canvas);
      const spriteMat = new THREE.SpriteMaterial({ map: texture, depthTest: false });
      const sprite = new THREE.Sprite(spriteMat);
      sprite.renderOrder = 999;
      return sprite;
    }

    // =========================================================================
    // 5. KHỞI TẠO TẤT CẢ LINH KIỆN VÀO SCENE
    // =========================================================================
    const floatingLabels = [];
    let showLabels = true;

    COMPONENTS.forEach(comp => {
      let groupObj;

      switch(comp.id) {
        case "o2_sensor":
          groupObj = buildO2Sensor(comp);
          break;
        case "mq7_sensor":
          groupObj = buildMQSensor(comp, "CO");
          break;
        case "mq4_sensor":
          groupObj = buildMQSensor(comp, "CH4");
          break;
        case "dht22_sensor":
          groupObj = buildDHT22Sensor(comp);
          break;
        case "esp32_slave":
          groupObj = buildESP32Board(comp, false);
          break;
        case "max485_slave":
          groupObj = buildMAX485Module(comp);
          break;
        case "cable_cat5e":
          groupObj = buildCat5eModule(comp);
          break;
        case "max485_master":
          groupObj = buildMAX485Module(comp);
          break;
        case "lm2596":
          groupObj = buildLM2596Module(comp);
          break;
        case "esp32_master":
          groupObj = buildESP32Board(comp, true);
          break;
        case "oled_display":
          groupObj = buildOLEDModule(comp);
          break;
        case "alarm_system":
          groupObj = buildAlarmModule(comp);
          break;
        default:
          groupObj = new THREE.Group();
      }

      // Đặt userData để tương tác
      groupObj.userData = { id: comp.id, name: comp.name };
      scene.add(groupObj);
      componentMeshes[comp.id] = groupObj;

      // Hộp vô hình bao quanh giúp click chuột cực kỳ nhạy và chuẩn xác
      const hitBox = new THREE.Mesh(
        new THREE.BoxGeometry(1.8, 1.2, 1.8),
        new THREE.MeshBasicMaterial({ visible: false })
      );
      hitBox.userData = { id: comp.id };
      groupObj.add(hitBox);

      // Tạo nhãn nổi 3D phía trên linh kiện
      const labelSprite = createTextSprite(comp.name, comp.color);
      labelSprite.position.set(comp.pos.x, comp.pos.y + 0.95, comp.pos.z);
      labelSprite.scale.set(2.0, 0.5, 1.0);
      scene.add(labelSprite);
      floatingLabels.push(labelSprite);
    });

    // Cập nhật nội dung màn hình OLED ban đầu
    updateOledDisplay("safe");

    // =========================================================================
    // 6. XÂY DỰNG ĐƯỜNG DÂY NỐI VÀ HẠT ELECTRON (DÒNG ĐIỆN)
    // =========================================================================
    const wireCurves = [];

    // Cụm 3 Dây Dương (+) (Màu Cam) từ LM2596 Mặt Đất xuống Slave
    createCurvedWire(
      new THREE.Vector3(2.3, 1.3, 1.9),
      new THREE.Vector3(-1.8, -1.1, 0.0),
      0xf97316, 0.045, "wire_power"
    );

    // Cụm 3 Dây Mass GND (-) (Màu Xanh Lá)
    createCurvedWire(
      new THREE.Vector3(2.3, 1.1, 1.9),
      new THREE.Vector3(-1.8, -1.3, 0.0),
      0x10b981, 0.045, "wire_gnd"
    );

    // Cặp 2 Dây Tín Hiệu RS485 Vi Sai (Xanh Dương)
    createCurvedWire(
      new THREE.Vector3(2.3, 1.3, 0.0),
      new THREE.Vector3(-0.3, -1.1, 0.0),
      0x06b6d4, 0.035, "wire_rs485"
    );

    // Dây nội bộ dưới đáy
    createCurvedWire(new THREE.Vector3(-3.8, -1.1, 2.1), new THREE.Vector3(-1.8, -1.1, 0.0), 0x38bdf8, 0.025, "wire_o2");
    createCurvedWire(new THREE.Vector3(-3.8, -1.1, 0.5), new THREE.Vector3(-1.8, -1.1, 0.0), 0xf97316, 0.025, "wire_mq7");
    createCurvedWire(new THREE.Vector3(-3.8, -1.1, -1.1), new THREE.Vector3(-1.8, -1.1, 0.0), 0xeab308, 0.025, "wire_mq4");
    createCurvedWire(new THREE.Vector3(-3.8, -1.1, -2.5), new THREE.Vector3(-1.8, -1.1, 0.0), 0x3b82f6, 0.025, "wire_dht22");
    createCurvedWire(new THREE.Vector3(-1.8, -1.1, 0.0), new THREE.Vector3(-0.3, -1.1, 0.0), 0xa855f7, 0.03, "wire_uart_slave");

    // Dây nội bộ trên mặt đất
    createCurvedWire(new THREE.Vector3(4.0, 1.3, 0.0), new THREE.Vector3(2.3, 1.3, 0.0), 0xa855f7, 0.03, "wire_uart_master");
    createCurvedWire(new THREE.Vector3(4.0, 1.3, 0.0), new THREE.Vector3(4.0, 1.3, 1.9), 0x38bdf8, 0.025, "wire_oled");
    createCurvedWire(new THREE.Vector3(4.0, 1.3, 0.0), new THREE.Vector3(4.0, 1.3, -1.9), 0xef4444, 0.03, "wire_alarm");

    function createCurvedWire(start, end, colorHex, radius, wireId) {
      const mid = new THREE.Vector3().addVectors(start, end).multiplyScalar(0.5);
      mid.y += (start.y > 0 ? 0.65 : -0.25);

      const curve = new THREE.QuadraticBezierCurve3(start, mid, end);
      const tubeGeo = new THREE.TubeGeometry(curve, 36, radius, 8, false);
      const tubeMat = new THREE.MeshStandardMaterial({
        color: colorHex,
        roughness: 0.35,
        metalness: 0.3,
        emissive: colorHex,
        emissiveIntensity: 0.2
      });
      const tubeMesh = new THREE.Mesh(tubeGeo, tubeMat);
      scene.add(tubeMesh);

      wireCurves.push({
        id: wireId,
        curve: curve,
        mesh: tubeMesh,
        originalColor: colorHex,
        particles: createParticlesAlongCurve(curve, colorHex)
      });
    }

    // Tạo các hạt electron phát sáng
    function createParticlesAlongCurve(curve, colorHex) {
      const particleCount = 16;
      const geo = new THREE.SphereGeometry(0.065, 8, 8);
      const mat = new THREE.MeshBasicMaterial({ color: 0xffffff });
      const group = new THREE.Group();

      const particles = [];
      for (let i = 0; i < particleCount; i++) {
        const p = new THREE.Mesh(geo, mat);
        p.visible = false;
        group.add(p);
        particles.push({
          mesh: p,
          offset: i / particleCount
        });
      }
      scene.add(group);
      return { group, particles };
    }

    // =========================================================================
    // 7. ÂM THANH CÒI HÚ WEB AUDIO API CHÂN THẬT
    // =========================================================================
    let audioCtx = null;
    let isSoundMuted = false;

    function playBuzzerBeep(freq = 2400, duration = 0.18) {
      if (isSoundMuted) return;
      try {
        if (!audioCtx) {
          audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
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

    // Render danh sách bên trái
    let currentGroup = "";
    COMPONENTS.forEach(comp => {
      if (comp.group !== currentGroup) {
        currentGroup = comp.group;
        const grp = document.createElement("div");
        grp.className = "group-label";
        grp.textContent = currentGroup;
        compListContainer.appendChild(grp);
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

    // Chọn linh kiện
    function selectComponent(compId) {
      const comp = COMPONENTS.find(c => c.id === compId);
      if (!comp) return;

      document.querySelectorAll(".comp-item").forEach(el => el.classList.remove("active"));
      const selectedItem = document.getElementById(`item-${comp.id}`);
      if (selectedItem) selectedItem.classList.add("active");

      // Hiệu ứng phóng to nhẹ linh kiện đang chọn
      Object.keys(componentMeshes).forEach(k => {
        const group = componentMeshes[k];
        if (k === comp.id) {
          group.scale.set(1.15, 1.15, 1.15);
        } else {
          group.scale.set(1, 1, 1);
        }
      });

      // Camera lướt lại gần vật thể
      const targetPos = new THREE.Vector3(comp.pos.x, comp.pos.y, comp.pos.z);
      controls.target.lerp(targetPos, 0.55);

      // Render nội dung bảng thông tin chi tiết bên phải
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

    // Bật/Tắt Nhãn 3D
    btnLabels.onclick = () => {
      showLabels = !showLabels;
      floatingLabels.forEach(lbl => lbl.visible = showLabels);
      platformLabel1.visible = showLabels;
      platformLabel2.visible = showLabels;
      labelText.textContent = showLabels ? "Tắt Nhãn 3D" : "Bật Nhãn 3D";
    };

    // Bật/Tắt Âm thanh
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

        wireCurves.forEach(w => {
          w.particles.particles.forEach(p => p.mesh.visible = true);
        });
      } else {
        btnPower.classList.remove("active");
        powerText.textContent = "BẬT NGUỒN PIN";
        flowDot.classList.remove("active");
        flowStatusText.textContent = "Nguồn đang tắt (Chưa có dòng điện)";
        flowDesc.textContent = "Bấm 'BẬT NGUỒN PIN' để kích hoạt dòng điện và truyền nhận RS485";

        wireCurves.forEach(w => {
          w.particles.particles.forEach(p => p.mesh.visible = false);
        });
      }
    };

    // Cài đặt 3 cấp độ cảnh báo
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

    // Đặt lại góc nhìn
    document.getElementById("btn-reset-view").onclick = () => {
      camera.position.set(0, 8.5, 12);
      controls.target.set(0, 0, 0);
    };

    // Bắt click chọn trực tiếp trên không gian 3D
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

    // Mặc định chọn Oxy ban đầu
    selectComponent("o2_sensor");

    // =========================================================================
    // 9. VÒNG LẶP RENDER HOẠT HÌNH 3D (ANIMATION LOOP)
    // =========================================================================
    let clock = new THREE.Clock();
    let lastBeepTime = 0;

    function animate() {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();
      const time = clock.getElapsedTime();

      // Di chuyển các hạt electron nếu nguồn đang bật
      if (isPowerOn) {
        wireCurves.forEach(w => {
          const speed = (w.id === "wire_power" || w.id === "wire_gnd") ? 0.35 : 0.55;
          w.particles.particles.forEach(p => {
            p.offset = (p.offset + delta * speed) % 1.0;
            const pt = w.curve.getPoint(p.offset);
            p.mesh.position.copy(pt);
          });
        });

        // Chớp nháy LED Đỏ và hú còi định kỳ khi ở mức Nguy Hiểm
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
    document.getElementById("btn-schematic").onclick = () => {
      modalSchematic.style.display = "flex";
    };
    document.getElementById("btn-close-modal").onclick = () => {
      modalSchematic.style.display = "none";
    };
    modalSchematic.onclick = (e) => {
      if (e.target === modalSchematic) modalSchematic.style.display = "none";
    };
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape") modalSchematic.style.display = "none";
    });
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

import os

output_path = r"c:\Users\Admin\Downloads\All-Project\canhbaokhi\mo_phong_3d_noi_day\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Successfully generated photorealistic 3D simulation at: {output_path}")
