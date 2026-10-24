#include <Arduino.h>
#include <Wire.h>
#include <DHT.h>
#include <DFRobot_OxygenSensor.h>
#include <ArduinoJson.h>
#include "BluetoothSerial.h"

// --- KHAI BÁO CÁC CHÂN KẾT NỐI NGOẠI VI ---
#define DHTPIN          13        // Data DHT22 -> GPIO 13
#define DHTTYPE         DHT22
#define MQ4_PIN         34        // AO MQ-4 (CH4) -> GPIO 34
#define MQ7_PIN         35        // AO MQ-7 (CO)  -> GPIO 35

// Module MAX485
#define PIN_RS485_RX   16        // RO MAX485 -> GPIO 16 (RX2)
#define PIN_RS485_TX   17        // DI MAX485 -> GPIO 17 (TX2)
#define PIN_RS485_DIR  4         // DE & RE chập chung -> GPIO 4

// Cảm biến Oxy DFRobot I2C (Mặc định: ADDRESS_3 = 0x73)
#define OXYGEN_I2C_ADDRESS ADDRESS_3 
#define COLLECT_NUMBER 10

DHT dht(DHTPIN, DHTTYPE);
DFRobot_OxygenSensor oxygen;
HardwareSerial RS485Serial(2);
BluetoothSerial SerialBT;

// --- THÔNG SỐ ĐIỆN TRỞ CHUẨN ĐO KHÍ (LOG-LOG MODEL) ---
const float RL_VALUE = 10.0;     // Điện trở tải RL trên module (10 kOhm)
float R0_MQ4 = 15.0;            // Nội trở chuẩn MQ-4 trong không khí sạch (kOhm)
float R0_MQ7 = 10.0;            // Nội trở chuẩn MQ-7 trong không khí sạch (kOhm)

bool isO2SensorReady = false;

// Đọc điện áp ADC ESP32 qua lấy mẫu đa điểm (20 mẫu) để lọc nhiễu
float readAdcVoltage(int pin) {
  long sum = 0;
  for (int i = 0; i < 20; i++) {
    sum += analogRead(pin);
    delayMicroseconds(300);
  }
  float adcVal = sum / 20.0;
  // ESP32 ADC 12-bit (0-4095), dải đo tương ứng ~3.3V
  return (adcVal * 3.3) / 4095.0;
}

// Tính nồng độ khí Metan (CH4) theo mô hình Log-Log (% LEL)
float readCH4() {
  float vOut = readAdcVoltage(MQ4_PIN);
  if (vOut <= 0.05) return 0.0;
  
  float Rs = ((5.0 - vOut) * RL_VALUE) / vOut;
  float ratio = Rs / R0_MQ4;

  // Công thức đặc tính MQ-4: ppm = 1000 * (Rs/R0)^(-2.6)
  float ppm = 1000.0 * pow(ratio, -2.6);
  if (isnan(ppm) || ppm < 0.0) ppm = 0.0;

  // Quy đổi ra % LEL (100% LEL của CH4 tương đương 50.000 ppm)
  float percentLEL = (ppm / 50000.0) * 100.0;
  if (percentLEL > 100.0) percentLEL = 100.0;
  return percentLEL;
}

// Tính nồng độ khí Carbon Monoxide (CO) theo mô hình Log-Log (ppm)
float readCO() {
  float vOut = readAdcVoltage(MQ7_PIN);
  if (vOut <= 0.05) return 0.0;

  float Rs = ((5.0 - vOut) * RL_VALUE) / vOut;
  float ratio = Rs / R0_MQ7;

  // Công thức đặc tính MQ-7: ppm = 99.04 * (Rs/R0)^(-1.518)
  float ppm = 99.04 * pow(ratio, -1.518);
  if (isnan(ppm) || ppm < 0.0) ppm = 0.0;
  if (ppm > 1000.0) ppm = 1000.0;
  return ppm;
}

void setup() {
  Serial.begin(115200);

  // Cấu hình chân chuyển hướng truyền/nhận RS485
  pinMode(PIN_RS485_DIR, OUTPUT);
  digitalWrite(PIN_RS485_DIR, LOW); // Mặc định ở chế độ nghỉ/nhận

  // Khởi động cổng UART2 giao tiếp MAX485
  RS485Serial.begin(9600, SERIAL_8N1, PIN_RS485_RX, PIN_RS485_TX);

  // Khởi động Bluetooth Serial Slave
  SerialBT.begin("ESP32_GIENG_SLAVE");
  Serial.println("\n[Duoi Gieng] Bluetooth bat dau phat: ESP32_GIENG_SLAVE");

  // Khởi động I2C (SDA: D21, SCL: D22)
  Wire.begin(21, 22);

  // Thử kết nối cảm biến Oxy (tối đa 3 lần, tránh treo bo mạch nếu chưa cắm)
  for (int retry = 0; retry < 3; retry++) {
    if (oxygen.begin(OXYGEN_I2C_ADDRESS)) {
      isO2SensorReady = true;
      Serial.println("[OK] Cam bien Oxy I2C da ket noi thanh cong!");
      break;
    }
    Serial.println("[!] Dang thu ket noi cam bien Oxy...");
    delay(500);
  }
  if (!isO2SensorReady) {
    Serial.println("[Canh bao] Khong tim thay cam bien Oxy. He thong se dung gia tri mac dinh 20.9%!");
  }

  // Khởi động DHT22
  dht.begin();

  // Cấu hình ADC ESP32
  analogReadResolution(12);
  analogSetAttenuation(ADC_11db); // Đo dải áp tới ~3.3V

  Serial.println("[Duoi Gieng] He thong khoi dong xong! Bat dau chu ky do.");
}

unsigned long lastSendTime = 0;

void loop() {
  // Chu kỳ gửi gói tin mỗi 1.5 giây
  if (millis() - lastSendTime >= 1500) {
    lastSendTime = millis();

    // 1. Đọc dữ liệu Oxy
    float oxygenVol = 20.9;
    if (isO2SensorReady) {
      oxygenVol = oxygen.getOxygenData(COLLECT_NUMBER);
      if (oxygenVol <= 0.0 || isnan(oxygenVol) || oxygenVol > 35.0) {
        oxygenVol = 20.9;
      }
    }

    // 2. Đọc DHT22
    float temp = dht.readTemperature();
    float hum  = dht.readHumidity();
    if (isnan(temp)) temp = 0.0;
    if (isnan(hum))  hum  = 0.0;

    // 3. Đọc tính toán MQ-4 & MQ-7
    float ch4_lel = readCH4();
    float co_ppm  = readCO();

    // 4. Đóng gói JSON
    StaticJsonDocument<200> doc;
    doc["o2"]   = round(oxygenVol * 10.0) / 10.0;
    doc["co"]   = round(co_ppm * 10.0) / 10.0;
    doc["ch4"]  = round(ch4_lel * 10.0) / 10.0;
    doc["temp"] = round(temp * 10.0) / 10.0;
    doc["hum"]  = round(hum * 10.0) / 10.0;

    String jsonString;
    serializeJson(doc, jsonString);

    // 5. Phát qua đường dây RS485 (Kênh chính)
    digitalWrite(PIN_RS485_DIR, HIGH); // Kéo chân DIR lên HIGH để truyền
    delayMicroseconds(60);
    RS485Serial.println(jsonString);
    RS485Serial.flush();               // Chờ đẩy hết toàn bộ byte ra dây
    delayMicroseconds(60);
    digitalWrite(PIN_RS485_DIR, LOW);  // Hạ chân DIR xuống LOW để nghỉ

    // 6. Phát qua sóng vô tuyến Bluetooth (Kênh dự phòng)
    SerialBT.println(jsonString);

    // In ra Serial monitor máy tính để theo dõi tại chỗ
    Serial.print("[Sensor Data] ");
    Serial.println(jsonString);
  }
}