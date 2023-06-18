from itertools import combinations
S, K = input().split()
S = sorted(S)
for i in range(1, int(K)+1):
    output = list(combinations(S, i))
    for j in output:
        print(''.join(j))