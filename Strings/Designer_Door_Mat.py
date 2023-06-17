if __name__ == '__main__':
    N, M = map(int, input().split())

# Upper
for i in range(N//2):
    print(('.|.' * (2*i+1)).center(M, '-'))

# Middle
print('WELCOME'.center(M, '-'))

# Lower
for i in range(N//2-1, -1, -1):
    print(('.|.' * (2*i+1)).center(M, '-'))
    
