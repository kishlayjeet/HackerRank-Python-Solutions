import numpy
N, M = map(int, input().split())
lst = []
for i in range(N):
    lst += list(map(int, input().split()))
np_arr = numpy.reshape(lst, (N, M))
print(numpy.transpose(np_arr))
print(np_arr.flatten())