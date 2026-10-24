import os

# Đọc file index.html hiện tại
path = os.path.abspath(r'mo_phong_3d_noi_day\index.html')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Thêm CSS cho Guide Modal
modal_css = '''
    /* MODAL GIẢI THÍCH DỄ HIỂU LỚP 9 */
    .guide-modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(15, 23, 42, 0.78);
      backdrop-filter: blur(8px);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.22s ease;
    }

    .guide-modal-overlay.open {
      opacity: 1;
      pointer-events: auto;
    }

    .guide-modal-content {
      width: 92%;
      max-width: 900px;
      max-height: 88vh;
      background: var(--card-bg, #ffffff);
      border: 2px solid #0284c7;
      border-radius: 18px;
      box-shadow: 0 25px 65px rgba(0, 0, 0, 0.35);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modalPop {
      0% { transform: scale(0.92) translateY(20px); }
      100% { transform: scale(1) translateY(0); }
    }

    .guide-modal-header {
      padding: 16px 22px;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .guide-modal-header h2 {
      font-size: 1.08rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .guide-modal-close {
      background: rgba(255, 255, 255, 0.2);
      border: none;
      color: #ffffff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      font-size: 1.2rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }

    .guide-modal-close:hover {
      background: rgba(255, 255, 255, 0.35);
    }

    .guide-modal-body {
      padding: 22px 26px;
      overflow-y: auto;
      line-height: 1.65;
      font-size: 0.86rem;
      color: var(--text, #0f172a);
    }

    .guide-section {
      background: var(--row-bg, #f1f5f9);
      border: 1px solid var(--row-border, #cbd5e1);
      border-radius: 12px;
      padding: 16px 18px;
      margin-bottom: 18px;
    }

    .guide-section h3 {
      font-size: 0.96rem;
      font-weight: 800;
      color: #0284c7;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    body.dark-mode .guide-section h3 {
      color: #38bdf8;
    }

    .guide-callout {
      padding: 10px 14px;
      border-radius: 8px;
      margin: 10px 0;
      font-size: 0.82rem;
    }

    .guide-callout-green {
      background: #dcfce7;
      border-left: 4px solid #16a34a;
      color: #166534;
    }
    body.dark-mode .guide-callout-green {
      background: rgba(22, 163, 74, 0.15);
      color: #86efac;
    }

    .guide-callout-orange {
      background: #ffedd5;
      border-left: 4px solid #ea580c;
      color: #9a3412;
    }
    body.dark-mode .guide-callout-orange {
      background: rgba(234, 88, 12, 0.15);
      color: #fdba74;
    }

    .guide-callout-red {
      background: #fee2e2;
      border-left: 4px solid #dc2626;
      color: #991b1b;
    }
    body.dark-mode .guide-callout-red {
      background: rgba(220, 38, 38, 0.15);
      color: #fca5a5;
    }

    .guide-step-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 12px;
      margin-top: 10px;
    }

    .guide-step-card {
      background: var(--card-bg, #ffffff);
      border: 1px solid var(--row-border, #cbd5e1);
      border-radius: 10px;
      padding: 12px 14px;
    }

    .guide-step-card h4 {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
'''

# Chèn CSS vào trước </style>
if '/* MODAL GIẢI THÍCH DỄ HIỂU LỚP 9 */' not in content:
    content = content.replace('</style>', modal_css + '\n  </style>')

# 2. Thêm nút [Giải Thích Dễ Hiểu (Lớp 9)] vào header-actions
btn_guide_html = '''      <!-- NÚT MỞ BẢNG GIẢI THÍCH DỄ HIỂU LỚP 9 -->
      <button class="btn" id="btn-open-guide" style="background: #16a34a; color: #ffffff; border-color: #15803d; font-weight: 700;">
        <i class="fa-solid fa-book-open-reader"></i> <span>Giải Thích Dễ Hiểu (Lớp 9)</span>
      </button>'''

if 'id="btn-open-guide"' not in content:
    content = content.replace('<div class="header-actions">', '<div class="header-actions">\n' + btn_guide_html)

# 3. Tạo toàn bộ Modal HTML với nội dung câu chuyện 2 người thám hiểm
modal_html = '''
  <!-- MODAL GIẢI THÍCH DỄ HIỂU LỚP 9 (TẠI SAO PHẢI NỐI DÂY NHƯ VẬY?) -->
  <div id="guide-modal" class="guide-modal-overlay">
    <div class="guide-modal-content">
      <div class="guide-modal-header">
        <h2><i class="fa-solid fa-graduation-cap"></i> GIẢI THÍCH SƠ ĐỒ ĐI DÂY THỰC TẾ (DỄ HIỂU CHO HỌC SINH LỚP 9)</h2>
        <button class="guide-modal-close" id="btn-close-guide" title="Đóng">&times;</button>
      </div>
      <div class="guide-modal-body">
        
        <!-- PHẦN 1: CÂU CHUYỆN HAI NGƯỜI THÁM HIỂM -->
        <div class="guide-section">
          <h3><i class="fa-solid fa-compass"></i> 1. CÂU CHUYỆN: "HAI NGƯỜI THÁM HIỂM HẦM TỐI"</h3>
          <p>Để hiểu toàn bộ dự án mà không cần nhớ những từ kỹ thuật đau đầu, các em hãy tưởng tượng hệ thống gồm <b>2 người đồng đội</b> phối hợp cùng nhau:</p>
          <div class="guide-step-grid">
            <div class="guide-step-card">
              <h4><i class="fa-solid fa-robot" style="color: #16a34a;"></i> Chú lính tí hon (ESP32 dưới đáy)</h4>
              <p style="font-size: 0.78rem; color: var(--text-muted);">Được thả xuống hầm sâu đầy bùn rác tăm tối. Mang theo 4 chiếc "mũi ngửi" (cảm biến) để liên tục hít thở và đo nồng độ khí độc.</p>
            </div>
            <div class="guide-step-card">
              <h4><i class="fa-solid fa-user-shield" style="color: #2563eb;"></i> Đội trưởng chỉ huy (ESP32 trên bờ)</h4>
              <p style="font-size: 0.78rem; color: var(--text-muted);">Đứng an toàn trên mặt đất. Nhìn số liệu trên màn hình, phát Wi-Fi cho điện thoại mọi người cùng xem và sẵn sàng bấm còi hú báo động.</p>
            </div>
            <div class="guide-step-card">
              <h4><i class="fa-solid fa-ethernet" style="color: #ea580c;"></i> Dây cáp mạng Cat5e (20 - 30 mét)</h4>
              <p style="font-size: 0.78rem; color: var(--text-muted);">Sợi dây liên lạc nối giữa 2 người: vừa tiếp tế điện từ trên bờ xuống, vừa truyền tin tức từ dưới đáy phóng lên.</p>
            </div>
          </div>
        </div>

        <!-- PHẦN 2: TẠI SAO CẦN 3 SỢI DÂY -->
        <div class="guide-section">
          <h3><i class="fa-solid fa-plug"></i> 2. TẠI SAO MỌI CẢM BIẾN LUÔN CẦN 3 SỢI DÂY?</h3>
          <p>Nhiều bạn thắc mắc: <i>"Tại sao mỗi cảm biến lại cắm tới 3 sợi dây rườm rà thế?"</i> Rất đơn giản, nó giống hệt chiếc điện thoại của các em:</p>
          <ul style="margin-left: 20px; margin-top: 6px; font-size: 0.82rem;">
            <li><b>Dây VCC (Đỏ - Cực Dương):</b> Giống như cắm sạc pin, đây là đường <b>cấp điện 5V</b> để nuôi cảm biến sống và nung nóng lõi đo.</li>
            <li><b>Dây GND (Xanh lá - Cực Âm/Mass):</b> Đường dây khép kín mạch điện để dòng điện chạy về nguồn (theo bài dòng điện Vật lý 7 và 9).</li>
            <li><b>Dây Tín Hiệu (Data / Analog):</b> Đây là <b>"chiếc micro nói chuyện"</b>. Sau khi ngửi thấy khí, cảm biến dùng sợi dây này để báo số liệu về cho ESP32.</li>
          </ul>
        </div>

        <!-- PHẦN 3: 4 CHIẾC MŨI NGỬI NÓI CHUYỆN NHƯ THẾ NÀO -->
        <div class="guide-section">
          <h3><i class="fa-solid fa-lungs"></i> 3. 4 CHIẾC "MŨI NGỬI" NÓI CHUYỆN VỚI ESP32 DƯỚI ĐÁY NHƯ THẾ NÀO?</h3>
          <div class="guide-step-grid">
            <div class="guide-step-card">
              <h4 style="color: #ea580c;"><i class="fa-solid fa-skull-crossbones"></i> Khí CO (MQ-7) & Gas (MQ-4)</h4>
              <p style="font-size: 0.78rem;">Dùng chân <b>A0 (Analog)</b> cắm vào chân <b>GPIO 34 và GPIO 35</b>. Chân A0 giống một cái đồng hồ đo: khí độc càng đậm đặc thì điện áp phát ra càng cao. ESP32 chỉ cần đo độ mạnh yếu của điện áp là biết ngay có bao nhiêu phần triệu (ppm) khí độc.</p>
            </div>
            <div class="guide-step-card">
              <h4 style="color: #0284c7;"><i class="fa-solid fa-lungs"></i> Cảm biến Oxy (DFRobot)</h4>
              <p style="font-size: 0.78rem;">Dùng 2 dây <b>SDA (Dữ liệu)</b> và <b>SCL (Nhịp đồng hồ)</b> cắm vào <b>GPIO 21 và GPIO 22</b>. Giống như hai người gõ nhịp: một dây gõ "tíc tắc", dây kia đọc to: <i>"Oxy đang là 20.9%!"</i>, siêu chuẩn xác.</p>
            </div>
            <div class="guide-step-card">
              <h4 style="color: #9333ea;"><i class="fa-solid fa-temperature-half"></i> Nhiệt Ẩm (DHT22)</h4>
              <p style="font-size: 0.78rem;">Dùng chân <b>DATA</b> cắm vào <b>GPIO 4</b>. Cống rãnh rất ẩm ướt làm cảm biến khí dễ bị báo sai. DHT22 báo nhiệt độ và độ ẩm về để ESP32 "bù trừ sai số", không bao giờ báo động giả.</p>
            </div>
            <div class="guide-step-card">
              <h4 style="color: #16a34a;"><i class="fa-solid fa-envelope-open-text"></i> Bức thư báo cáo (Gói JSON)</h4>
              <p style="font-size: 0.78rem;">ESP32 dưới đáy gom cả 5 con số vào 1 dòng chữ báo cáo: <code>{"o2":20.9, "co":0, "ch4":0, "t":28, "h":80}</code> rồi gửi qua chip phát loa <b>MAX485</b> phóng lên mặt đất.</p>
            </div>
          </div>
        </div>

        <!-- PHẦN 4: BÍ MẬT CÁP CAT5E & VẬT LÝ 9 -->
        <div class="guide-section">
          <h3><i class="fa-solid fa-bolt"></i> 4. SÁNG KIẾN VẬT LÝ 9: TẠI SAO CHẬP CỤM DÂY 3 - 3 - 2?</h3>
          <div class="guide-callout guide-callout-green">
            <b>Công thức Điện trở dây dẫn (Vật lý lớp 9):</b> \( R = \rho \cdot \frac{l}{S} \)
          </div>
          <p style="font-size: 0.8rem; margin-top: 6px;">
            Sợi dây cáp mạng Cat5e có lõi đồng rất mảnh (tiết diện \(S\) nhỏ xíu). Dây dài tới 20 mét thì điện trở \(R\) rất lớn. Các cảm biến nung nhiệt dưới đáy ăn dòng điện rất khỏe. Nếu chỉ dùng 1 sợi dây nhỏ xíu, điện sẽ bị rơi rớt dọc đường (sụt áp): trên bờ cấp 5V nhưng xuống đáy chỉ còn 3.5V làm cảm biến chết ngất!
          </p>
          <div class="guide-callout guide-callout-orange">
            <b>Giải pháp sáng kiến của nhóm:</b>
            <ul style="margin-left: 20px; margin-top: 4px;">
              <li><b>Chập 3 sợi làm 1 đường Dương (+5.2V):</b> Tiết diện \(S\) tăng gấp 3 &rarr; Điện trở \(R\) <b>giảm 3 lần</b>!</li>
              <li><b>Chập 3 sợi làm 1 đường Mass (GND):</b> Đường về của dòng điện cũng giảm điện trở 3 lần!</li>
              <li><b>2 sợi còn lại (Cặp xoắn A & B):</b> Dùng truyền tín hiệu vi sai RS-485 chống mọi sóng nhiễu sấm sét, độ ẩm.</li>
              <li><b>Chỉnh nguồn LM2596 lên 5.2V:</b> Bù trừ đúng 0.2V rơi rớt dọc đường cáp 20m &rarr; Xuống tới đáy hầm điện áp luôn chuẩn đét <b>5.0V</b> tròn trịa!</li>
            </ul>
          </div>
        </div>

        <!-- PHẦN 5: TRÊN MẶT ĐẤT LÀM GÌ ĐỂ CỨU MẠNG NGƯỜI -->
        <div class="guide-section">
          <h3><i class="fa-solid fa-bullhorn" style="color: #dc2626;"></i> 5. TRÊN MẶT ĐẤT, ESP32 MASTER LÀM GÌ ĐỂ CỨU MẠNG NGƯỜI?</h3>
          <p>Khi chip MAX485 trên bờ đón lấy bức thư gửi từ dưới đáy, nó chuyển vào chân <b>GPIO 16 (RX2)</b> của ESP32 Master trên mặt đất. Đội trưởng Master lập tức làm 3 việc:</p>
          <ul style="margin-left: 20px; margin-top: 6px; font-size: 0.82rem;">
            <li><b>Chiếu lên Màn hình OLED (chân 21, 22):</b> Người chỉ huy liếc nhìn là thấy ngay nồng độ Oxy và khí độc.</li>
            <li><b>Tự phát sóng Wi-Fi:</b> Ai cầm điện thoại lại gần mở trình duyệt là xem được biểu đồ sóng thời gian thực mà <b>hoàn toàn không cần Internet hay 4G</b>.</li>
            <li><b>Điều khiển Còi Hú và 3 Đèn LED (chân 23, 19, 5, 18):</b>
              <br>&bull; <span style="color: #16a34a; font-weight: 700;">Đèn Xanh:</span> An toàn, được phép bước xuống.
              <br>&bull; <span style="color: #d97706; font-weight: 700;">Đèn Vàng:</span> Có dấu hiệu khí lạ, phải bật quạt thông gió.
              <br>&bull; <span style="color: #dc2626; font-weight: 700;">Đèn Đỏ + Còi Hú Inh Ỏi:</span> Nguy hiểm chết người! Oxy &lt; 18% hoặc có khí độc!
            </li>
          </ul>

          <div class="guide-callout guide-callout-red" style="margin-top: 10px;">
            <b>ĐIỂM CỐT LÕI CỨU SỐNG CON NGƯỜI ("BỨC TƯỜNG ÂM THANH"):</b><br>
            Máy đo cầm tay hiện nay bắt công nhân phải cầm máy bước xuống hầm mới đo được. Khi người dưới ngất đi, người trên bờ không biết gì sẽ nhảy xuống cứu và chết chùm!
            <br>&rarr; Hệ thống của nhóm thả xuống đo trước khi con người bước vào. Chiếc còi hú công suất lớn đặt ngay miệng hầm đóng vai trò như một <b>"BỨC TƯỜNG ÂM THANH"</b> đanh thép, cảnh báo trực diện làm người trên bờ giật mình khựng lại, <b>dứt khoát ngăn chặn thảm kịch nhảy xuống cứu mù quáng!</b>
          </div>
        </div>

      </div>
    </div>
  </div>
'''

if 'id="guide-modal"' not in content:
    content = content.replace('<!-- WORKSPACE PAN & ZOOM STAGE -->', modal_html + '\n  <!-- WORKSPACE PAN & ZOOM STAGE -->')

# 4. Thêm JS mở/đóng modal vào script
modal_js = '''
    // ĐIỀU KHIỂN MODAL GIẢI THÍCH DỄ HIỂU LỚP 9
    const guideModal = document.getElementById("guide-modal");
    const btnOpenGuide = document.getElementById("btn-open-guide");
    const btnCloseGuide = document.getElementById("btn-close-guide");

    if (btnOpenGuide && guideModal) {
      btnOpenGuide.onclick = () => guideModal.classList.add("open");
    }
    if (btnCloseGuide && guideModal) {
      btnCloseGuide.onclick = () => guideModal.classList.remove("open");
    }
    window.addEventListener("click", (e) => {
      if (e.target === guideModal) guideModal.classList.remove("open");
    });
'''

if 'btnOpenGuide.onclick' not in content:
    content = content.replace('// KHỞI ĐỘNG HỆ THỐNG', modal_js + '\n    // KHỞI ĐỘNG HỆ THỐNG')

# Ghi lại vào file
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Guide Modal & Easy 9th-Grade Explanations into index.html!")
