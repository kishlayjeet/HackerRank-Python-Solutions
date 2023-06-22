for x in range(int(input())):
    _ = int(input())
    lst = list(map(int, input().split()))
    m = max(lst)
    for y in range(len(lst)+1):
        if len(lst) == 0:
            print("Yes")
        elif m <= lst[0]:
            lst.remove(lst[-1])
        elif m <= lst[-1]:
            lst.remove(lst[0])
        else:
            print("No")
            break