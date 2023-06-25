import numpy
N, M, P = map(int, input().split())
lst1 = []
lst2 = []
for i in range(N):
    lst1 += list(map(int, input().split()))
for i in range(M):
    lst2 += list(map(int, input().split()))
np_arr1 = numpy.reshape(lst1, (N, P))
np_arr2 = numpy.reshape(lst2, (M, P))
print(numpy.concatenate((np_arr1, np_arr2), axis=0))
