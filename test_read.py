import os

# Đường dẫn file index.html
path = os.path.abspath(r'mo_phong_3d_noi_day\index.html')

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Kiểm tra nội dung hiện tại
print(f"Current file size: {len(text)} bytes")
