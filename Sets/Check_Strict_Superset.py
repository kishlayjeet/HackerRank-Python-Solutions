superset = set(map(int, input().split()))
N = int(input())
for i in range(N):
    count = 0
    subset = set(map(int, input().split()))
    first = superset - subset
    second = subset - superset
    if len(first) > 0 and len(second) == 0:
        continue
    else:
        print(False)
        quit()
print(True)
