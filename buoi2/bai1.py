# y a
m = int(input())
sum = 0
while m > 0 :
    sum += m % 10
    m //= 10
print (sum)
# y b
n = int(input())
thuong = 0
if n > 0:
    for i in range(1,n+1,1):
        if n % i == 0:
            thuong += i
print(thuong)
# y c
a = int(input())
b = int(input())
c = int(input())
if a<=0 or b <=0 or c<=0:
    print("Khong")
elif a+b <= c or b+c <= a or c+a <=b:
    print("Khong")
elif a == b and b == c :
    print("tgiac Deu")
elif a == b or b == c or c == a:
    print("tgiac can")
elif a * a == b*b + c *c or b * b == a * a + c * c or c*c == b*b + a*a :
    print("tgiac vuong")
elif a*a + b*b > c*c and a*a + c*c > b*b and b*b + c*c > a*a:
    print("tgiac nhon")
else :
    print("tu")