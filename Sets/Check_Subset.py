N = int(input())
for i in range(N):
    _ = input()
    A = set(map(int, input().split()))
    _ = input()
    B = set(map(int, input().split()))
    if len(A-B) == 0:
        print(True)
    else:
        print(False)
