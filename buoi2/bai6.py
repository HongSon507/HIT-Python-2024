
def check(num):
    tong = 0
    for i in range(1,num):
        if num % i == 0:
            tong += i 
    return tong == num
n = int(input())
print(f" Cac so hoan hao tu 1 den {n} la: ")
for num in range(1,n+1,1):
    if check(num):
        print(num)