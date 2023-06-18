from itertools import groupby
data = groupby(input())
for key, value in data:
    print(f'({len(list(value))}, {key})', end=' ')