from collections import namedtuple
N = int(input())
Student = namedtuple('Student', input().split())
average_marks = 0
for i in range(N):
    data = input().split()
    xyz = Student(data[0], data[1], data[2], data[3])
    average_marks += int(xyz.MARKS)
print(average_marks/N)