# Bài 9: Làm việc với dữ liệu thời gian

from datetime import datetime

# Lấy thời điểm hiện tại
thoi_diem = datetime.now()

# Chuyển thời điểm thành chuỗi theo định dạng quy định
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Khởi tạo thời điểm bắt đầu và kết thúc
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

# Tính thời lượng
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))