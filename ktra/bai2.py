s = int(input())

def kqua(s):
    return s // 3 + (bool)(s % 3)
print(kqua(s))