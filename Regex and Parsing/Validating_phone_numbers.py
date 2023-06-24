import re
for i in range(int(input())):
    print("YES" if re.fullmatch(r'[789][0-9]{9}', input()) else "NO")