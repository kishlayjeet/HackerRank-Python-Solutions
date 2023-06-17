ENUM = int(input())
english_students = set(map(int, input().split()))
FNUM = int(input())
french_students = set(map(int, input().split()))

print(len(english_students.symmetric_difference(french_students)))