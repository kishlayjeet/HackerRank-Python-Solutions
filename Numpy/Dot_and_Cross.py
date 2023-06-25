import numpy

N = int(input())
lst1, lst2 = [], []
for _ in range(N):
    lst1 += list(map(int, input().split()))
for _ in range(N):
    lst2 += list(map(int, input().split()))
arr1 = numpy.reshape(lst1, (N, N))
arr2 = numpy.reshape(lst2, (N, N))
print(numpy.dot(arr1, arr2))
