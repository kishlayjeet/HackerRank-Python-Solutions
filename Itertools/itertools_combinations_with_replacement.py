from itertools import combinations_with_replacement
S, K = input().split()
S = sorted(S)
output = list(combinations_with_replacement(S, int(K)))
for i in output:
    print(''.join(i))