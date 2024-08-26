def tinhtong(str):
    tong = 0
    num = ''
    for char in str:
        if char.isdigit() or (char == "-" and not num):
            num += char
        else:
            if num:
                tong += int(num)
                num = ""
    if num:
        tong += int(num)
    return (tong)
str = input("Nhap chuoi vao: ")
kqua = tinhtong(str)
print(kqua)


