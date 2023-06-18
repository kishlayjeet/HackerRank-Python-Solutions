import math
a, b = float(input()), float(input())
print(f'{round(math.degrees(math.atan2(a, b)))}{chr(176)}')
