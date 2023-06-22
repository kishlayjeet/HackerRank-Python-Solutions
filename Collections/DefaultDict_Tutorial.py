from collections import defaultdict
dictionary = defaultdict(list)
A, B = map(int, input().split())
for i in range(A+B):
    inp = input()
    if i<A:
        dictionary['characters'].append(inp)
    else:
        dictionary['char'].append(inp)
for i in dictionary['char']:
    count = 1
    if i in dictionary['characters']:
        for j in dictionary['characters']:
            if i == j:
                print(count, end=' ')
            count+=1   
        print()    
    else:
        print(-1)
        
