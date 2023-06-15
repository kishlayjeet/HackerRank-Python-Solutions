if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list = list(arr)
    
    max_num = max(list)
    runner_up = max([n for n in list if n != max_num])
    
    print(runner_up) 