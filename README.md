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

## 🚀 Hướng Dẫn Chạy Sơ Đồ Đi Dây Kỹ Thuật 3D

1. **Khởi động nhanh**:
   - Nhấp đúp vào tệp [`Mo_Phong_3D.bat`](Mo_Phong_3D.bat).
   - Hoặc mở trực tiếp [`mo_phong_3d_noi_day/index.html`](mo_phong_3d_noi_day/index.html) bằng bất kỳ trình duyệt web nào (Chrome, Edge, Firefox).

2. **Các tính năng nổi bật của bản mô phỏng**:
   - **Sơ đồ đi dây chuẩn công nghiệp**: Đường dây Manhattan vuông vức, không bị chéo góc, không che chữ.
   - **Mô phỏng âm thanh còi hú thực tế (Web Audio API)**:
     - *Mức An Toàn*: Đèn xanh sáng, không có còi.
     - *Mức Cảnh Báo*: Đèn vàng sáng, còi chíp bíp ngắt quãng.
     - *Mức Nguy Hiểm*: Đèn đỏ chớp giật liên tục, còi hú dồn dập, còi rung lắc trực quan.
     - Nút bật/tắt âm thanh còi tiện lợi ngay trên thanh điều khiển.
   - **Bộ lọc mạch nhanh**: Bật sáng 100% toàn bộ 43 đường dây hoặc lọc riêng từng module.
   - **Cẩm nang Lớp 9**: Giải thích nguyên lý đấu nối bằng ngôn ngữ hình tượng học sinh dễ hiểu nhất để tự tin trả lời Ban giám khảo.
   - **Hiệu năng 60 FPS mượt mà**: Tối ưu hóa GPU phần cứng, không giật lag khi xoay chuyển phóng to thu nhỏ.

---

## 📂 Cấu Trúc Thư Mục

```
canhbaokhi/
├── mo_phong_3d_noi_day/           # Ứng dụng Web Mô phỏng Đi Dây & Giám sát SCADA
│   ├── index.html                 # Giao diện chính Sơ đồ Đi Dây Kỹ Thuật
│   ├── wokwi-elements.bundle.js   # Bộ thư viện linh kiện Wokwi 3D
│   └── images/                    # Hình ảnh cảm biến thực tế
├── Mo_Phong_3D.bat                # Phím tắt 1-click mở mô phỏng trên Windows
├── code.ino                       # Mã nguồn nhúng Arduino C++ cho ESP32
├── Bai_Thuyet_Trinh_Canh_Bao_Khi_Doc_THCS.pptx   # Slide thuyết trình KHKT
├── BaoCao_KHKT_CanhBaoKhi_THCS.pdf              # Bản báo cáo nghiên cứu hoàn chỉnh
├── So_Nhat_Ky_Nghien_Cuu_Canh_Bao_Khi_Doc.pdf   # Sổ nhật ký nghiên cứu
├── Kich_Ban_Thuyet_Trinh_Lop9_Canh_Bao_Khi_Doc.pdf # Kịch bản trả lời giám khảo
└── README.md                      # Tài liệu dự án
```

---

*Tác giả & Bản quyền nghiên cứu: Dự án Khoa Học Kỹ Thuật Học Sinh THCS - 2026*