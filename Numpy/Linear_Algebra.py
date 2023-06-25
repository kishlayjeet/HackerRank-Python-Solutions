import numpy

N = int(input())
lst = []
for i in range(N):
    lst += list(map(float, input().split()))
arr = numpy.reshape(lst, (N, N))
print(round(numpy.linalg.det(arr), 2))
