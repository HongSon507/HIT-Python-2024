n = int(input())
A = set(input(f"Nhập mã sinh viên thứ {i+1} cho tập hợp A: ") for i in range(n))
B = set(input(f"Nhập mã sinh viên thứ {i+1} cho tập hợp B: ") for i in range(n))

print("Tập A:", A)
print("Tập B:", B)

sv = A & B
if sv:
    print("Sinh viên đăng ký học tại cả hai bàn:", sv)
else:
    print("Không có sinh viên ")

cacsv = A | B
print("Danh sách tổng hợp các sinh viên đã đăng ký của cả hai bàn:", cacsv)

chi1ban = A - B
print("đăng ký bàn 1 mà không đăng ký tại bàn 2:", chi1ban)
