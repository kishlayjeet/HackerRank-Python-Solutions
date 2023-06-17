arr_size = int(input())
arr = set(map(int, input().split()))

N = int(input())
for i in range(N):
    cmd = input().split()
    sets = set(map(int, input().split()))
    if cmd[0] == 'intersection_update':
        arr.intersection_update(sets)
    elif cmd[0] == 'update':
        arr.update(sets)
    elif cmd[0] == 'symmetric_difference_update':
        arr.symmetric_difference_update(sets)
    elif cmd[0] == 'difference_update':
        arr.difference_update(sets)
print(sum(arr))