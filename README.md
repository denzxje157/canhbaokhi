# HỆ THỐNG CẢNH BÁO SỚM KHÍ ĐỘC VÀ THIẾU OXY TRONG KHÔNG GIAN KÍN

Dự án Nghiên cứu Khoa học Kỹ thuật (KHKT) cấp THCS ứng dụng công nghệ vi điều khiển ESP32, chuẩn truyền thông công nghiệp RS-485 vi sai và giao diện SCADA Web Server tự động phát Wi-Fi.

---

## 📌 Tổng Quan Hệ Thống

Dự án gồm **3 Khối Chính** phối hợp chặt chẽ với nhau:

1. **Khối Dưới Đáy Không Gian Kín (ESP32 Slave)**:
   - **4 Cảm biến khí**:
     - Cảm biến Oxy DFRobot I2C Gravity (`SEN0496` / `SEN0322`): Theo dõi nồng độ $O_2$ (Cảnh báo $< 18.0\%$).
     - Cảm biến CO Winsen MQ-7 (AO Analog): Phát hiện khí than độc (Cảnh báo $> 35\text{ ppm}$).
     - Cảm biến Gas/Metan Winsen MQ-4 (AO Analog): Phát hiện khí metan gây nổ (Cảnh báo $> 1.0\%$).
     - Cảm biến Nhiệt độ & Độ ẩm DHT22 (1-Wire): Đo môi trường hầm lò.
   - **Bộ xử lý ESP32 Slave**: Gom toàn bộ 5 thông số khí thành bức thư JSON.
   - **Module MAX485 Slave (TX)**: Chuyển tín hiệu UART thành dòng điện vi sai đối xứng trên 2 chân tín hiệu $A$ và $B$.
   - **Bus Nguồn Kép (5.2V & GND)**: Nhận dòng điện từ mặt đất truyền xuống nuôi 4 cảm biến và vi điều khiển.

2. **Hệ Thống Cáp Truyền Tải Vật Lý (Cáp Cat5e 20m - Sáng Kiến Cụm 3 - 3 - 2)**:
   - **3 Sợi Dương (+5.2V)**: Chập 3 sợi (Cam, Trắng-Cam, Trắng-Nâu) để tăng tiết diện $S$ gấp 3, giảm điện trở $R$ 3 lần ($R = \rho \frac{l}{S}$).
   - **3 Sợi Mass (GND)**: Chập 3 sợi (Nâu, Xanh Lá, Trắng-Xanh Lá) làm đường về của dòng điện.
   - **2 Sợi Tín Hiệu Vi Sai ($A$ & $B$)**: Xanh Dương và Trắng-Xanh dẫn sóng RS-485 chống nhiễu cực mạnh dọc theo chiều sâu 20m–50m.

3. **Khối Cứu Hộ Trên Mặt Đất (ESP32 Master)**:
   - **Cục Pin 3S 18650 Li-ion (12V)**: Dung lượng 2600mAh cấp điện độc lập hơn 16 tiếng không cần điện lưới 220V.
   - **Nguồn Giảm Áp DC-DC LM2596 BUCK (5.2V)**: Hạ áp biến tần hiệu suất cao 92%, đặt 5.2V để bù đắp 0.2V sụt áp trên đường dây dài.
   - **Module MAX485 Master (RX)**: Thu sóng vi sai và dịch ngược thành chuỗi JSON đưa vào chân `RX2` (GPIO 16).
   - **Bộ Não ESP32 Master**: Tự phát trạm sóng Wi-Fi Access Point `CANH_BAO_KHI_DOC` và chạy Web SCADA theo thời gian thực.
   - **Màn hình OLED 0.96" SSD1306**: Hiển thị bảng số liệu trực quan tại chỗ.
   - **Hệ thống Còi Hú & 3 Đèn LED**: Còi báo động (GPIO 23), LED Đỏ (GPIO 19), LED Vàng (GPIO 5), LED Xanh (GPIO 18).

---

## 🚀 Trải Nghiệm Sơ Đồ Đi Dây Kỹ Thuật (Web App)

1. **Khởi động**:
   - Mở trực tiếp file [`index.html`](index.html) bằng trình duyệt web bất kỳ (Chrome, Edge, Safari, Firefox).
   - Hoặc bật GitHub Pages trên nhánh `main` để truy cập trực tuyến trên điện thoại và máy tính.

2. **Các tính năng nổi bật**:
   - **UX/UI chuẩn Mobile App**: Tích hợp Bottom Navigation Bar 5 tab, Slide-over Drawer, Bottom Sheet kéo vuốt và nút thao tác nhanh FAB.
   - **100% Đường Dây Trực Quan**: 43 dây nối màu sắc chuẩn kỹ thuật, hiển thị sắc nét tức thì.
   - **Mô phỏng âm thanh còi hú thực tế (Web Audio API)**:
     - *Mức An Toàn*: Đèn xanh sáng, không có còi.
     - *Mức Cảnh Báo*: Đèn vàng sáng, còi chíp bíp ngắt quãng.
     - *Mức Nguy Hiểm*: Đèn đỏ chớp giật liên tục, còi hú dồn dập, còi rung lắc trực quan.
     - Tùy chọn Bật/Tắt âm thanh còi ngay trên thanh công cụ.
   - **Cẩm nang Lớp 9**: Giải thích nguyên lý đấu nối bằng câu chuyện "Hai người thám hiểm hầm tối" dễ hiểu nhất cho học sinh và phụ huynh.
   - **Hiệu năng 60 FPS mượt mà**: Tối ưu hóa GPU phần cứng, không giật lag khi xoay chuyển phóng to thu nhỏ.

---

## 📂 Cấu Trúc Mã Nguồn

```
canhbaokhi/
├── index.html                 # Ứng dụng Web Sơ đồ Đi Dây Kỹ Thuật & Giám sát SCADA (Chạy trực tiếp)
├── wokwi-elements.bundle.js   # Bộ thư viện linh kiện Wokwi 3D
├── code.ino                   # Mã nguồn nhúng Arduino C++ cho ESP32
├── images/                    # Hình ảnh sơ đồ mạch & cảm biến thực tế
│   ├── board_esp32.png
│   ├── sensor_o2.png
│   ├── sensor_mq7.png
│   ├── sensor_mq4.png
│   ├── sensor_dht22.png
│   ├── hinh1_so_do_khoi_tong_the.png
│   ├── hinh2_phan_tang_khi_va_dau_do.png
│   ├── hinh2_so_do_mach_dien.png
│   ├── hinh3_luu_do_thuat_toan.png
│   ├── hinh3_so_do_mach_dien.png
│   ├── hinh4_luu_do_thuat_toan.png
│   ├── hinh4_phan_tang_khi_va_dau_do.png
│   └── hinh5_giao_dien_web_scada.png
├── mo_phong_3d_noi_day/       # Thư mục phụ hỗ trợ tương thích đường dẫn cũ
│   ├── index.html
│   ├── wokwi-elements.bundle.js
│   ├── esp32_glb_data.js
│   └── images/
├── .gitignore
└── README.md                  # Hướng dẫn dự án
```

---

*Tác giả & Bản quyền: Dự án Khoa Học Kỹ Thuật Học Sinh THCS - 2026*