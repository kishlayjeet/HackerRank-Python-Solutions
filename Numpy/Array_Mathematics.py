import numpy

N, M = map(int, input().split())
lst1, lst2 = [], []

for _ in range(N):
    lst1 += list(map(int, input().split()))
for _ in range(N):
    lst2 += list(map(int, input().split()))

a = numpy.reshape(lst1, (N, M))
b = numpy.reshape(lst2, (N, M))

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))
