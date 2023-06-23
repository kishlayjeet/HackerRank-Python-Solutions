_, lst = int(input()), list(map(int, input().split()))
print(all([i >= 0 for i in lst]) and any(
    [str(x) == str(x)[::-1] for x in lst]))
