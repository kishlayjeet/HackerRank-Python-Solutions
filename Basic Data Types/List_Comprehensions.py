if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    x1 = [i for i in range(x+1)]
    y1 = [i for i in range(y+1)]
    z1 = [i for i in range(z+1)]
    
    all_perm = [[i, j, k] for i in x1 for j in y1 for k in z1]
    req_perm = [r for r in all_perm if sum(r) != n]
    
    print(req_perm)
    