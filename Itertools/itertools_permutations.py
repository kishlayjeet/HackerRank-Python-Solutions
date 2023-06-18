from itertools import permutations
S, K = input().split()
K = int(K)
output = sorted(list(permutations(S, K)))
for i in output:
    print(''.join(i))