tpl = tuple(input("".format(i+1)) for i in range(int(input( "số lượng phần tử: "))))
new = tuple(int(x) for x in tpl)
average = sum(new) / len(new)
print("Trung bình cộng:", average)
