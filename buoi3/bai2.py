k = int(input())
a = []
for i in range(k):
    a.append(int(input()))
n = int(input())
m = int(input())
if n * m > k:
    print("Khong the")
else :
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        matrix.append(row)
    print(matrix)