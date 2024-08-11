sinh_vien = {
    'SV001': 3.2,
    'SV002': 3.5,
    'SV003': 2.8,
    'SV004': 3.0,
    'SV005': 1.9
}

count_in_range = sum(1 for diem in sinh_vien.values() if 3.0 <= diem <= 3.5)
print(f"Số sinh viên có điểm tổng kết trong đoạn [3.0, 3.5]: {count_in_range}")

sinh_vien['SV006'] = 3.6

sinh_vien = {ma_sv: diem for ma_sv, diem in sinh_vien.items() if diem >= 2.0}

print("Danh sách sinh viên và điểm tổng kết:")
for ma_sv, diem in sinh_vien.items():
    print(f"{ma_sv}: {diem}")
