#1
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
dem = 0
x = int(input())
for x in lst:
    if i == x: 
        dem += 1
print(dem)
#2+3
dsthaythe = [8, 5, 4, 0, 1, 3]
lst[1:7] = dsthaythe
print(lst)
#4
print(max(lst))
print(min(lst))
#5
y = int(input())
lst.insert(0, y)
print(lst)
#6
if lst == sorted(lst):
    print("Tang")
elif lst == sorted(lst, reverse= True):
    print("Giam")
else :
    print("No")
#7
lst2 = []
tong = 0
for i in lst:
    tong += i
    lst2.append(tong)
print(lst2)
#8
lst3 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print(sorted(lst3))
listgttd = []
for i in lst3 :
    listgttd.append(abs(i))
print(sorted(listgttd))

