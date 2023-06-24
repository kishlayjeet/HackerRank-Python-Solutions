import re
for _ in range(int(input())):
    if re.search(r'^[+-]?[0-9]*\.[0-9]+$', input()):
        print(True)
    else:
        print(False)
