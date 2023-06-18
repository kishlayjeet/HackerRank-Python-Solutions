from itertools import combinations
N = int(input())
letters = input().split()
K = int(input())
combinations = list(combinations(letters, K))
a = sum('a' in combination for combination in combinations)
print(a/len(combinations))
