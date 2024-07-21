n = int(input())
def ktraams(num):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    return total == num
print("Các số Armstrong bậc 3 từ 1 đến {n} là:")
for num in range(1, n + 1):
    if ktraams(num):
        print(num)