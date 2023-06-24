import re
regex = re.search(r'([a-zA-Z0-9])\1+', input())
print(regex.group(1)) if regex else print(-1)