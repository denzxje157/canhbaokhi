import os
import re

path = os.path.abspath(r'mo_phong_3d_noi_day\index.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# ==============================================================================
# 1. CẬP NHẬT CSS RESPONSIVE & UXUI HIỆN ĐẠI
# ==============================================================================
responsive_css = '''
    /* ==========================================================================
       UX/UI HOÀN HẢO & TỐI ƯU HÓA RESPONSIVE MOBILE, LAPTOP, TABLET
       ========================================================================== */
    
    /* NÚT THU GỌN BẢNG ĐIỀU KHIỂN */
    .panel-close-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.95rem;
      padding: 4px 8px;
      border-radius: 6px;
      transition: all 0.15s;
    }
    .panel-close-btn:hover {
      background: var(--row-border);
      color: var(--text);
    }

    /* THANH KÉO DÀNH CHO BOTTOM SHEET MOBILE */
    .sheet-handle-bar {
      display: none;
      width: 44px;
      height: 5px;
      border-radius: 3px;
      background: var(--mat-border);
      margin: 8px auto 4px auto;
    }

    /* NÚT ĐIỀU KHIỂN ZOOM NHANH TRÊN MÀN HÌNH */
    .canvas-quick-controls {
      position: absolute;
      bottom: 25px;
      right: 25px;
      z-index: 40;
      display: flex;
      flex-direction: column;
      gap: 6px;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 10px;
      padding: 5px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.1);
      backdrop-filter: blur(12px);
    }
    .quick-zoom-btn {
      width: 32px;
      height: 32px;
      border-radius: 7px;
      background: var(--btn-bg);
      border: 1px solid var(--btn-border);
      color: var(--text);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
    }
    .quick-zoom-btn:hover {
      background: #0284c7;
      color: #fff;
      border-color: #0369a1;
    }

    /* BACKDROP PHỦ MỜ KHI MỞ DRAWER TRÊN MOBILE */
    .mobile-backdrop {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(15, 23, 42, 0.55);
      backdrop-filter: blur(4px);
      z-index: 85;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.22s ease;
    }
    .mobile-backdrop.active {
      opacity: 1;
      pointer-events: auto;
    }

    /* TIÊU ĐỀ THƯƠNG HIỆU GỌN GÀNG */
    .brand-box {
      display: flex;
      flex-direction: column;
    }
    .brand-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: #0284c7;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    body.dark-mode .brand-title {
      color: #38bdf8;
    }
    .brand-sub {
      font-size: 0.73rem;
      color: var(--text-muted);
      margin-top: 1px;
    }

    /* HIỆU ỨNG THU GỌN SIDEBAR MƯỢT MÀ */
    .sidebar-left {
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease !important;
    }
    .sidebar-left.collapsed {
      transform: translateX(-310px) !important;
      pointer-events: none !important;
      opacity: 0 !important;
    }

    .sidebar-right {
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease !important;
    }
    .sidebar-right.collapsed {
      transform: translateX(450px) !important;
      pointer-events: none !important;
      opacity: 0 !important;
    }

    /* ĐỊNH DẠNG FILTER BAR KHÔNG BAO GIỜ BỊ ĐÈ */
    .filter-bar {
      top: 72px !important;
      left: 50% !important;
      transform: translateX(-50%) !important;
      max-width: calc(100vw - 32px) !important;
      overflow-x: auto !important;
      white-space: nowrap !important;
      scrollbar-width: none !important;
      border-radius: 30px !important;
      padding: 5px 12px !important;
      z-index: 45 !important;
    }
    .filter-bar::-webkit-scrollbar { display: none; }

    /* ĐỊNH DẠNG BOTTOM BAR TRUNG TÂM */
    .bottom-bar {
      bottom: 20px !important;
      left: 50% !important;
      right: auto !important;
      transform: translateX(-50%) !important;
      min-width: 580px !important;
      max-width: 90vw !important;
      z-index: 45 !important;
    }

    /* ==========================================================================
       MEDIA QUERIES CHO MÀN HÌNH LAPTOP VÀ IPAD (DƯỚI 1280px)
       ========================================================================== */
    @media (max-width: 1280px) {
      .sidebar-right {
        width: 360px !important;
      }
      .sidebar-left {
        width: 260px !important;
      }
      .hide-md {
        display: none !important;
      }
      .bottom-bar {
        min-width: auto !important;
        width: 92vw !important;
      }
    }

    /* ==========================================================================
       MEDIA QUERIES TỐI ƯU HÓA HOÀN TOÀN CHO MOBILE & TABLET (DƯỚI 900px)
       ========================================================================== */
    @media (max-width: 900px) {
      /* HEADER GỌN GÀNG TRÊN ĐIỆN THOẠI */
      header {
        top: 8px !important;
        left: 10px !important;
        right: 10px !important;
      }
      .header-title {
        padding: 6px 12px !important;
      }
      .brand-title {
        font-size: 0.88rem !important;
      }
      .brand-sub {
        display: none !important;
      }
      .header-actions {
        gap: 6px !important;
      }
      .btn {
        padding: 7px 10px !important;
        font-size: 0.78rem !important;
      }
      .hide-sm {
        display: none !important;
      }

      /* FILTER BAR CO DÃN */
      .filter-bar {
        top: 60px !important;
        padding: 4px 8px !important;
        font-size: 0.7rem !important;
      }

      /* SIDEBAR TRÁI: BIẾN THÀNH MOBILE DRAWER TRƯỢT TỪ BÊN TRÁI */
      .sidebar-left {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        bottom: 0 !important;
        width: 82vw !important;
        max-width: 320px !important;
        border-radius: 0 16px 16px 0 !important;
        z-index: 90 !important;
        box-shadow: 10px 0 35px rgba(0,0,0,0.3) !important;
        transform: translateX(-105%) !important;
      }
      .sidebar-left.mobile-open {
        transform: translateX(0) !important;
        opacity: 1 !important;
        pointer-events: auto !important;
      }

      /* SIDEBAR PHẢI: BIẾN THÀNH BOTTOM SHEET TRƯỢT TỪ DƯỚI LÊN (CHUẨN APP DI ĐỘNG) */
      .sidebar-right {
        position: fixed !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        top: auto !important;
        width: 100vw !important;
        height: 78vh !important;
        border-radius: 20px 20px 0 0 !important;
        z-index: 90 !important;
        box-shadow: 0 -10px 40px rgba(0,0,0,0.35) !important;
        transform: translateY(105%) !important;
      }
      .sidebar-right.mobile-open {
        transform: translateY(0) !important;
        opacity: 1 !important;
        pointer-events: auto !important;
      }
      .sheet-handle-bar {
        display: block !important;
      }

      /* BOTTOM BAR TRÊN MOBILE */
      .bottom-bar {
        bottom: 10px !important;
        width: 95vw !important;
        height: 48px !important;
        padding: 0 10px !important;
        font-size: 0.72rem !important;
      }
      .flow-desc {
        display: none !important;
      }
      .sim-levels {
        gap: 4px !important;
      }
      .btn-level {
        padding: 4px 8px !important;
        font-size: 0.72rem !important;
      }

      /* NÚT ZOOM TRÊN MOBILE */
      .canvas-quick-controls {
        bottom: 68px !important;
        right: 12px !important;
      }
    }
'''

# Thay thế hoặc bổ sung CSS
if '/* UX/UI HOÀN HẢO & TỐI ƯU HÓA RESPONSIVE MOBILE, LAPTOP, TABLET */' not in text:
    text = text.replace('</style>', responsive_css + '\n  </style>')

# ==============================================================================
# 2. CẬP NHẬT HEADER VỚI CÁC NÚT BẬT/TẮT PANEL THÔNG MINH
# ==============================================================================
new_header = '''  <!-- TOP HEADER ĐỒNG BỘ THÔNG MINH -->
  <header>
    <div class="header-title">
      <div class="brand-box">
        <div class="brand-title">
          <i class="fa-solid fa-microchip"></i> SƠ ĐỒ ĐI DÂY KỸ THUẬT
        </div>
        <div class="brand-sub">Hệ Thống Cảnh Báo Sớm Khí Độc Trong Không Gian Kín</div>
      </div>
    </div>
    
    <div class="header-actions">
      <!-- Nút mở danh sách thiết bị -->
      <button class="btn" id="btn-toggle-left" title="Danh Sách 11 Thiết Bị">
        <i class="fa-solid fa-bars-staggered"></i> <span class="hide-sm">Thiết Bị (11)</span>
      </button>

      <!-- Nút mở cẩm nang dễ hiểu lớp 9 -->
      <button class="btn btn-guide" id="btn-open-guide" style="background: #16a34a; color: #ffffff; border-color: #15803d; font-weight: 700;">
        <i class="fa-solid fa-book-open-reader"></i> <span class="hide-sm">Giải Thích Lớp 9</span>
      </button>

      <!-- Nút đổi nền Sáng / Tối -->
      <button class="btn btn-theme" id="btn-theme-toggle" title="Chuyển Sáng / Tối">
        <i class="fa-solid fa-sun"></i> <span class="hide-md" id="theme-text">Sáng</span>
      </button>

      <!-- Nút Bật / Tắt Nguồn Pin -->
      <button class="btn btn-power" id="btn-power" title="Bật Nguồn Hệ Thống">
        <i class="fa-solid fa-power-off"></i> <span class="hide-sm" id="power-text">Nguồn (5.2V)</span>
      </button>

      <!-- Nút Reset Vị Trí Căn Giữa -->
      <button class="btn" id="btn-reset-view" title="Căn chỉnh toàn cảnh">
        <i class="fa-solid fa-arrows-rotate"></i> <span class="hide-md">Căn Giữa</span>
      </button>

      <!-- Nút mở bảng chi tiết bên phải -->
      <button class="btn" id="btn-toggle-right" title="Xem Chi Tiết & Quy Trình">
        <i class="fa-solid fa-circle-info"></i> <span class="hide-sm">Chi Tiết</span>
      </button>
    </div>
  </header>'''

# Thay thế khối header cũ
text = re.sub(r'<header>.*?</header>', new_header, text, flags=re.DOTALL)

# ==============================================================================
# 3. CẬP NHẬT HEADER TRONG SIDEBAR TRÁI & PHẢI CÓ NÚT ĐÓNG X
# ==============================================================================
new_left_panel_hdr = '''    <div class="panel-hdr">
      <span><i class="fa-solid fa-layer-group"></i> THIẾT BỊ HỆ THỐNG</span>
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="font-size: 0.72rem; color: var(--text-muted);">11 Module</span>
        <button class="panel-close-btn" id="btn-close-left" title="Đóng bảng"><i class="fa-solid fa-xmark"></i></button>
      </div>
    </div>'''

text = re.sub(r'<div class="sidebar-left">\s*<div class="panel-hdr">.*?</div>\s*</div>', 
              r'<div class="sidebar-left" id="sidebar-left">\n' + new_left_panel_hdr, text, flags=re.DOTALL)

# Đảm bảo sidebar-left có id="sidebar-left"
if 'id="sidebar-left"' not in text:
    text = text.replace('<div class="sidebar-left">', '<div class="sidebar-left" id="sidebar-left">')

# Đảm bảo sidebar-right có id="sidebar-right", handle bar và nút đóng X
new_right_panel_hdr = '''  <div class="sidebar-right" id="sidebar-right">
    <div class="sheet-handle-bar"></div>
    <div class="panel-hdr">
      <span><i class="fa-solid fa-circle-info"></i> THÔNG TIN KẾT NỐI & CODE THƯ VIỆN</span>
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 0.75rem; color: #0284c7; font-weight: 800;" id="detail-category">SLAVE</span>
        <button class="panel-close-btn" id="btn-close-right" title="Đóng chi tiết"><i class="fa-solid fa-xmark"></i></button>
      </div>
    </div>'''

text = re.sub(r'<div class="sidebar-right" id="sidebar-right">\s*<div class="panel-hdr">.*?</div>', 
              new_right_panel_hdr, text, flags=re.DOTALL)

# ==============================================================================
# 4. THÊM NÚT ZOOM NHANH VÀ BACKDROP CHO MOBILE VÀO TRANG
# ==============================================================================
quick_controls_html = '''
  <!-- BACKDROP PHỦ MỜ CHO MOBILE KHI MỞ MENU/PANEL -->
  <div class="mobile-backdrop" id="mobile-backdrop"></div>

  <!-- NÚT ZOOM VÀ RESET NHANH TRÊN MÀN HÌNH -->
  <div class="canvas-quick-controls">
    <button class="quick-zoom-btn" id="btn-zoom-in" title="Phóng to (+)"><i class="fa-solid fa-plus"></i></button>
    <button class="quick-zoom-btn" id="btn-zoom-out" title="Thu nhỏ (-)"><i class="fa-solid fa-minus"></i></button>
    <button class="quick-zoom-btn" id="btn-zoom-fit" title="Vừa màn hình"><i class="fa-solid fa-expand"></i></button>
  </div>
'''

if 'id="mobile-backdrop"' not in text:
    text = text.replace('</body>', quick_controls_html + '\n</body>')

# ==============================================================================
# 5. CẬP NHẬT JAVASCRIPT ĐIỀU KHIỂN RESPONSIVE & MOBILE TOUCH
# ==============================================================================
responsive_js = '''
    // ==========================================================================
    // ĐIỀU KHIỂN RESPONSIVE & MOBILE GESTURES CHO MỌI THIẾT BỊ
    // ==========================================================================
    const sidebarLeft = document.getElementById("sidebar-left");
    const sidebarRight = document.getElementById("sidebar-right");
    const mobileBackdrop = document.getElementById("mobile-backdrop");

    const btnToggleLeft = document.getElementById("btn-toggle-left");
    const btnCloseLeft = document.getElementById("btn-close-left");
    const btnToggleRight = document.getElementById("btn-toggle-right");
    const btnCloseRight = document.getElementById("btn-close-right");

    function isMobileView() {
      return window.innerWidth <= 900;
    }

    // Toggle Sidebar Trái
    function toggleLeftSidebar(openState) {
      if (isMobileView()) {
        const isOpen = openState !== undefined ? openState : !sidebarLeft.classList.contains("mobile-open");
        sidebarLeft.classList.toggle("mobile-open", isOpen);
        mobileBackdrop.classList.toggle("active", isOpen);
        if (isOpen) sidebarRight.classList.remove("mobile-open");
      } else {
        const isCollapsed = openState !== undefined ? !openState : !sidebarLeft.classList.contains("collapsed");
        sidebarLeft.classList.toggle("collapsed", isCollapsed);
      }
    }

    if (btnToggleLeft) btnToggleLeft.onclick = () => toggleLeftSidebar();
    if (btnCloseLeft) btnCloseLeft.onclick = () => toggleLeftSidebar(false);

    // Toggle Sidebar Phải
    function toggleRightSidebar(openState) {
      if (isMobileView()) {
        const isOpen = openState !== undefined ? openState : !sidebarRight.classList.contains("mobile-open");
        sidebarRight.classList.toggle("mobile-open", isOpen);
        mobileBackdrop.classList.toggle("active", isOpen);
        if (isOpen) sidebarLeft.classList.remove("mobile-open");
      } else {
        const isCollapsed = openState !== undefined ? !openState : !sidebarRight.classList.contains("collapsed");
        sidebarRight.classList.toggle("collapsed", isCollapsed);
      }
    }

    if (btnToggleRight) btnToggleRight.onclick = () => toggleRightSidebar();
    if (btnCloseRight) btnCloseRight.onclick = () => toggleRightSidebar(false);

    // Click backdrop để đóng tất cả drawer trên mobile
    if (mobileBackdrop) {
      mobileBackdrop.onclick = () => {
        sidebarLeft.classList.remove("mobile-open");
        sidebarRight.classList.remove("mobile-open");
        mobileBackdrop.classList.remove("active");
      };
    }

    // Tự động căn chỉnh góc nhìn phù hợp theo kích thước màn hình thiết bị
    function fitViewToScreen() {
      const w = window.innerWidth;
      const h = window.innerHeight;

      if (w <= 600) {
        // Điện thoại di động
        scale = 0.36;
        panX = 15;
        panY = 65;
        // Mặc định đóng cả 2 panel để hiển thị sơ đồ rộng thoáng 100%
        sidebarLeft.classList.add("collapsed");
        sidebarRight.classList.add("collapsed");
      } else if (w <= 1024) {
        // Máy tính bảng iPad / Màn hình nhỏ
        scale = 0.45;
        panX = 40;
        panY = 50;
        sidebarLeft.classList.add("collapsed");
      } else if (w <= 1400) {
        // Laptop 13-15 inch (như máy bạn đang dùng)
        scale = 0.52;
        panX = 160;
        panY = 20;
      } else {
        // Màn hình máy tính lớn
        scale = 0.60;
        panX = 220;
        panY = 25;
      }
      updateTransform();
    }

    // Nút Zoom Nhanh
    document.getElementById("btn-zoom-in").onclick = () => {
      scale = Math.min(scale * 1.15, 1.8);
      updateTransform();
    };
    document.getElementById("btn-zoom-out").onclick = () => {
      scale = Math.max(scale * 0.85, 0.28);
      updateTransform();
    };
    document.getElementById("btn-zoom-fit").onclick = () => {
      fitViewToScreen();
    };

    // HỖ TRỢ CẢM ỨNG ĐA ĐIỂM (PINCH ZOOM & TOUCH PAN CHO ĐIỆN THOẠI)
    let initialTouchDist = 0;
    let initialTouchScale = 1;

    container.addEventListener("touchstart", (e) => {
      if (e.target.closest(".comp-card") || e.target.closest("button") || e.target.closest(".sidebar-left") || e.target.closest(".sidebar-right") || e.target.closest(".filter-bar")) return;
      if (e.touches.length === 1) {
        isDragging = true;
        startX = e.touches[0].clientX - panX;
        startY = e.touches[0].clientY - panY;
      } else if (e.touches.length === 2) {
        isDragging = false;
        initialTouchDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        initialTouchScale = scale;
      }
    }, { passive: true });

    container.addEventListener("touchmove", (e) => {
      if (e.touches.length === 1 && isDragging) {
        panX = e.touches[0].clientX - startX;
        panY = e.touches[0].clientY - startY;
        updateTransform();
      } else if (e.touches.length === 2 && initialTouchDist > 0) {
        const currentDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        const factor = currentDist / initialTouchDist;
        scale = Math.min(Math.max(initialTouchScale * factor, 0.28), 1.8);
        updateTransform();
      }
    }, { passive: true });

    container.addEventListener("touchend", () => {
      isDragging = false;
      initialTouchDist = 0;
    });
'''

# Chèn mã responsive_js vào trước hàm KHỞI ĐỘNG HỆ THỐNG
if 'fitViewToScreen' not in text:
    text = text.replace('// KHỞI ĐỘNG HỆ THỐNG', responsive_js + '\n    // KHỞI ĐỘNG HỆ THỐNG')

# Cập nhật hàm khởi động gọi fitViewToScreen()
text = text.replace('updateTransform();\n        selectComponent("o2_sensor");', 
                    'fitViewToScreen();\n        selectComponent("o2_sensor");')

# Khi bấm Reset Vị Trí, gọi fitViewToScreen()
text = re.sub(r'document\.getElementById\("btn-reset-view"\)\.onclick = \(\) => \{.*?\};',
              'document.getElementById("btn-reset-view").onclick = () => fitViewToScreen();',
              text)

# Khi người dùng chọn 1 component trong danh sách trên mobile:
# Tự động mở Bottom Sheet để xem giải thích
mobile_click_select = '''      // Nếu đang ở màn hình mobile, tự động mở Bottom Sheet xem chi tiết
      if (isMobileView()) {
        sidebarRight.classList.add("mobile-open");
        mobileBackdrop.classList.add("active");
        sidebarLeft.classList.remove("mobile-open");
      } else {
        // Trên màn hình lớn, nếu bảng chi tiết đang đóng thì tự mở ra
        sidebarRight.classList.remove("collapsed");
      }'''

if 'if (isMobileView()) {' not in text:
    text = text.replace('applyWireVisibility();', 'applyWireVisibility();\n' + mobile_click_select)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully applied Ultimate Responsive & Mobile UI/UX overhaul to index.html!")
