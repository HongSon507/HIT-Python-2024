# a
n = int(input())
if n >= 0:
    sum = 0
    for i in range( 1, 2*n + 2, 1):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
print(sum)
# y b
n2 = int(input())
sum2 = 0
for i in range( 1, n2+ 1, 1):
    sum2 += 1/i
print(sum2)
# y c
a = float(input())
b = float(input())
c= float(input())
if a == b and b ==c and c == 0:
    print("pt vo so nghiem")
if a == 0:
    if b ==0:
        print("pt vo nghiem")
    else :
        print(-c/b)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("pt vo nghiem")
    elif delta ==0 :
        print(-b/(2*a))
    else:
        print("x1 = " + str((-b + delta**(1/2))/(2*a)))
        print("x2 = " + str((-b - delta**(1/2))/(2*a)))
