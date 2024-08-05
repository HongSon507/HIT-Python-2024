input_list = input("Nhap vao cac ptu: ")
lst = []
for char in input_list:
    if char == " ":
        continue
    lst.append(char)

print(set(list(lst)))