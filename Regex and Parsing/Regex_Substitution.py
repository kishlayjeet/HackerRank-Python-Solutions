import re
for _ in range(int(input())):
    print(re.sub(r"(?<= )&&(?= )|(?<= )\|\|(?= )", lambda z: "and" if z.group()=="&&" else "or", input()))