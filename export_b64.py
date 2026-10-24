import base64
import os

glb_path = 'test_esp32.glb'
output_js = r'mo_phong_3d_noi_day\esp32_glb_data.js'

with open(glb_path, 'rb') as f:
    data = f.read()

b64 = base64.b64encode(data).decode('utf-8')
print(f'GLB size: {len(data)} bytes, Base64 size: {len(b64)} chars')

with open(output_js, 'w', encoding='utf-8') as f:
    f.write(f'window.ESP32_GLB_BASE64 = "{b64}";\n')

print(f'Successfully exported to {output_js}')
