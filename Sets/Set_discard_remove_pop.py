_ = input()
S = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd = input().split()
    if cmd[0] == 'pop':
        S.pop()
    elif cmd[0] == 'remove':
        S.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        S.discard(int(cmd[1]))
print(sum(S))
