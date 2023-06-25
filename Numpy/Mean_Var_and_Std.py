import numpy

N, M = map(int, input().split())
lst = []
for i in range(N):
    lst += list(map(int, input().split()))
arr = numpy.reshape(lst, (N, M))
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))
