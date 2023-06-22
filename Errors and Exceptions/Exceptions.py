for i in range(int(input())):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except Exception as e:
        print(f'Error Code:', e)