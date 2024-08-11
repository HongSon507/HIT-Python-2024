chuoi = input("Nhập một chuỗi: ")

dem = {}

for ky_tu in chuoi:
    if ky_tu in dem:
        dem[ky_tu] += 1
    else:
        dem[ky_tu] = 1

print(dem)
