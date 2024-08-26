def bailam(kqua):
    dem = 0 
    so = 19 
    while True :
        if sum(int(digit) for digit in str(so)) == 10:
            dem += 1 
            if dem == kqua:
                return so
        so += 9

kqua = int(input("Nhap so: "))
result = bailam(kqua)
print(result)