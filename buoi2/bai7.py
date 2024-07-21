def tongcacso(num):
    tong = 0
    for i in range(1,num):
        if num % i == 0:
            tong += i
    return tong
n = int(input())
print(f"Cac cap so Amicable tu 1 den {n} la: ")
for num1 in range(1, n+1,1):
    num2 = tongcacso(num1)
    if num1 < num2 <= n and tongcacso(num2) == num1 :
        print(f"({num1}, {num2})")