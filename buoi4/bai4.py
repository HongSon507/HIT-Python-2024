def find_largest_subset(s, tonglonnhat):
    sapxep = sorted(s)
    subset = set()
    tongbdau = 0

    for elements in sapxep:
        if tongbdau + elements <= tonglonnhat:
            subset.add(elements)
            tongbdau += elements
        else:
            break
    
    return subset

n = int(input("Nhập số lượng phần tử trong tập hợp: "))
s = set(int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n))

tonglonnhat = int(input("Nhập số nguyên giới hạn: "))

largest_subset = find_largest_subset(s, tonglonnhat)

print("Tập hợp con lớn nhất thỏa mãn điều kiện:", largest_subset)
