import os
import re

path = os.path.abspath(r'mo_phong_3d_noi_day\index.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Thêm CSS cho khối 3 bước thực tế bên trong .explanation-card
new_css = '''
    /* PHẦN GIẢI THÍCH THỰC TẾ TRONG EXPLANATION-CARD (DỄ HIỂU LỚP 9) */
    .explanation-card {
      margin-top: 14px;
      background: var(--row-bg);
      border: 1.5px solid var(--row-border);
      border-radius: 12px;
      padding: 14px 16px;
    }

    .why-title {
      font-size: 0.88rem;
      font-weight: 800;
      color: #ea580c;
      display: flex;
      align-items: center;
      gap: 7px;
      margin-bottom: 8px;
    }
    body.dark-mode .why-title {
      color: #ff9f1a;
    }

    .why-desc {
      font-size: 0.82rem;
      line-height: 1.6;
      color: var(--text);
      margin-bottom: 12px;
    }

    .flow-steps-box {
      background: var(--card-bg);
      border: 1px solid var(--row-border);
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 12px;
    }

    .flow-steps-hdr {
      font-size: 0.76rem;
      font-weight: 800;
      color: #0284c7;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    body.dark-mode .flow-steps-hdr {
      color: #38bdf8;
    }

    .flow-step-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.78rem;
      line-height: 1.5;
      color: var(--text);
      margin-bottom: 8px;
      padding-bottom: 8px;
      border-bottom: 1px dashed var(--row-border);
    }
    .flow-step-item:last-child {
      margin-bottom: 0;
      padding-bottom: 0;
      border-bottom: none;
    }

    .step-badge {
      background: #0284c7;
      color: #fff;
      font-size: 0.68rem;
      font-weight: 800;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
    }
'''

if '/* PHẦN GIẢI THÍCH THỰC TẾ TRONG EXPLANATION-CARD (DỄ HIỂU LỚP 9) */' not in text:
    text = text.replace('</style>', new_css + '\n  </style>')

# 2. Cập nhật mảng COMPONENTS với đầy đủ step1, step2, step3, studentTip cho từng linh kiện
new_components = r'''    const COMPONENTS = [
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
          { from: "SDA (Data)", to: "GPIO 21 (D21)", note: "Dây truyền số nồng độ Oxy" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22)", note: "Dây gõ nhịp đồng hồ tíc-tắc" },
          { from: "VCC (Nguồn)", to: "VCC 5V Power Rail", note: "Dây cấp điện 5V nuôi cảm biến" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Dây cực âm khép kín dòng điện" }
        ],
        codeSnippet: `// Khởi tạo thư viện DFRobot_OxygenSensor theo chuẩn I2C\n#include "DFRobot_OxygenSensor.h"\n#define Oxygen_IICAddress ADDRESS_3 // 0x73 mặc định\nDFRobot_OxygenSensor oxygen;\n\nvoid setup() {\n  Wire.begin(21, 22); // SDA=21, SCL=22 phần cứng\n  while(!oxygen.begin(Oxygen_IICAddress)) {\n    Serial.println("I2C Error!"); delay(1000);\n  }\n}\nfloat readO2() {\n  return oxygen.getOxygenData(10); // Đọc trung bình 10 lần\n}`,
        why: "TẠI SAO PHẢI NỐI CHÂN SDA VÀO D21, SCL VÀO D22?",
        whyContent: "Chân SDA là chân tín hiệu (Data), còn chân SCL là chân nhịp đồng hồ. Muốn ESP32 giao tiếp được với cảm biến Oxy thì bắt buộc phải thông qua 2 chân này để 2 con nối vào nhau. Khi cảm biến ngửi thấy nồng độ Oxy trong không khí, nó dùng dây SCL để gõ nhịp và dây SDA để đọc to con số nồng độ Oxy (ví dụ 20.9%) gửi trực tiếp cho ESP32 dưới không gian kín.",
        step1: "Cảm biến Oxy liên tục đo lượng dưỡng khí dưới đáy hầm, gửi con số phần trăm qua cặp chân SDA và SCL vào cổng GPIO 21 và GPIO 22 của ESP32 dưới đáy.",
        step2: "ESP32 ở dưới không gian kín nhận được tin, lập tức đóng gói nồng độ Oxy vào bức thư báo cáo (chuỗi JSON), rồi đưa sang chân tín hiệu A và B của cáp Cat5e phóng vọt lên mặt đất.",
        step3: "ESP32 trên mặt đất nhận được dữ liệu thì đưa lên trang Web xem trên điện thoại, hiện số % Oxy lên màn hình OLED, và nếu thấy Oxy tụt dưới 18% thì lập tức hú còi + chớp đèn đỏ cảnh báo không cho ai bước xuống!",
        studentTip: "Hãy giải thích với thầy cô: Chân 21 và 22 là cổng I2C phần cứng có sẵn của ESP32, giúp 2 bên nói chuyện ăn ý với nhau cực nhanh (400.000 nhịp/giây) mà không bao giờ bị nghẽn CPU.",
        physicsTip: "💡 Không khí bình thường có 20.9% Oxy. Nếu dưới hầm tụt xuống < 18.0%, chỉ sau 30-40 giây não bộ sẽ mất ý thức ngất xỉu mà nạn nhân không hề hay biết!"
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
          { from: "A0 (Analog)", to: "GPIO 35", note: "Chân truyền tín hiệu nồng độ khí CO" },
          { from: "VCC (5V Nung)", to: "VCC 5V Power Rail", note: "Cấp điện 5V nung nóng lõi cảm biến" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp dòng điện nung lớn" }
        ],
        codeSnippet: `// Cấu hình thư viện MQUnifiedsensor cho MQ-7\n#include <MQUnifiedsensor.h>\n#define Pin 35 // ADC1 GPIO 35\nMQUnifiedsensor MQ7("ESP-32", 3.3, 12, Pin, "MQ-7");\n\nvoid setup() {\n  MQ7.init();\n  MQ7.setRegressionMethod(1); // PPM = a*ratio^b\n  MQ7.setA(99.042); MQ7.setB(-1.518); // Hệ số chuẩn khí CO\n}\nfloat readCO() {\n  MQ7.update();\n  return MQ7.readSensor();\n}`,
        why: "TẠI SAO PHẢI NỐI CHÂN TÍN HIỆU A0 VÀO GPIO 35?",
        whyContent: "Chân A0 là chân tín hiệu (Data). Muốn ESP32 giao tiếp được với MQ-7 thì bắt buộc phải nối qua chân này. Khi cảm biến ngửi thấy khí than độc CO (sinh ra do cháy yếm khí hoặc động cơ nổ), lò nung trong cảm biến sẽ phát ra dòng điện áp tương ứng và gửi qua chân A0 vào cổng GPIO 35 của ESP32 dưới không gian kín để ESP32 đọc được mức độ độc hại.",
        step1: "Cảm biến MQ-7 phát hiện khí than độc CO, chuyển thành điện áp gửi qua chân tín hiệu A0 vào cổng GPIO 35 của ESP32 dưới đáy hầm.",
        step2: "ESP32 ở dưới không gian kín nhận được tin thì tính ra có bao nhiêu hạt khí độc (ppm), đóng gói tin vào bức thư JSON rồi đưa sang chân tín hiệu A và B của cáp Cat5e gửi lên mặt đất.",
        step3: "ESP32 trên mặt đất nhận được dữ liệu thì đưa lên Web xem trên điện thoại, hiện số ppm khí độc lên màn hình OLED, và nếu thấy nồng độ CO vượt ngưỡng nguy hiểm (>= 30 ppm) thì lập tức hú còi inh ỏi + bật đèn đỏ cảnh báo!",
        studentTip: "Hãy giải thích với thầy cô: GPIO 35 là cổng đo điện áp độc lập (ADC1) của ESP32, không bị nhiễu sóng khi chip phát Wi-Fi/Bluetooth, giúp đo khí than độc chính xác 100%.",
        physicsTip: "💡 Khí CO chiếm ái lực với hồng cầu gấp 250 lần dưỡng khí Oxy. Mức >= 30 ppm là mức nguy hại, hít phải trong không gian kín sẽ ngấm ngầm làm tế bào chết ngạt!"
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
          { from: "A0 (Analog)", to: "GPIO 34", note: "Chân truyền tín hiệu nồng độ khí Gas" },
          { from: "VCC (5V Nung)", to: "VCC 5V Power Rail", note: "Cấp điện nung nóng sấy nhiệt" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp mass chung" }
        ],
        codeSnippet: `// Cấu hình thư viện MQUnifiedsensor cho MQ-4\n#include <MQUnifiedsensor.h>\n#define PinMQ4 34 // ADC1 GPIO 34\nMQUnifiedsensor MQ4("ESP-32", 3.3, 12, PinMQ4, "MQ-4");\n\nvoid setup() {\n  MQ4.init();\n  MQ4.setRegressionMethod(1);\n  MQ4.setA(1012.7); MQ4.setB(-2.786); // Hệ số khí CH4\n}\nfloat readCH4_LEL() {\n  MQ4.update();\n  float ppm = MQ4.readSensor();\n  return (ppm / 50000.0) * 100.0; // 50,000 ppm = 100% LEL\n}`,
        why: "TẠI SAO PHẢI NỐI CHÂN TÍN HIỆU A0 VÀO GPIO 34?",
        whyContent: "Chân A0 là chân tín hiệu (Data). Muốn ESP32 giao tiếp được với MQ-4 thì phải thông qua chân này để 2 con nối vào nhau. Khi con cảm biến đọc được khí gas Metan bốc lên từ bùn rác dưới cống, nó sẽ gửi tín hiệu điện áp qua chân A0 cho ESP32 dưới không gian kín để ESP32 biết khí gas đang đậm đặc cỡ nào.",
        step1: "Cảm biến MQ-4 ngửi thấy khí gas Metan bốc lên từ bùn cống, gửi tín hiệu điện áp qua chân A0 vào cổng GPIO 34 của ESP32 dưới đáy hầm.",
        step2: "ESP32 ở dưới không gian kín nhận được tin thì tính ra nồng độ % cháy nổ (%LEL), đóng gói tin vào bức thư chung rồi gửi qua chân tín hiệu A và B của cáp mạng Cat5e chạy lên mặt đất.",
        step3: "ESP32 trên mặt đất nhận được dữ liệu thì đưa lên trang Web xem trên điện thoại, hiện % khí gas lên màn hình OLED, và nếu thấy nồng độ đạt ngưỡng nguy hiểm (>= 10% LEL) thì lập tức hú còi báo động + chớp đèn đỏ không cho ai bước xuống!",
        studentTip: "Hãy giải thích với thầy cô: GPIO 34 thuộc bộ ADC1 độc lập, đo đạc ổn định kể cả khi có dòng nung lớn từ cảm biến khí cháy nổ.",
        physicsTip: "💡 Khí Metan bốc lên từ hầm phân, bùn cống rác thối. Chỉ cần đạt 5% thể tích là một tia lửa nhỏ từ giày dép hay kim loại va đập cũng có thể gây nổ tung hầm!"
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
          { from: "DATA (1-Wire)", to: "GPIO 4 (D4)", note: "Chân truyền tín hiệu nhiệt độ và độ ẩm" },
          { from: "VCC (Nguồn)", to: "VCC 5V Power Rail", note: "Nguồn nuôi cảm biến" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Chân mass chung" }
        ],
        codeSnippet: `// Khởi tạo thư viện Adafruit DHT\n#include "DHT.h"\n#define DHTPIN 4     // Nối vào GPIO 4\n#define DHTTYPE DHT22\nDHT dht(DHTPIN, DHTTYPE);\n\nvoid setup() {\n  dht.begin();\n}\nvoid readEnv(float &temp, float &hum) {\n  hum = dht.readHumidity();\n  temp = dht.readTemperature();\n}`,
        why: "TẠI SAO PHẢI NỐI CHÂN DATA VÀO GPIO 4?",
        whyContent: "Chân DATA là chân tín hiệu (Data). Muốn ESP32 giao tiếp được với DHT22 thì phải nối qua chân này. Dưới cống rãnh ngầm độ ẩm lúc nào cũng tới 80-99% và rất nóng làm các cảm biến khí bị sai lệch. Khi DHT22 đọc được nhiệt độ và độ ẩm, nó gửi tín hiệu xung điện qua chân DATA vào chân GPIO 4 để ESP32 dưới không gian kín tự động bù trừ sai số, không bao giờ bị báo động giả.",
        step1: "Cảm biến DHT22 đo nhiệt độ và độ ẩm dưới cống, gửi tín hiệu xung điện qua chân DATA vào chân GPIO 4 của ESP32 dưới đáy hầm.",
        step2: "ESP32 ở dưới không gian kín dùng số nhiệt ẩm này để bù sai số cho các cảm biến khí, gom tất cả vào bức thư báo cáo (gói JSON), rồi đóng gói vào chân tín hiệu A và B của cáp mạng Cat5e gửi lên mặt đất.",
        step3: "ESP32 trên mặt đất nhận được dữ liệu thì đưa lên Web xem trên điện thoại, hiện số độ C và % độ ẩm lên màn hình OLED, và nếu phát hiện có khí độc hoặc thiếu Oxy thì kích hoạt còi hú + đèn đỏ báo động!",
        studentTip: "Hãy giải thích với thầy cô: Nối DHT22 vào GPIO 4 giúp thuật toán bù trừ nhiệt ẩm môi trường, đảm bảo các số đo PPM khí độc không bao giờ bị báo động nhầm khi trời ẩm ướt.",
        physicsTip: "💡 Dữ liệu nhiệt ẩm được chớp tắt bằng xung điện siêu ngắn (chỉ 26 đến 70 phần triệu giây) qua đúng 1 sợi dây duy nhất."
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
          { from: "VIN (Nguồn)", to: "VCC 5V Power Rail", note: "Ăn điện từ cáp nguồn mặt đất cấp xuống" },
          { from: "GND (Mass)", to: "GND Mass Rail", note: "Đường hồi tiếp mass chung" },
          { from: "GPIO 17 (TX2)", to: "DI (MAX485 Slave)", note: "Bắn bức thư JSON sang loa phóng MAX485" },
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Slave)", note: "Cổng nhận nối tiếp UART2" }
        ],
        codeSnippet: `// Đóng gói JSON và gửi qua UART2 RS485\nvoid sendDataToMaster(float o2, float co, float ch4, float t, float h) {\n  String json = "{\\"o2\\":" + String(o2,1) + \n                ",\\"co\\":" + String(co,1) + \n                ",\\"ch4\\":" + String(ch4,1) + \n                ",\\"t\\":" + String(t,1) + \n                ",\\"h\\":" + String(h,1) + "}\\n";\n  Serial2.print(json); // Bắn lên qua MAX485\n}`,
        why: "CHÚ LÍNH ESP32 DƯỚI ĐÁY ĐÓNG GÓI TIN VÀ GỬI LÊN THẾ NÀO?",
        whyContent: "Khi 4 con cảm biến đọc được khí gas, khí than, oxy và nhiệt ẩm, chúng gửi tín hiệu về cho ESP32 dưới không gian kín qua các chân Data. Sau khi nhận đủ tin, con ESP32 này sẽ đóng gói tất cả vào một bức thư duy nhất (dạng JSON), rồi đưa sang chân tín hiệu A và B của cáp mạng Cat5e gửi vọt lên cho ESP32 trên mặt đất.",
        step1: "ESP32 dưới đáy nhận tín hiệu liên tục từ 4 cảm biến Oxy, CO, Metan, Nhiệt độ và Độ ẩm.",
        step2: "Gom cả 5 con số vào một dòng chữ duy nhất dạng JSON: {\"o2\":20.5, \"co\":0, \"ch4\":0, \"t\":28, \"h\":80} rồi gửi qua cổng UART2 (chân 17) ra chip MAX485.",
        step3: "Chip MAX485 đóng gói tin vào 2 sợi dây tín hiệu A và B của cáp mạng Cat5e, phóng thẳng qua 20-30m hầm sâu lên cho ESP32 trên mặt đất hiển thị và báo còi đèn!",
        studentTip: "Hãy giải thích với thầy cô: Dùng cổng UART2 (GPIO 16/17) độc lập để không đè lên cổng nạp USB, giúp vi điều khiển nạp code và chạy thật trơn tru, không bao giờ bị treo.",
        physicsTip: "💡 ESP32 chạy chip lõi kép 240MHz, đóng gói bức thư 5 tham số chỉ mất chưa đầy 2 phần nghìn giây!"
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
          { from: "DI", to: "GPIO 17 (TX2)", note: "Nhận bức thư từ chân TX2 của ESP32" },
          { from: "RO", to: "GPIO 16 (RX2)", note: "Cổng nối tiếp UART2" },
          { from: "VCC & GND", to: "5V & GND Out (ESP32)", note: "Nguồn nuôi IC vi sai" },
          { from: "Chân A & B", to: "Cặp Xoắn Đôi Cáp Cat5e", note: "Hai chân tín hiệu phóng lên mặt đất" }
        ],
        codeSnippet: `// Cấu hình cổng Serial2 phần cứng cho MAX485\nvoid setup() {\n  Serial2.begin(9600, SERIAL_8N1, 16, 17);\n}`,
        why: "TẠI SAO PHẢI QUA CHIP NÀY ĐỂ ĐÓNG GÓI VÀO CHÂN A VÀ B?",
        whyContent: "Dây từ dưới hầm lên mặt đất dài tới 20–30 mét, lại ẩm ướt và đầy sóng nhiễu. Nếu ESP32 gửi thẳng tín hiệu dây thường thì lên bờ sẽ bị mất chữ, chập chờn. Chip MAX485 đóng vai trò như 'chiếc loa phóng thanh': nó nhận bức thư từ ESP32 rồi chia thành 2 dòng điện chạy trên 2 chân tín hiệu A và B của cáp Cat5e để gửi lên mặt đất an toàn 100%.",
        step1: "Nhận bức thư báo cáo từ chân TX2 của ESP32 dưới không gian kín.",
        step2: "Biến đổi thành 2 dòng điện ngược dấu nhau chạy trên cặp chân tín hiệu A và B của cáp Cat5e.",
        step3: "Khi có sóng nhiễu đập vào, cả 2 dây cùng bị nhiễu như nhau. Lên mặt đất, 2 dây trừ nhau là triệt tiêu sạch nhiễu, giúp ESP32 trên bờ nhận tin nguyên vẹn để chiếu lên Web và báo còi đèn!",
        studentTip: "Hãy giải thích với thầy cô: Đây là chuẩn giao tiếp vi sai công nghiệp RS-485, cho phép truyền dữ liệu xa tới 1.200 mét trong môi trường ẩm ướt khắc nghiệt.",
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
          { from: "3 Dây Dương (+)", to: "Cam, Trắng-Cam, Trắng-Nâu", note: "Chập 3 sợi tăng S gấp 3, giảm R 3 lần" },
          { from: "3 Dây Mass (GND)", to: "Nâu, Xanh Lá, Trắng-Xanh Lá", note: "Chập 3 sợi giảm điện trở đường về" },
          { from: "2 Dây Tín Hiệu", to: "Xanh Dương (A) & Trắng-Xanh (B)", note: "Cặp dây tín hiệu đưa tin lên mặt đất" }
        ],
        codeSnippet: `// Định luật Ohm & Điện trở dây (Vật lý 9):\n// R = rho * (l / S)\n// Chập 3 sợi làm 1 => S tăng gấp 3 => R giảm 3 lần!\n// Kết hợp nâng nguồn LM2596 lên 5.2V bù sụt áp 0.2V đường dài.`,
        why: "TẠI SAO LẠI CHẬP CỤM 3 SỢI VÀ CÓ CHÂN TÍN HIỆU A-B?",
        whyContent: "Cáp mạng có 8 sợi: 3 sợi chập làm cực Dương (+5.2V), 3 sợi chập làm cực Mass (GND), và 2 sợi dùng cho chân tín hiệu A và B. Chập 3 sợi giúp dòng điện xuống đáy không bị rơi rớt (sụt áp), còn 2 sợi A-B đưa dữ liệu từ đáy phóng thẳng lên mặt đất cho ESP32 trên bờ làm việc.",
        step1: "3 dây dương và 3 dây mass dẫn điện 5.2V từ nguồn LM2596 trên bờ xuống tận đáy nuôi ESP32 và các cảm biến nung nhiệt.",
        step2: "2 dây tín hiệu xoắn A và B đón lấy dữ liệu từ MAX485 dưới đáy phóng ngược lên trên mặt đất.",
        step3: "Lên đến miệng hầm, 2 dây A-B cắm vào bộ thu MAX485 Master để chuyển dữ liệu vào ESP32 trên mặt đất hiển thị và báo động.",
        studentTip: "Hãy tự hào đọc công thức Vật lý 9: R = rho * (l / S). Chập 3 sợi thì diện tích S tăng 3 lần, điện trở R giảm 3 lần! Ban giám khảo sẽ cho điểm tuyệt đối vì áp dụng đúng bài học trong sách giáo khoa.",
        physicsTip: "💡 Bù sụt áp: LM2596 vặn lên 5.2V, rơi rớt 0.2V dọc đường cáp 20m, xuống đáy vừa vặn đúng chuẩn 5.0V!"
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
          { from: "Chân A & B", to: "Nhận từ Cáp Cat5e", note: "Đón nhận 2 luồng xung tín hiệu từ đáy hầm" },
          { from: "RO", to: "GPIO 16 (RX2 Master)", note: "Đưa chuỗi JSON vào tai ESP32 Master" },
          { from: "VCC & GND", to: "5V & GND Nguồn", note: "Nguồn nuôi module" }
        ],
        codeSnippet: `// Nhận chuỗi JSON từ Slave\nvoid loop() {\n  if (Serial2.available()) {\n    String json = Serial2.readStringUntil('\\n');\n    parseGasData(json); // Giải mã 5 thông số\n  }\n}`,
        why: "TẠI SAO CẦN CON MAX485 THỨ HAI TRÊN MẶT ĐẤT?",
        whyContent: "Bức thư từ dưới hầm được phóng lên qua 2 chân tín hiệu A và B. Con chip MAX485 trên mặt đất đóng vai trò như 'người đón thư': nó nhận cặp dây A-B, dịch ngược lại thành dòng chữ ban đầu rồi đẩy qua chân RO vào tai chú lính ESP32 Master trên mặt đất để ESP32 Master xử lý lên Web, OLED và còi đèn.",
        step1: "Đón nhận 2 luồng tín hiệu A và B chạy từ dưới đáy hầm lên qua cáp mạng Cat5e.",
        step2: "Dịch ngược tín hiệu vi sai thành chuỗi chữ báo cáo JSON chuẩn và đưa qua chân RO.",
        step3: "Chân RO cắm thẳng vào chân GPIO 16 (RX2) của ESP32 Master trên mặt đất để bắt đầu kích hoạt Web, OLED và còi báo động!",
        studentTip: "Hãy giải thích với thầy cô: Cần một cặp MAX485 ở hai đầu - một con đóng gói phát tin ở đáy hầm và một con đón nhận dịch tin trên mặt đất.",
        physicsTip: "💡 Chuẩn RS-485 cho phép truyền tín hiệu xa tới 1.200 mét với độ bền bỉ chống sét lan truyền cao."
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
          { from: "OUT+ (5.2V)", to: "Cụm 3 Dây Dương Cáp Cat5e & VIN Master", note: "Cấp 5.2V bù sụt áp đường dài 20m" },
          { from: "OUT- (GND)", to: "Cụm 3 Dây Mass Cáp Cat5e & GND Master", note: "Cực âm chung toàn hệ thống" }
        ],
        codeSnippet: `// Hiệu suất chuyển đổi BUCK xung:\n// H = P_out / P_in > 90% (Mạch luôn mát, tiết kiệm ắc quy gấp đôi LM7805)`,
        why: "TẠI SAO NGUỒN PHẢI CHỈNH LÊN 5.2V MÀ KHÔNG ĐỂ 5.0V?",
        whyContent: "Dòng điện chạy qua 20 mét dây cáp mạng xuống đáy hầm sẽ bị hao hụt mất 0.2V dọc đường theo định luật Ohm. Nếu trên bờ để đúng 5.0V thì xuống đáy chỉ còn 4.8V làm cảm biến nung bị yếu và chập chờn. Việc chỉnh nguồn lên 5.2V là tính toán thực tế: 5.2V trừ đi 0.2V rơi rớt dọc đường sẽ vừa vặn đúng chuẩn 5.0V nuôi cảm biến dưới đáy hầm!",
        step1: "Nhận điện áp 7.4V - 12V từ bình ắc quy hoặc pin dự phòng trên mặt đất.",
        step2: "Hạ áp bằng cuộn cảm xung hiệu suất cao > 90%, duy trì mức điện áp 5.2V cực kỳ mát mẻ, không bị nóng bỏng như IC cũ.",
        step3: "Cấp nguồn cho ESP32 Master trên bờ và phóng dòng điện qua cụm 3 dây dương cáp Cat5e xuống tận đáy nuôi toàn bộ cảm biến.",
        studentTip: "Hãy giải thích với thầy cô: Dùng mạch Buck xung LM2596 giúp tiết kiệm pin gấp đôi so với IC LM7805 cũ, máy chạy được cả ca làm việc 8-12 tiếng trên bình ắc quy nhỏ.",
        physicsTip: "💡 Công nghệ BUCK xung PWM tần số 150kHz, tiết kiệm năng lượng tối đa cho thiết bị cứu hộ di động."
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
          { from: "GPIO 16 (RX2)", to: "RO (MAX485 Master)", note: "Nhận bức thư dữ liệu từ đáy gửi lên" },
          { from: "GPIO 21 & 22", to: "OLED SSD1306 (SDA & SCL)", note: "Gửi số liệu ra màn hình OLED" },
          { from: "GPIO 23", to: "Còi Hú Báo Động (Buzzer)", note: "Hú còi dồn dập khi có khí độc" },
          { from: "GPIO 19, 5, 18", to: "LED Đỏ - Vàng - Xanh", note: "Báo động 3 cấp độ an toàn" },
          { from: "VIN & GND", to: "5.2V Nguồn & GND Chung", note: "Nuôi Master từ LM2596" }
        ],
        codeSnippet: `// Hàm xử lý còi đèn theo 3 cấp độ an toàn:\nvoid handleAlarm(float o2, float co, float ch4) {\n  bool isDanger = (o2 < 18.0 || co >= 30.0 || ch4 >= 10.0);\n  bool isWarning = (o2 <= 19.5 || co >= 15.0 || ch4 >= 5.0);\n  if (isDanger) {\n    digitalWrite(19, HIGH); // LED ĐỎ\n    digitalWrite(5, LOW); digitalWrite(18, LOW);\n    digitalWrite(23, (millis()/250)%2); // CÒI HÚ DỒN DẬP\n  } else if (isWarning) {\n    digitalWrite(5, HIGH); // LED VÀNG\n    digitalWrite(19, LOW); digitalWrite(18, LOW);\n    digitalWrite(23, LOW);\n  } else {\n    digitalWrite(18, HIGH); // LED XANH AN TOÀN\n    digitalWrite(19, LOW); digitalWrite(5, LOW);\n    digitalWrite(23, LOW);\n  }\n}`,
        why: "ESP32 TRÊN MẶT ĐẤT LÀM GÌ ĐỂ LÊN WEB, MÀN HÌNH VÀ BÁO CÒI ĐÈN?",
        whyContent: "Sau khi ESP32 dưới không gian kín gửi bức thư lên qua 2 chân tín hiệu A và B, con ESP32 Master trên mặt đất nhận được qua chân RX2 (GPIO 16). Nó lập tức làm 3 việc thực tế: 1. Đưa số liệu lên Web Server Wi-Fi; 2. Đưa số liệu ra màn hình OLED để người đứng trên bờ đọc; 3. Nếu phát hiện có khí độc hoặc thiếu Oxy thì kích hoạt còi hú vang trời và bật đèn đỏ báo động!",
        step1: "Nhận bức thư 5 thông số từ dưới đáy hầm đưa vào chân GPIO 16 (RX2).",
        step2: "Kiểm tra mức độ an toàn: Oxy có < 18% không, CO có >= 30 ppm không, Gas có >= 10% LEL không.",
        step3: "Chiếu ngay số lên OLED (chân 21, 22), phát Wi-Fi cho điện thoại xung quanh mở Web xem biểu đồ không cần 4G, và bật còi hú (chân 23) + đèn đỏ (chân 19) báo động khẩn cấp!",
        studentTip: "Hãy giải thích với thầy cô: ESP32 Master là bộ não trung tâm trên mặt đất, phối hợp cả Web Server không dây, màn hình hiển thị tại chỗ và hệ thống còi đèn đa tầng.",
        physicsTip: "💡 ESP32 tự tạo trạm phát Wi-Fi Access Point tên 'GIAM_SAT_KHONG_GIAN_KIN' (IP: 192.168.4.1), mở trình duyệt điện thoại là xem được biểu đồ sóng mà hoàn toàn không cần Internet hay 4G!"
      },
      {
        id: "oled_display",
        name: "Màn Hình OLED 0.96 inch",
        sub: "Hiển Thị SSD1306 I2C (0x3C)",
        group: "KHỐI TRÊN MẶT ĐẤT (MASTER)",
        badge: "Bảng hiển thị số đo tại chỗ",
        repo: "adafruit/Adafruit_SSD1306",
        repoUrl: "https://github.com",
        color: "#0284c7",
        icon: "fa-tv",
        pins: [
          { from: "SDA (Data)", to: "GPIO 21 (D21 Master)", note: "Chân nhận dữ liệu hiển thị số" },
          { from: "SCL (Clock)", to: "GPIO 22 (D22 Master)", note: "Chân nhận xung nhịp đồng hồ" },
          { from: "VCC & GND", to: "3.3V & GND (ESP32 Master)", note: "Nguồn nuôi màn hình" }
        ],
        codeSnippet: `// Hiển thị 5 thông số lên OLED SSD1306\n#include <Adafruit_SSD1306.h>\nAdafruit_SSD1306 display(128, 64, &Wire, -1);\nvoid updateOLED() {\n  display.clearDisplay();\n  display.setCursor(0,0);\n  display.printf("O2: %.1f%%  CO:%dppm\\n", o2_val, (int)co_val);\n  display.printf("CH4:%.1f%%LEL\\n", ch4_val);\n  display.printf("T:%.1fC  H:%.1f%%\\n", t_val, h_val);\n  display.display();\n}`,
        why: "TẠI SAO ESP32 PHẢI NỐI RA MÀN HÌNH OLED?",
        whyContent: "Khi ESP32 Master trên mặt đất nhận được bức thư từ dưới đáy đưa lên, nó gửi ngay qua 2 chân SDA (GPIO 21) và SCL (GPIO 22) để hiển thị 5 con số lên màn hình OLED. Người chỉ huy đứng trên bờ không cần cầm điện thoại, chỉ cần liếc mắt nhìn vào hộp máy là biết ngay dưới hầm an toàn hay nguy hiểm.",
        step1: "Nhận tín hiệu hiển thị số từ chân GPIO 21 và GPIO 22 của ESP32 Master trên bờ.",
        step2: "Màn hình tự phát sáng từng điểm ảnh hiển thị rõ ràng 5 dòng: Oxy (%), Khí than CO (ppm), Khí Gas (%LEL), Nhiệt độ và Độ ẩm.",
        step3: "Giúp người giám sát tại chỗ nắm bắt tình hình tức khắc mà không bị phụ thuộc vào điện thoại hay kết nối mạng.",
        studentTip: "Hãy giải thích với thầy cô: Dùng chuẩn I2C chỉ tốn đúng 2 sợi dây nhưng truyền được toàn bộ đồ họa và văn bản với tốc độ cao.",
        physicsTip: "💡 Công nghệ OLED tự phát sáng từng điểm ảnh (Pixel), ngoài trời nắng gắt vẫn nhìn rất rõ và cực kỳ tiết kiệm điện."
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
        why: "TẠI SAO CÒI HÚ VÀ ĐÈN PHẢI NỐI VÀO CÁC CHÂN 23, 19, 5, 18 TRÊN MIỆNG HẦM?",
        whyContent: "Khi ESP32 Master trên bờ phát hiện có khí độc từ chân A-B gửi lên, nó lập tức kích hoạt chân GPIO 23 để còi hú vang trời và chân GPIO 19 để đèn đỏ chớp dồn dập. Đặt còi ngay miệng hầm để tạo ra 'BỨC TƯỜNG ÂM THANH' đanh thép, cảnh báo trực diện làm người trên bờ giật mình khựng lại, dứt khoát không bước xuống hầm!",
        step1: "ESP32 Master trên mặt đất phát hiện nồng độ khí vượt ngưỡng nguy hiểm (Oxy < 18% hoặc CO >= 30 ppm hoặc Gas >= 10% LEL).",
        step2: "Lập tức xuất lệnh điện áp cao ra chân GPIO 23 (bật còi hú ngắt quãng 250ms) và chân GPIO 19 (bật LED Đỏ).",
        step3: "Âm thanh còi hú > 85dB vang dội ngay cửa hầm, báo động toàn khu vực và ngăn chặn tuyệt đối thảm kịch nhảy xuống cứu mù quáng.",
        studentTip: "Hãy giải thích với thầy cô: Đây là điểm nhân văn cốt lõi cứu sống con người của dự án - cảnh báo tại chỗ trước khi con người bước vào không gian kín.",
        physicsTip: "💡 Tiếng còi hú ngắt quãng dồn dập 250ms bật / 250ms tắt kích thích trực tiếp vào thính giác con người, tạo phản xạ dừng lại ngay lập tức."
      }
    ];'''

text = re.sub(r'const COMPONENTS = \[.*?\];', new_components, text, flags=re.DOTALL)

# 3. Cập nhật cách render detailBody để hiển thị khối 3 bước thực tế đúng như ảnh người dùng chụp
old_render = r'''        <div class="explanation-card">
          <h4><i class="fa-solid fa-circle-question"></i> ${comp.why}</h4>
          <p>${comp.whyContent}</p>
          <div class="highlight-tip">
            <strong>Ghi nhớ cốt lõi:</strong> Hãy giải thích rõ với thầy cô đây là thiết kế phần cứng có chủ đích để chống xung đột tài nguyên vi điều khiển.
          </div>
          <div class="physicsTip">
            ${comp.physicsTip}
          </div>
        </div>'''

new_render = r'''        <div class="explanation-card">
          <div class="why-title"><i class="fa-solid fa-circle-question"></i> ${comp.why}</div>
          <p class="why-desc">${comp.whyContent}</p>

          <!-- KHỐI QUY TRÌNH HOẠT ĐỘNG THỰC TẾ 3 BƯỚC -->
          <div class="flow-steps-box">
            <div class="flow-steps-hdr"><i class="fa-solid fa-route"></i> QUY TRÌNH HOẠT ĐỘNG THỰC TẾ:</div>
            <div class="flow-step-item">
              <span class="step-badge">1</span>
              <div><b>Dưới không gian kín:</b> ${comp.step1}</div>
            </div>
            <div class="flow-step-item">
              <span class="step-badge">2</span>
              <div><b>Đường truyền cáp Cat5e:</b> ${comp.step2}</div>
            </div>
            <div class="flow-step-item">
              <span class="step-badge">3</span>
              <div><b>Trên mặt đất cứu người:</b> ${comp.step3}</div>
            </div>
          </div>

          <div class="highlight-tip">
            <strong><i class="fa-solid fa-lightbulb"></i> Mẹo trả lời thầy cô:</strong> ${comp.studentTip}
          </div>

          <div class="physicsTip">
            ${comp.physicsTip}
          </div>
        </div>'''

text = text.replace(old_render, new_render)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated explanation card with 3-step practical data flow and student-friendly tips!")
