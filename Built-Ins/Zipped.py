students, subjects = map(int, input().split())
marks = []
for i in range(subjects):
    marks += [list(map(float, input().split()))]
for i in zip(*marks):
    print(sum(i)/subjects)
