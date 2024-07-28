def chuan_hoa_ho_ten(name):
    words = name.split()
    words = [word.capitalize() for word in words]
    return ' '.join(words)

name = input()
normalized_name = chuan_hoa_ho_ten(name)
print(normalized_name)