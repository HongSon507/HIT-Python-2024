N = int(input())
numbers = list(map(int, input().split()))
lst = [1, 3, 5, 7, 9]
favorite_numbers = [num for num in numbers if num % 10 in lst]
favorite_numbers.sort()
print(len(favorite_numbers))
print(" ".join(map(str, favorite_numbers)))
