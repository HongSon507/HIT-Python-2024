def is_numeric(s):
    return s.isdigit()

n = int(input("Nhập số lượng phần tử trong mảng: "))
a = [input("Nhập xâu ký tự: ") for _ in range(n)]
b = tuple(a)

print("Tuple b:", b)

count = 0
for item in b:
    if is_numeric(item):
        count += 1

print("Số phần tử có dạng số trong tuple:", count)
