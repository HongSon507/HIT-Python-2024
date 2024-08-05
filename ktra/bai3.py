n = int(input())
lst = [input().split() for _ in range(n)]
lst = [(name, int(score)) for name, score in lst]
scores = sorted(set(score for name, score in lst))
second_lowest_score = scores[1]
result = [name for name, score in lst if score == second_lowest_score]
for name in result:
    print(name)

