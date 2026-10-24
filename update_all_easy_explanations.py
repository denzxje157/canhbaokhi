import os
import re

path = os.path.abspath(r'mo_phong_3d_noi_day\index.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Sửa lỗi hiển thị công thức LaTeX trong Modal nếu có
text = text.replace(r'\( R = ho \cdot rac{l}{S} \)', r'\( R = \rho \cdot \frac{l}{S} \)')
text = text.replace(r'R = ho \cdot rac{l}{S}', r'R = \rho \cdot \frac{l}{S}')

# Cập nhật mảng COMPONENTS với lời giải thích dễ hiểu 100% cho học sinh lớp 9
new_components_code = r'''    const COMPONENTS = [
      {
        id: "o2_sensor",
        name: "Cảm Biến Oxygen (O2)",
        sub: "DFRobot Gravity I2C (SEN0496 / SEN0322)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Chiếc mũi ngửi dưỡng khí Oxy",
        repo: "DFRobot/DFRobot_OxygenSensor",
        repoUrl: "https://github.com/DFRobot/DFRobot_OxygenSensor",
        color: "#0284c7",
        icon: "fa-lungs",
        pins: [
          { from: "SDA (Data)", to: "GPIO 21 (D21)", note: "Dây đọc con số nồng độ Oxy" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22)", note: "Dây gõ nhịp đồng hồ tíc-tắc" },
          { from: "VCC (Nguồn)", to: "VCC 5V Power Rail", note: "Dây cấp điện 5V nuôi cảm biến sống" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Dây cực âm khép kín dòng điện" }
        ],
        codeSnippet: `// Khởi tạo thư viện DFRobot_OxygenSensor theo chuẩn I2C\n#include "DFRobot_OxygenSensor.h"\n#define Oxygen_IICAddress ADDRESS_3 // 0x73 mặc định\nDFRobot_OxygenSensor oxygen;\n\nvoid setup() {\n  Wire.begin(21, 22); // SDA=21, SCL=22 phần cứng\n  while(!oxygen.begin(Oxygen_IICAddress)) {\n    Serial.println("I2C Error!"); delay(1000);\n  }\n}\nfloat readO2() {\n  return oxygen.getOxygenData(10); // Đọc trung bình 10 lần\n}`,
        why: "TẠI SAO NỐI VÀO GPIO 21 (SDA) VÀ GPIO 22 (SCL)?",
        whyContent: "Cảm biến Oxy là loại cảm biến thông minh, nói chuyện với ESP32 bằng 2 dây kỹ thuật số (chuẩn I2C): dây SCL gõ nhịp đồng hồ tíc-tắc, còn dây SDA đọc to con số nồng độ Oxy (ví dụ 20.9%). Chân 21 và 22 là cổng I2C phần cứng có sẵn của ESP32, giúp 2 bên nói chuyện ăn ý với nhau cực nhanh (400.000 nhịp/giây) mà không bao giờ bị nghẽn CPU.",
        physicsTip: "💡 Khí quyển bình thường có 20.9% Oxy. Nếu dưới hầm tụt xuống < 18.0%, chỉ sau 30-40 giây não bộ sẽ mất ý thức ngất xỉu mà nạn nhân không hề hay biết!"
      },
      {
        id: "mq7_sensor",
        name: "Cảm Biến Khí Than Độc (CO)",
        sub: "Winsen MQ-7 (AO Analog Output)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Chiếc mũi ngửi khí than độc CO",
        repo: "miguel5612/MQSensorsLib",
        repoUrl: "https://github.com/miguel5612/MQSensorsLib",
        color: "#ea580c",
        icon: "fa-skull-crossbones",
        pins: [
          { from: "A0 (Analog)", to: "GPIO 35", note: "Chiếc micro gửi độ lớn dòng điện khí độc" },
          { from: "VCC (5V Nung)", to: "VCC 5V Power Rail", note: "Cấp điện 5V nung nóng lõi cảm biến" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp dòng điện nung lớn" }
        ],
        codeSnippet: `// Cấu hình thư viện MQUnifiedsensor cho MQ-7\n#include <MQUnifiedsensor.h>\n#define Pin 35 // ADC1 GPIO 35\nMQUnifiedsensor MQ7("ESP-32", 3.3, 12, Pin, "MQ-7");\n\nvoid setup() {\n  MQ7.init();\n  MQ7.setRegressionMethod(1); // PPM = a*ratio^b\n  MQ7.setA(99.042); MQ7.setB(-1.518); // Hệ số chuẩn khí CO\n}\nfloat readCO() {\n  MQ7.update();\n  return MQ7.readSensor();\n}`,
        why: "TẠI SAO CHÂN TÍN HIỆU A0 NỐI VÀO GPIO 35?",
        whyContent: "Chân A0 (Analog) là 'chiếc micro nói chuyện' của cảm biến khí than độc CO. Khi có khí than độc, lò nung trong cảm biến nóng lên và đẩy điện áp ra chân A0. ESP32 nhận tín hiệu này qua chân GPIO 35 (cổng đo điện áp độc lập ADC1). Khí độc càng nhiều thì điện áp gửi qua dây càng lớn, ESP32 chỉ cần đo độ mạnh yếu của điện áp là biết ngay có bao nhiêu hạt khí độc để báo động.",
        physicsTip: "💡 Khí CO chiếm ái lực với hồng cầu gấp 250 lần dưỡng khí Oxy. Mức >= 30 ppm là mức nguy hại phải bật còi báo khẩn cấp ngay."
      },
      {
        id: "mq4_sensor",
        name: "Cảm Biến Khí Gas/Metan (CH4)",
        sub: "Winsen MQ-4 (AO Analog Output)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Chiếc mũi ngửi khí Gas cháy nổ",
        repo: "miguel5612/MQSensorsLib",
        repoUrl: "https://github.com/miguel5612/MQSensorsLib",
        color: "#d97706",
        icon: "fa-fire-flame-simple",
        pins: [
          { from: "A0 (Analog)", to: "GPIO 34", note: "Gửi điện áp tỉ lệ với lượng khí gas" },
          { from: "VCC (5V Nung)", to: "VCC 5V Power Rail", note: "Cấp điện cho lò nung sấy nhiệt" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp mass chung" }
        ],
        codeSnippet: `// Cấu hình thư viện MQUnifiedsensor cho MQ-4\n#include <MQUnifiedsensor.h>\n#define PinMQ4 34 // ADC1 GPIO 34\nMQUnifiedsensor MQ4("ESP-32", 3.3, 12, PinMQ4, "MQ-4");\n\nvoid setup() {\n  MQ4.init();\n  MQ4.setRegressionMethod(1);\n  MQ4.setA(1012.7); MQ4.setB(-2.786); // Hệ số khí CH4\n}\nfloat readCH4_LEL() {\n  MQ4.update();\n  float ppm = MQ4.readSensor();\n  return (ppm / 50000.0) * 100.0; // 50,000 ppm = 100% LEL\n}`,
        why: "TẠI SAO CHÂN TÍN HIỆU A0 NỐI VÀO GPIO 34?",
        whyContent: "Tương tự như MQ-7, chân A0 của MQ-4 là chân truyền tín hiệu nồng độ khí Gas/Metan bốc lên từ bùn rác dưới cống. Khi lượng khí gas tăng, chân A0 sẽ gửi dòng điện áp tương ứng vào chân GPIO 34 của ESP32. ESP32 dưới đáy đọc số điện áp này để tính ra % nồng độ có nguy cơ gây cháy nổ (%LEL) hay không.",
        physicsTip: "💡 Giới hạn nổ dưới (LEL) của Metan là 5% thể tích. Khi đạt >= 10% LEL, tia lửa nhỏ từ giày dép hay kim loại va đập cũng có thể gây nổ hầm!"
      },
      {
        id: "dht22_sensor",
        name: "Cảm Biến Nhiệt Độ - Độ Ẩm",
        sub: "Aosong AM2302 (DHT22)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Nhiệt ẩm kế bù trừ sai số",
        repo: "adafruit/DHT-sensor-library",
        repoUrl: "https://github.com/adafruit/DHT-sensor-library",
        color: "#9333ea",
        icon: "fa-temperature-half",
        pins: [
          { from: "DATA (1-Wire)", to: "GPIO 4 (D4)", note: "Dây gửi xung nhịp nhiệt độ và độ ẩm" },
          { from: "VCC (Nguồn)", to: "VCC 5V Power Rail", note: "Nguồn nuôi cảm biến" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Chân mass chung" }
        ],
        codeSnippet: `// Khởi tạo thư viện Adafruit DHT\n#include "DHT.h"\n#define DHTPIN 4     // Nối vào GPIO 4\n#define DHTTYPE DHT22\nDHT dht(DHTPIN, DHTTYPE);\n\nvoid setup() {\n  dht.begin();\n}\nvoid readEnv(float &temp, float &hum) {\n  hum = dht.readHumidity();\n  temp = dht.readTemperature();\n}`,
        why: "TẠI SAO PHẢI ĐO NHIỆT ĐỘ VÀ ĐỘ ẨM (GPIO 4)?",
        whyContent: "Dưới cống rãnh ngầm độ ẩm lúc nào cũng tới 80-99% và rất nóng. Hơi nước nhiều sẽ bám vào cảm biến khí làm số đo bị sai lệch. Cảm biến DHT22 dùng chân DATA gửi xung điện chớp tắt siêu nhanh vào GPIO 4 để ESP32 biết trời đang nóng bao nhiêu độ và ẩm bao nhiêu %, từ đó tự động bù trừ sai số giúp không bao giờ bị báo động giả.",
        physicsTip: "💡 Dữ liệu nhiệt ẩm được chớp tắt bằng xung điện siêu ngắn (chỉ vài chục micro-giây) qua đúng 1 sợi dây duy nhất."
      },
      {
        id: "esp32_slave",
        name: "Vi Điều Khiển Dưới Đáy (Slave)",
        sub: "ESP32 NodeMCU 30 Chân (Thu thập & Gom gói)",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Chú lính trinh sát tí hon dưới đáy",
        repo: "kike-canaries/canairio_sensorlib",
        repoUrl: "https://github.com/kike-canaries/canairio_sensorlib",
        color: "#16a34a",
        icon: "fa-microchip",
        pins: [
          { from: "VIN (Nguồn)", to: "VCC 5V Power Rail", note: "Ăn điện từ cáp nguồn trên mặt đất cấp xuống" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp mass chung" },
          { from: "GPIO 17 (TX2)", to: "DI (MAX485 Slave)", note: "Bắn bức thư JSON sang loa phóng MAX485" },
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Slave)", note: "Cổng nhận nối tiếp UART2" }
        ],
        codeSnippet: `// Đóng gói JSON và gửi qua UART2 RS485\nvoid sendDataToMaster(float o2, float co, float ch4, float t, float h) {\n  String json = "{\\"o2\\":" + String(o2,1) + \n                ",\\"co\\":" + String(co,1) + \n                ",\\"ch4\\":" + String(ch4,1) + \n                ",\\"t\\":" + String(t,1) + \n                ",\\"h\\":" + String(h,1) + "}\\n";\n  Serial2.print(json); // Bắn lên qua MAX485\n}`,
        why: "CHÚ LÍNH ESP32 DƯỚI ĐÁY ĐÓNG GÓI TIN THẾ NÀO?",
        whyContent: "Sau khi nhận tín hiệu từ 4 chiếc 'mũi ngửi' (Oxy, CO, Metan, Nhiệt độ, Độ ẩm), ESP32 dưới đáy viết tất cả 5 con số vào một bức thư báo cáo (chuỗi JSON), ví dụ: {\"o2\":20.5, \"co\":0, \"ch4\":0, \"t\":28, \"h\":80}. Sau đó nó dùng chân TX2 (GPIO 17) đẩy bức thư này sang chip MAX485 để phóng lên mặt đất.",
        physicsTip: "💡 ESP32 có 2 bộ não (lõi kép) chạy 240 triệu phép tính/giây, gom gói bức thư 5 tham số chỉ mất chưa đầy 2 phần nghìn giây!"
      },
      {
        id: "max485_slave",
        name: "Module Chuyển Đổi MAX485 (Slave)",
        sub: "UART sang Vi Sai RS-485",
        group: "KHỐI KHÔNG GIAN KÍN (SLAVE)",
        badge: "Chiếc loa phóng thanh chống nhiễu",
        repo: "HardwareSerial RS-485",
        repoUrl: "https://github.com/kike-canaries/canairio_sensorlib",
        color: "#9333ea",
        icon: "fa-network-wired",
        pins: [
          { from: "DI", to: "GPIO 17 (TX2)", note: "Nhận bức thư từ ESP32" },
          { from: "RO", to: "GPIO 16 (RX2)", note: "Cổng nối tiếp UART2" },
          { from: "VCC & GND", to: "5V & GND Out (ESP32)", note: "Nguồn nuôi IC vi sai" },
          { from: "Chân A & B", to: "Cặp Xoắn Đôi Cáp Cat5e", note: "Cặp dây vi sai phóng tín hiệu đi xa" }
        ],
        codeSnippet: `// Cấu hình cổng Serial2 phần cứng cho MAX485\nvoid setup() {\n  Serial2.begin(9600, SERIAL_8N1, 16, 17);\n}`,
        why: "TẠI SAO PHẢI QUA MAX485 CHUYỂN THÀNH DÂY A VÀ B?",
        whyContent: "Dây từ dưới hầm lên mặt đất dài 20–30 mét, lại ẩm ướt và đầy sóng nhiễu. Nếu gửi thẳng tín hiệu điện thoại thông thường thì lên bờ sẽ bị méo mó, mất chữ. Con chip MAX485 đóng vai trò như 'chiếc loa phóng thanh': nó biến bức thư thành 2 luồng điện chạy trên 2 sợi dây A và B song song. Mọi sóng nhiễu đánh vào cả 2 dây sẽ tự động triệt tiêu lẫn nhau, đảm bảo bức thư truyền lên bờ nguyên vẹn 100%.",
        physicsTip: "💡 Nguyên lý vi sai: Tín hiệu = Dây A trừ Dây B. Nhiễu đánh vào cả 2 dây như nhau nên khi trừ nhau là nhiễu biến mất hoàn toàn!"
      },
      {
        id: "cable_cat5e",
        name: "Cáp Mạng Cat5e (Cụm 3 - 3 - 2)",
        sub: "Chiều dài thực tế 10m - 50m",
        group: "ĐƯỜNG TRUYỀN VẬT LÝ",
        badge: "Sáng kiến Vật lý 9 chống sụt áp",
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
        why: "TẠI SAO CHẬP CỤM 3 SỢI DƯƠNG VÀ 3 SỢI MASS (VẬT LÝ 9)?",
        whyContent: "Theo công thức Vật lý 9: R = rho * (l / S). Dây mạng rất mảnh (tiết diện S bé tí). Kéo dài 20m thì điện trở R rất lớn, làm dòng điện bị rơi rớt dọc đường (sụt áp), xuống đáy không đủ 5V để nuôi cảm biến nung. Sáng kiến của nhóm là chập 3 sợi làm 1 đường Dương và 3 sợi làm 1 đường Mass -> Tiết diện S tăng gấp 3 -> Điện trở R giảm 3 lần! Kết hợp vặn nguồn LM2596 lên 5.2V bù 0.2V rơi rớt, điện xuống tận đáy hầm luôn chuẩn đét 5.0V!",
        physicsTip: "💡 Đây là điểm sáng tạo đạt điểm tuyệt đối trước ban giám khảo vì áp dụng đúng bài Điện trở dây dẫn trong sách giáo khoa Vật lý 9!"
      },
      {
        id: "max485_master",
        name: "Module Chuyển Đổi MAX485 (Master)",
        sub: "RS-485 sang UART Vi Điều Khiển",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Người dịch tin trên mặt đất",
        repo: "HardwareSerial RS-485",
        repoUrl: "https://github.com",
        color: "#9333ea",
        icon: "fa-network-wired",
        pins: [
          { from: "Chân A & B", to: "Nhận từ Cáp Cat5e", note: "Đón nhận 2 luồng xung vi sai từ đáy hầm" },
          { from: "RO", to: "GPIO 16 (RX2 Master)", note: "Đưa chuỗi JSON vào tai ESP32 Master" },
          { from: "VCC & GND", to: "5V & GND Nguồn", note: "Nguồn nuôi module" }
        ],
        codeSnippet: `// Nhận chuỗi JSON từ Slave\nvoid loop() {\n  if (Serial2.available()) {\n    String json = Serial2.readStringUntil('\\n');\n    parseGasData(json); // Giải mã 5 thông số\n  }\n}`,
        why: "TẠI SAO CẦN CON MAX485 THỨ HAI TRÊN MẶT ĐẤT?",
        whyContent: "Tín hiệu đi trên 2 dây A-B là ngôn ngữ đường dài. Cần có con chip MAX485 thứ hai trên bờ làm nhiệm vụ 'người dịch tin': đón lấy cặp dây A-B, dịch ngược lại thành dòng chữ ban đầu và chuyển qua chân RO vào tai chú lính ESP32 Master trên mặt đất.",
        physicsTip: "💡 Cặp đôi MAX485 hai đầu cho phép truyền tín hiệu xa tới 1.200 mét mà không lo bị yếu tín hiệu."
      },
      {
        id: "lm2596",
        name: "Mạch Hạ Áp DC-DC LM2596",
        sub: "Hạ Áp Hiệu Suất Cao Xung BUCK (5.2V)",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Nhà máy điện cấp nguồn toàn hệ thống",
        repo: "Texas Instruments LM2596",
        repoUrl: "https://ti.com",
        color: "#0284c7",
        icon: "fa-bolt",
        pins: [
          { from: "OUT+ (5.2V)", to: "Cụm 3 Dây Dương Cáp Cat5e & VIN Master", note: "Chỉnh chiết áp lên 5.2V bù sụt áp đường dài" },
          { from: "OUT- (GND)", to: "Cụm 3 Dây Mass Cáp Cat5e & GND Master", note: "Cực âm chung toàn hệ thống" }
        ],
        codeSnippet: `// Hiệu suất chuyển đổi BUCK xung:\n// H = P_out / P_in > 90% (Mạch luôn mát, tiết kiệm ắc quy gấp đôi LM7805)`,
        why: "TẠI SAO CHỈNH NGUỒN LÊN 5.2V MÀ KHÔNG ĐỂ 5.0V?",
        whyContent: "Khi dòng điện chạy qua 20 mét dây cáp mạng, theo định luật Ohm sẽ có một lượng điện áp bị tiêu hao dọc đường (khoảng 0.2V). Nếu trên bờ chỉ để đúng 5.0V thì xuống đáy chỉ còn 4.8V khiến cảm biến chập chờn. Việc vặn ốc chiết áp nâng lên 5.2V là tính toán có chủ đích: 5.2V trừ đi 0.2V rơi rớt dọc đường sẽ vừa vặn đúng 5.0V chuẩn đét dưới đáy!",
        physicsTip: "💡 Mạch xung LM2596 chuyển đổi điện bằng cuộn cảm với hiệu suất > 90%, mạch luôn mát mẻ và giúp thiết bị chạy liên tục suốt 8-12 tiếng trên bình ắc quy nhỏ."
      },
      {
        id: "esp32_master",
        name: "Bộ Não Xử Lý & Web Server (Master)",
        sub: "Trung Tâm Phân Tích, Báo Động & Web SCADA",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Đội trưởng chỉ huy trên mặt đất",
        repo: "kike-canaries/canairio_sensorlib",
        repoUrl: "https://github.com/kike-canaries/canairio_sensorlib",
        color: "#2563eb",
        icon: "fa-microchip",
        pins: [
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Master)", note: "Nhận chuỗi dữ liệu JSON từ đáy" },
          { from: "GPIO 21 & 22", to: "OLED SSD1306 (SDA & SCL)", note: "Chiếu 5 số đo lên màn hình" },
          { from: "GPIO 23", to: "Còi Hú Báo Động (Buzzer)", note: "Bức tường âm thanh ngăn nhảy cứu" },
          { from: "GPIO 19, 5, 18", to: "LED Đỏ - Vàng - Xanh", note: "Báo động 3 cấp độ an toàn" },
          { from: "VIN & GND", to: "5.2V Nguồn & GND Chung", note: "Nuôi Master từ LM2596" }
        ],
        codeSnippet: `// Hàm xử lý còi đèn theo 3 cấp độ an toàn:\nvoid handleAlarm(float o2, float co, float ch4) {\n  bool isDanger = (o2 < 18.0 || co >= 30.0 || ch4 >= 10.0);\n  bool isWarning = (o2 <= 19.5 || co >= 15.0 || ch4 >= 5.0);\n  if (isDanger) {\n    digitalWrite(19, HIGH); // LED ĐỎ\n    digitalWrite(5, LOW); digitalWrite(18, LOW);\n    digitalWrite(23, (millis()/250)%2); // CÒI HÚ DỒN DẬP\n  } else if (isWarning) {\n    digitalWrite(5, HIGH); // LED VÀNG\n    digitalWrite(19, LOW); digitalWrite(18, LOW);\n    digitalWrite(23, LOW);\n  } else {\n    digitalWrite(18, HIGH); // LED XANH AN TOÀN\n    digitalWrite(19, LOW); digitalWrite(5, LOW);\n    digitalWrite(23, LOW);\n  }\n}`,
        why: "ĐỘI TRƯỞNG ESP32 TRÊN MẶT ĐẤT LÀM GÌ ĐỂ CỨU MẠNG NGƯỜI?",
        whyContent: "Sau khi nhận được bức thư từ dưới hầm qua chân RX2, ESP32 Master lập tức làm 3 việc: 1. Chiếu ngay 5 con số lên màn hình OLED cho người giám sát đọc bằng mắt; 2. Tự phát Wi-Fi để ai cầm điện thoại đứng gần mở lên là xem được biểu đồ sóng thời gian thực không cần 4G; 3. Nếu thấy khí độc hoặc thiếu Oxy, lập tức kích hoạt Còi Hú và Đèn Đỏ báo động khẩn cấp!",
        physicsTip: "💡 ESP32 tự tạo trạm phát Wi-Fi Access Point tên 'GIAM_SAT_KHONG_GIAN_KIN' (IP: 192.168.4.1), mở trình duyệt điện thoại là xem được biểu đồ sóng mà hoàn toàn không cần Internet hay 4G!"
      },
      {
        id: "oled_display",
        name: "Màn Hình OLED 0.96 inch",
        sub: "Hiển Thị SSD1306 I2C (0x3C)",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Bảng hiển thị số đo tại chỗ",
        repo: "adafruit/Adafruit_SSD1306",
        repoUrl: "https://github.com/adafruit/Adafruit_SSD1306",
        color: "#0284c7",
        icon: "fa-tv",
        pins: [
          { from: "SDA (Data)", to: "GPIO 21 (D21 Master)", note: "Chân I2C Data hiển thị số" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22 Master)", note: "Chân I2C Clock gõ nhịp" },
          { from: "VCC & GND", to: "3.3V & GND (ESP32 Master)", note: "Nguồn nuôi màn hình" }
        ],
        codeSnippet: `// Hiển thị 5 thông số lên OLED SSD1306\n#include <Adafruit_SSD1306.h>\nAdafruit_SSD1306 display(128, 64, &Wire, -1);\nvoid updateOLED() {\n  display.clearDisplay();\n  display.setCursor(0,0);\n  display.printf("O2: %.1f%%  CO:%dppm\\n", o2_val, (int)co_val);\n  display.printf("CH4:%.1f%%LEL\\n", ch4_val);\n  display.printf("T:%.1fC  H:%.1f%%\\n", t_val, h_val);\n  display.display();\n}`,
        why: "TẠI SAO PHẢI CÓ MÀN HÌNH OLED NGAY TRÊN HỘP MÁY?",
        whyContent: "Màn hình OLED dùng 2 dây SDA/SCL để hiển thị trực tiếp 5 dòng thông số (Oxy, CO, Metan, Nhiệt, Ẩm). Người chỉ huy trên bờ không cần cầm điện thoại, chỉ cần liếc mắt nhìn vào hộp máy là biết ngay dưới đáy hầm có an toàn hay không.",
        physicsTip: "💡 Màn hình OLED tự phát sáng từng điểm ảnh (Pixel), ngoài trời nắng gắt vẫn nhìn rất rõ và cực kỳ tiết kiệm pin."
      },
      {
        id: "alarm_system",
        name: "Hệ Thống Đèn 3 Màu & Còi Hú",
        sub: "Còi Buzzer & LED Đỏ - Vàng - Xanh",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Bức tường âm thanh cứu mạng người",
        repo: "GPIO Digital Output",
        repoUrl: "https://github.com",
        color: "#dc2626",
        icon: "fa-bullhorn",
        pins: [
          { from: "Còi Buzzer (+)", to: "GPIO 23", note: "Âm lượng > 85dB hú dồn dập" },
          { from: "LED ĐỎ (+)", to: "GPIO 19", note: "Sáng khi Oxy < 18% hoặc có độc" },
          { from: "LED VÀNG (+)", to: "GPIO 5", note: "Sáng khi tiệm cận ngưỡng chú ý" },
          { from: "LED XANH (+)", to: "GPIO 18", note: "Sáng khi môi trường an toàn" },
          { from: "GND (Mass)", to: "GND Chung Master", note: "Cực âm chung" }
        ],
        codeSnippet: `// Kích hoạt còi hú ngắt quãng dồn dập (250ms bật / 250ms tắt)\nif (isDanger) {\n  digitalWrite(BUZZER_PIN, (millis() / 250) % 2 == 0 ? HIGH : LOW);\n}`,
        why: "TẠI SAO CÒI HÚ VÀ ĐÈN PHẢI ĐẶT NGAY MIỆNG CỬA HẦM?",
        whyContent: "ĐÂY LÀ ĐIỂM CỐT LÕI CỨU SỐNG CON NGƯỜI: Các máy đo hiện nay bắt công nhân phải cầm máy bước xuống hầm mới đo được. Khi người dưới ngất đi, người trên bờ không biết gì sẽ nhảy xuống cứu và chết chùm. Chiếc còi hú công suất lớn đặt ngay tại miệng cửa hầm đóng vai trò như 'BỨC TƯỜNG ÂM THANH' đanh thép, cảnh báo trực diện làm người trên bờ giật mình khựng lại, dứt khoát không bước xuống!",
        physicsTip: "💡 Còi được lập trình hú ngắt quãng dồn dập (chớp tắt 250 phần nghìn giây) để tạo âm thanh báo động khẩn cấp nhất, đập tan phản xạ nhảy xuống cứu mù quáng."
      }
    ];'''

# Thay thế mảng COMPONENTS cũ bằng mảng mới
pattern = r'const COMPONENTS = \[.*?\];'
text = re.sub(pattern, new_components_code, text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated all explanations for Grade 9 students directly into the web application!")
