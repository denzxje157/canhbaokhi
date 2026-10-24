# SỔ NHẬT KÝ NGHIÊN CỨU (RESEARCH LOGBOOK)
### THEO MẪU QUY ĐỊNH PHỤ LỤC 2 (KÈM THEO KẾ HOẠCH HƯỚNG DẪN CUỘC THI KHKT)

**TÊN ĐỀ TÀI: THIẾT BỊ CẢNH BÁO KHÍ ĐỘC VÀ THIẾU OXYGEN TRONG KHÔNG GIAN KÍN**
- **Lĩnh vực:** Hệ thống nhúng
- **Người thực hiện:** Nhóm học sinh Nghiên cứu Dự án
- **Thời gian thực hiện:** 10/06/2026 – 19/06/2026 (10 ngày làm việc thực tế)
- **Địa điểm:** Phòng thực hành STEM

---

## NGÀY: 10/06/2026                                                                    TRANG: 3
**GIAI ĐOẠN: Tìm hiểu tài liệu và lên ý tưởng thiết kế**
*THỜI GIAN: Từ 08h00 đến 16h30*

### 1. MỤC TIÊU
• Giám sát nguy cơ ngạt khí (O2), ngộ độc (CO) và cháy nổ (CH4) trong không gian kín (hầm, bồn chứa, cống ngầm, hố sâu).
• Tra cứu tiêu chuẩn (QCVN 34:2018/BLĐTBXH, QCVN 02:2019/BYT, OSHA) xác định ngưỡng cảnh báo nguy hiểm.
• Lên kiến trúc hệ thống 2 khối (Trong không gian kín và Mặt đất) kết nối cáp mạng qua chuẩn truyền thông RS485.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Máy tính kết nối Internet phòng STEM; công cụ AI: Claude, Grok, Gemini (tra cứu tài liệu và lên kế hoạch).
• Các văn bản tiêu chuẩn: QCVN 34:2018/BLĐTBXH, QCVN 02:2019/BYT, OSHA; Sổ ghi chép, bút.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Nhóm sử dụng công cụ Claude, Grok, Gemini tra cứu tiêu chuẩn an toàn lao động (QCVN 34, QCVN 02, OSHA).
2. Xác định các ngưỡng nồng độ cảnh báo theo 3 cấp độ tương ứng đèn và còi báo (lập bảng phân định):

| Cấp độ | Màu LED / Còi | Điều kiện kích hoạt | Trạng thái môi trường |
| :---: | :---: | :--- | :--- |
| MỨC NGUY HIỂM | LED ĐỎ sáng<br>+ CÒI hú dồn dập | O2 < 18.0%<br>HOẶC CO >= 30.0 ppm<br>HOẶC CH4 >= 10.0% LEL | Thiếu oxy nặng gây ngạt thở, khí độc CO vượt ngưỡng hoặc khí gas có nguy cơ bắt lửa nổ. Rút khỏi không gian kín ngay lập tức. |
| MỨC CẢNH BÁO | LED VÀNG sáng<br>+ Tắt còi | O2 <= 19.5% (nhưng >= 18.0%)<br>HOẶC CO >= 15.0 ppm (nhưng < 30.0 ppm)<br>HOẶC CH4 >= 5.0% LEL (nhưng < 10.0% LEL) | Khí quyển bắt đầu suy giảm chất lượng, cần theo dõi sát sao, chuẩn bị bật quạt thông gió. |
| MỨC AN TOÀN | LED XANH sáng<br>+ Tắt còi | O2 > 19.5%<br>VÀ CO < 15.0 ppm<br>VÀ CH4 < 5.0% LEL | Môi trường bình thường, đủ dưỡng khí và không có khí độc/khí cháy. |

3. Lên kiến trúc hệ thống 2 khối: Khối Trong Không Gian Kín (Slave - thu thập dữ liệu) và Khối Mặt Đất (Master - hiển thị, phát chuông/đèn báo động).
4. Thảo luận và thống nhất chọn giải pháp truyền thông có dây RS485 (chống nhiễu, truyền xa ổn định).

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Bảng phân định 3 cấp độ an toàn đã hoàn thiện; Sơ đồ kiến trúc 2 khối kết nối đường truyền RS485.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Không gian kín thành vách dày cản trở sóng vô tuyến, do đó bắt buộc dùng truyền thông có dây RS485 để dữ liệu ổn định.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai tìm hiểu thông số kỹ thuật và lựa chọn linh kiện, thiết bị cho 2 khối.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 11/06/2026                                                                    TRANG: 4
**GIAI ĐOẠN: Tìm hiểu và lựa chọn linh kiện, thiết bị**
*THỜI GIAN: Từ 08h00 đến 16h30*

### 1. MỤC TIÊU
• Khảo sát thông số kỹ thuật các linh kiện và lựa chọn linh kiện phù hợp cho dự án.
• Tính toán công suất tiêu thụ nguồn và thiết kế sơ đồ nguyên lý phân bổ chân I/O.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Máy tính kết nối Internet.
• Các công cụ AI: Claude, Grok, Gemini (sử dụng để tra cứu datasheet, tìm hiểu thông số thiết bị).
• Giấy vẽ sơ đồ mạch, thước kẻ, bút.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Nhóm sử dụng Claude, Grok, Gemini để khảo sát thông số kỹ thuật các linh kiện:
   - Vi điều khiển: ESP32 NodeMCU-32S (xử lý mạnh mẽ, tích hợp UART phần cứng).
   - Cảm biến khí cháy: MQ-4 (đặc tính phát hiện Metan CH4).
   - Cảm biến khí độc: MQ-7 (đặc tính phát hiện Carbon Monoxide CO).
   - Cảm biến Oxy: DFRobot Oxygen Sensor (giao tiếp I2C độ chính xác cao).
   - Cảm biến môi trường: DHT22 (nhiệt độ và độ ẩm).
   - Module chuyển đổi tín hiệu: MAX485 (giao tiếp vi sai half-duplex).
   - Hiển thị & Cảnh báo: Màn hình OLED SSD1306 (I2C), còi Buzzer, hệ thống LED 3 màu (Xanh, Vàng, Đỏ).
   - Khối nguồn: Module nguồn hạ áp Buck LM2596, khối pin 18650, công tắc nguồn.
2. Tính toán công suất tiêu thụ nguồn của các cảm biến và thiết kế sơ đồ nguyên lý phân bổ chân I/O cho vi điều khiển ESP32.

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Danh sách linh kiện đã chốt: ESP32 NodeMCU-32S (2 bo), MQ-4, MQ-7, DHT22, DFRobot Oxy, MAX485 (2 cái), OLED SSD1306, còi Buzzer, LED 3 màu, LM2596, pin 18650, cuộn cáp mạng 8 lõi (Cat5e).
• Sơ đồ nguyên lý phân bổ chân I/O hoàn thành trên giấy.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Hai cảm biến khí MQ có sợi nung nhiệt tiêu thụ dòng lớn, cần tính toán mạch nguồn LM2596 cấp đủ dòng.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai tiến hành đi mua sắm đầy đủ linh kiện và vật tư phụ trợ theo danh mục.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 12/06/2026                                                                    TRANG: 5
**GIAI ĐOẠN: Mua sắm linh kiện và vật tư phụ trợ**
*THỜI GIAN: Từ 08h30 đến 17h00*

### 1. MỤC TIÊU
• Mua đầy đủ các module cảm biến, vi điều khiển ESP32, module nguồn, cáp mạng và phụ kiện vỏ hộp.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Danh mục linh kiện đã lập ở Ngày 2.
• Tiền mặt quỹ của nhóm.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Đi mua đầy đủ các module cảm biến (MQ-4, MQ-7, DHT22, DFRobot Oxy) và vi điều khiển ESP32 (Học sinh tự làm).
2. Mua module nguồn hạ áp Buck LM2596, khối pin 18650, công tắc nguồn và phụ kiện vỏ hộp (Học sinh tự làm).
3. Mua module MAX485, màn hình OLED 0.96 inch, còi chíp, LED, điện trở hạn dòng và cuộn cáp mạng 8 lõi Cat5e (Học sinh tự làm).

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Mua đủ 100% linh kiện theo danh mục: 2 bo ESP32, cảm biến Oxy DFRobot, MQ-4, MQ-7, DHT22, 2 module MAX485, OLED 0.96 inch, còi Buzzer, LED, điện trở, module Buck LM2596, khối pin 18650, công tắc nguồn, phụ kiện vỏ hộp, cuộn cáp mạng 8 lõi Cat5e.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Cần kiểm tra kỹ chân cắm của các cảm biến và mạch nguồn trước khi rời cửa hàng.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai cấp nguồn và nạp code mẫu độc lập để kiểm tra từng module cảm biến và màn hình trên breadboard.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 13/06/2026                                                                    TRANG: 6
**GIAI ĐOẠN: Kiểm tra (test) từng module cảm biến và màn hình**
*THỜI GIAN: Từ 08h00 đến 16h30*

### 1. MỤC TIÊU
• Cấp nguồn và nạp code mẫu độc lập để kiểm tra từng linh kiện trên breadboard trước khi lắp ráp cố định.
• Đảm bảo tất cả linh kiện mua về đều hoạt động bình thường.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Bo ESP32, breadboard, dây cắm.
• Màn hình OLED SSD1306, cảm biến Oxy DFRobot, DHT22, MQ-4, MQ-7.
• Máy tính cài Arduino IDE, cáp nạp code.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Cấp nguồn và nạp code mẫu độc lập để kiểm tra từng linh kiện trên breadboard (Học sinh tự làm):
   - Màn hình OLED SSD1306: Quét địa chỉ I2C (0x3C), hiển thị text và thông số đồ họa.
   - Cảm biến Oxy DFRobot: Kiểm tra giao tiếp I2C (địa chỉ 0x73), xác nhận chỉ số đọc không khí thường đạt ~20.9%.
   - Cảm biến DHT22: Kiểm tra khả năng đọc nhiệt độ và độ ẩm phòng.
   - Cảm biến MQ-4 và MQ-7: Cấp nguồn sấy nhiệt sơ bộ, đo điện áp chân Analog (A0) qua bộ ADC 12-bit của ESP32.

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Màn hình OLED quét thấy địa chỉ 0x3C, hiển thị text và đồ họa bình thường.
• Cảm biến Oxy DFRobot đọc không khí thường đạt ~20.8% - 20.9%.
• Cảm biến DHT22 đọc nhiệt độ và độ ẩm phòng bình thường.
• Cảm biến MQ-4 và MQ-7 sấy nhiệt sơ bộ tốt, điện áp Analog ổn định.
• Tất cả linh kiện mua về đều hoạt động bình thường trước khi lắp ráp cố định.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Cảm biến MQ cần cấp nguồn sấy nhiệt sơ bộ vài phút để điện áp Analog ổn định.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai tiến hành gia công, lắp ráp, hàn mạch và đi dây phần cứng lên bo mạch đục lỗ.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 14/06/2026                                                                    TRANG: 7
**GIAI ĐOẠN: Gia công, lắp ráp, hàn mạch và đi dây phần cứng**
*THỜI GIAN: Từ 08h00 đến 17h00*

### 1. MỤC TIÊU
• Hàn cố định các khối linh kiện lên bo mạch đục lỗ.
• Đi dây cấp nguồn, đấu dây tín hiệu nội bộ giữa vi điều khiển và các ngoại vi theo sơ đồ thiết kế.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Bo mạch đục lỗ, mỏ hàn, thiếc hàn, nhựa thông, kìm cắt.
• Bo ESP32, OLED, còi Buzzer, LED, MAX485, cảm biến Oxy, DHT22, MQ-4, MQ-7, dây nối.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Tiến hành hàn cố định các khối linh kiện lên bo mạch đục lỗ (Học sinh tự làm):
   - Bo Mặt Đất: Hàn cố định OLED, hệ thống còi Buzzer, 3 đèn LED báo trạng thái và module MAX485.
   - Bo Trong Không Gian Kín: Bố trí cụm cảm biến (Oxy, DHT22, MQ-4, MQ-7) và module MAX485 trong hộp bảo vệ.
2. Đi dây cấp nguồn, đấu dây tín hiệu nội bộ giữa vi điều khiển và các ngoại vi theo sơ đồ thiết kế (Học sinh tự làm).

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Hàn xong phần cứng Bo Mặt Đất: ESP32 kết nối với OLED, còi Buzzer, 3 LED và MAX485.
• Hàn xong phần cứng Bo Trong Không Gian Kín: ESP32 kết nối với Oxy, DHT22, MQ-4, MQ-7 và MAX485.
• Các đường dây cấp nguồn và tín hiệu nội bộ được đấu nối chắc chắn.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Cần kiểm tra cẩn thận các mối hàn gần nhau để không bị chạm chì gây chập nguồn.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai hoàn thiện lắp ráp vào khung hộp, khoét lỗ thông khí và kiểm tra thông mạch.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 15/06/2026                                                                    TRANG: 8
**GIAI ĐOẠN: Hoàn thiện lắp ráp và xử lý các hạng mục dang dở**
*THỜI GIAN: Từ 08h00 đến 16h30*

### 1. MỤC TIÊU
• Hoàn thiện phần cơ khí: cố định bo mạch vào khung hộp, khoét lỗ thông khí cho các đầu lưới cảm biến khí và màn hình hiển thị.
• Kiểm tra thông mạch bằng đồng hồ vạn năng (VOM), kiểm tra tiếp xúc chân hàn để loại trừ nguy cơ ngắn mạch hoặc chạm chập nguồn.
• Tích hợp công tắc nguồn để chuẩn bị cho việc kết nối cáp truyền dẫn đường dài.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Khung hộp bảo vệ, máy khoan khoét lỗ mini, dao rọc giấy, súng bắn keo.
• Đồng hồ vạn năng VOM.
• Công tắc nguồn, dây dẫn.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Tiếp tục hoàn thiện phần cơ khí: cố định bo mạch vào khung hộp, khoét lỗ thông khí cho các đầu lưới cảm biến khí và khoét khe cho màn hình hiển thị OLED (Học sinh tự làm).
2. Kiểm tra thông mạch bằng đồng hồ vạn năng (VOM), kiểm tra tiếp xúc chân hàn để loại trừ nguy cơ ngắn mạch hoặc chạm chập nguồn (Học sinh tự làm).
3. Tích hợp công tắc nguồn để chuẩn bị cho việc kết nối cáp truyền dẫn đường dài (Học sinh tự làm).

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Bo mạch được cố định vào khung hộp bảo vệ; đầu lưới cảm biến hướng ra lỗ thông khí.
• Đo kiểm bằng đồng hồ VOM: Các mối hàn tiếp xúc tốt, không bị ngắn mạch giữa cực Dương và Mass.
• Công tắc nguồn bật tắt đóng ngắt điện tốt.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Khoét lỗ thông khí cho cảm biến vừa vặn với kích thước đầu lưới để thông thoáng khí.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai đấu nối cáp mạng truyền dẫn dài giữa bo Mặt Đất và bo Trong Không Gian Kín.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 16/06/2026                                                                    TRANG: 9
**GIAI ĐOẠN: Đấu nối cáp truyền dẫn đường dài – Phát hiện sự cố sụt áp**
*THỜI GIAN: Từ 08h00 đến 17h00*

### 1. MỤC TIÊU
• Đấu nối cáp mạng 8 lõi giữa bo Mặt Đất và bo Trong Không Gian Kín.
• Kiểm tra hoạt động của hệ thống khi kéo dây dài.
• Ghi nhận các vấn đề kỹ thuật phát sinh thực tế.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Cuộn cáp mạng 8 lõi Cat5e (chiều dài 4 – 5 mét của mô hình).
• Bo Mặt Đất, Bo Trong Không Gian Kín, bộ nguồn pin.
• Đồng hồ vạn năng VOM, máy tính.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Đấu nối cáp mạng 8 lõi giữa bo Mặt Đất và bo Trong Không Gian Kín theo cách đấu thông thường (1 cặp dây cấp nguồn 5V/GND, 1 cặp dây tín hiệu RS485) (Học sinh tự làm).
2. Vấn đề phát sinh thực tế:
   - Khi bật nguồn, cụm cảm biến MQ nung nhiệt tiêu thụ dòng lớn làm xảy ra hiện tượng sụt áp nghiêm trọng trên đường dây dẫn dài.
   - Điện áp ở đầu bo trong không gian kín tụt xuống dưới 4.5V, khiến ESP32 bo dưới bị thiếu áp, liên tục reset hoặc treo chip, dữ liệu truyền lên bị gián đoạn.
3. Tìm giải pháp: Nghiên cứu phương án ghép song song các lõi dây dẫn của cáp mạng để giảm tối đa nội trở đường dây, bù sụt áp.

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Đo điện áp tại đầu phát bo Mặt Đất: 5.0V.
• Điện áp đo tại đầu bo dưới: Tụt xuống dưới 4.5V (khi cảm biến MQ sấy nóng thì tụt còn ~4.0V).
• Hiện tượng: ESP32 bo dưới bị thiếu áp, liên tục reset hoặc treo chip, dữ liệu truyền lên bị gián đoạn.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Đấu nối 1 cặp dây thông thường cho cáp dài bị sụt áp lớn do dòng nung của cảm biến MQ.
• Giải pháp: Cần ghép song song các lõi dây của cáp mạng để giảm nội trở đường dây theo công thức Vật lý.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai tái cấu hình đấu dây theo giải pháp 3/3/2 và điều chỉnh mạch LM2596 để bù sụt áp.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 17/06/2026                                                                    TRANG: 10
**GIAI ĐOẠN: Tái cấu hình đấu dây theo giải pháp 3/3/2 – Khắc phục thành công sụt áp**
*THỜI GIAN: Từ 08h00 đến 16h30*

### 1. MỤC TIÊU
• Tái cấu hình đấu dây cáp mạng theo giải pháp 3/3/2 để triệt tiêu sụt áp.
• Điều chỉnh mạch Buck LM2596 bù áp đầu ra.
• Khắc phục triệt để hiện tượng reset chip, đảm bảo truyền dữ liệu thông suốt.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Cáp mạng 8 lõi Cat5e, kìm tuốt dây, mỏ hàn thiếc.
• Mạch Buck LM2596, tua-vít chỉnh chiết áp.
• Đồng hồ vạn năng VOM.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Đấu nối lại toàn bộ 8 lõi cáp mạng theo quy tắc phân bổ 3/3/2 (Học sinh tự làm):
   - Chập 3 lõi cấp nguồn 5V: Cam, Trắng - Cam, Trắng - Nâu.
   - Chập 3 lõi cấp Mass (GND): Nâu, Xanh Lá, Trắng - Xanh Lá.
   - 2 lõi truyền tín hiệu RS485: Xanh Dương (chân A) và Trắng - Xanh Dương (chân B).
2. Điều chỉnh mạch Buck LM2596 đưa áp đầu ra lên khoảng 5.2V để bù sụt áp (Học sinh tự làm).
3. Bật nguồn và đo kiểm điện áp tại chân VIN của bo dưới.

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Điện áp đo tại chân VIN của bo trong không gian kín đạt chuẩn ~4.9V - 5.0V.
• Bo hoạt động ổn định, 2 cảm biến MQ nóng đều và module MAX485 truyền dữ liệu thông suốt không còn bị treo.
• Số liệu cảm biến hiển thị liên tục lên màn hình OLED của bo Mặt Đất.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Giải pháp phân bổ 3/3/2 kết hợp chỉnh áp LM2596 lên 5.2V đã khắc phục thành công sự cố sụt áp.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai kiểm thử chức năng cảm biến và vận hành liên tục toàn hệ thống.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 18/06/2026                                                                    TRANG: 11
**GIAI ĐOẠN: Kiểm thử (Test) chức năng và vận hành liên tục toàn hệ thống**
*THỜI GIAN: Từ 08h00 đến 17h00*

### 1. MỤC TIÊU
• Cho hệ thống chạy liên tục để kiểm tra độ tin cậy của đường truyền RS485.
• Test cảm biến khí cháy MQ-4 và cảm biến Oxy.
• Kiểm tra đáp ứng kích hoạt còi và đèn cảnh báo theo logic thiết kế.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Toàn bộ thiết bị đã kết nối hoàn chỉnh (Master và bo dưới qua cáp 4 – 5m).
• Bật lửa ga (nhấn xả ga nguội, không đánh lửa).
• Cốc úp ngược, que lửa (hoặc nến nhỏ) để triệt tiêu Oxy.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Cho hệ thống chạy liên tục để kiểm tra độ tin cậy của đường truyền RS485 (Học sinh tự làm).
2. Test cảm biến khí cháy MQ-4: Dùng bật lửa ga (nhấn xả ga nguội, không đánh lửa) xịt vào đầu đo; nồng độ CH4 (% LEL) tăng vọt ngay trên màn hình (Học sinh tự làm).
3. Test cảm biến Oxy: Dùng cốc úp ngược và đốt que lửa bên trong để triệt tiêu Oxy; chỉ số O2 tụt xuống dưới 19.5% và tiếp tục tụt xuống dưới 18% (Học sinh tự làm).
4. Kiểm tra đáp ứng cảnh báo: Khi chỉ số chạm ngưỡng nguy hiểm, bo Mặt Đất lập tức chuyển LED sang Đỏ và hú còi Buzzer liên tục đúng theo logic thiết kế (Học sinh tự làm).

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Test MQ-4: Khi xịt ga nguội, nồng độ CH4 (% LEL) tăng vọt ngay trên màn hình, LED chuyển Đỏ, còi hú to.
• Test Oxy: Khi đốt que lửa trong cốc úp ngược, chỉ số O2 tụt xuống dưới 19.5% rồi xuống dưới 18.0%, còi hú liên tục.
• Đường truyền RS485 duy trì liên tục và tin cậy suốt buổi thử nghiệm.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Khi test khí ga chỉ nhấn xả ga nguội, không đánh lửa để đảm bảo an toàn tuyệt đối.

### 6. KẾ HOẠCH TIẾP THEO
• Ngày mai bọc ghen co nhiệt hoàn thiện thiết bị, tinh chỉnh lọc trung bình ADC và lập dàn ý báo cáo.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## NGÀY: 19/06/2026                                                                    TRANG: 12
**GIAI ĐOẠN: Tinh chỉnh hoàn thiện và lập dàn ý báo cáo**
*THỜI GIAN: Từ 08h00 đến 16h30*

### 1. MỤC TIÊU
• Bọc ghen co nhiệt, đóng nắp hộp bảo vệ hoàn chỉnh cho cả 2 khối thiết bị.
• Tinh chỉnh lại các tham số làm mượt dữ liệu (lọc trung bình mẫu ADC) trong code để kết quả hiển thị trên OLED ổn định nhất.
• Lập dàn ý, tổng hợp thông số kỹ thuật, hình ảnh thực nghiệm và các tiêu chuẩn viện dẫn để phục vụ viết thuyết minh/báo cáo đề tài.

### 2. DỤNG CỤ & VẬT LIỆU SỬ DỤNG
• Ghen co nhiệt, bật lửa hơ ghen, tua-vít đóng nắp hộp.
• Máy tính cài Arduino IDE để nạp code hoàn thiện.
• Toàn bộ sổ ghi chép, thông số kỹ thuật đo kiểm trong 10 ngày.

### 3. TIẾN TRÌNH THỰC HIỆN & HIỆN TƯỢNG
1. Bọc ghen co nhiệt các mối nối, đóng nắp hộp bảo vệ hoàn chỉnh cho cả 2 khối thiết bị (Học sinh tự làm).
2. Tinh chỉnh lại các tham số làm mượt dữ liệu (lọc trung bình mẫu ADC) trong code để kết quả hiển thị trên OLED ổn định nhất (Học sinh tự làm).
3. Lập dàn ý, tổng hợp thông số kỹ thuật, hình ảnh thực nghiệm và các tiêu chuẩn viện dẫn để phục vụ viết thuyết minh/báo cáo đề tài (Học sinh tự làm).

### 4. KẾT QUẢ & SỐ LIỆU THÔ
• Cả 2 khối thiết bị được đóng nắp hộp gọn gàng, các mối nối bọc ghen co nhiệt chắc chắn.
• Màn hình OLED hiển thị số đo ổn định và mượt mà.
• Hoàn thành xong dàn ý báo cáo đề tài khoa học.

### 5. RÚT KINH NGHIỆM & LỖI SAI
• Tinh chỉnh lọc trung bình mẫu ADC giúp số đo trên OLED ổn định, không bị dao động nhỏ.

### 6. KẾ HOẠCH TIẾP THEO
• Bắt tay vào viết báo cáo khoa học chi tiết và chuẩn bị hồ sơ dự thi.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*

---

## PHỤ LỤC: TÀI LIỆU THAM KHẢO & NGUỒN TRA CỨU                                    TRANG: 13
*(Danh mục các quy chuẩn an toàn lao động, sách giáo khoa và tài liệu kỹ thuật nhóm đã tra cứu trong quá trình thực hiện dự án)*

1. Bộ Lao động - Thương binh và Xã hội (2018), Quy chuẩn kỹ thuật quốc gia về an toàn lao động khi làm việc trong không gian hạn chế (QCVN 34:2018/BLĐTBXH).
2. Bộ Y tế (2019), Quy chuẩn kỹ thuật quốc gia về giới hạn tiếp xúc cho phép của 50 yếu tố hóa học tại nơi làm việc (QCVN 02:2019/BYT).
3. Nhóm tác giả Sách giáo khoa, Khoa học tự nhiên lớp 8 (Chủ đề Không khí - Dưỡng khí Oxygen), NXB Giáo dục Việt Nam.
4. Nhóm tác giả Sách giáo khoa, Khoa học tự nhiên lớp 9 (Bài Định luật Ohm và Điện trở của dây dẫn R = ρ · l / S), NXB Giáo dục Việt Nam.
5. Zhengzhou Winsen Electronics Technology Co., Ltd, Technical Data: MQ-4 Gas Sensor & MQ-7 Carbon Monoxide Sensor.
6. DFRobot, Gravity: I2C Oxygen Sensor Manual (SEN0322).
7. Espressif Systems, ESP32 NodeMCU-32S Datasheet & Pinout Reference.
8. Các công cụ AI hỗ trợ tra cứu tài liệu khoa học và gợi ý quy chuẩn an toàn trong Ngày 1 và Ngày 2: Claude, Grok, Gemini.

**Chữ ký của Học sinh:** *[Đã ký]*                **Chữ ký của Giáo viên hướng dẫn:** *[Đã ký]*
