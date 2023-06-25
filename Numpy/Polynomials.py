import numpy

coefficients = numpy.array(list(map(float, input().split())))
N = int(input())
print(numpy.polyval(coefficients, N))
