import re
for _ in range(int(input())):
    user, email = input().split()
    if re.match(r'^<[A-Za-z]\w+_*[\.\-]*\w*@[A-Za-z]+\.[A-Za-z]{1,3}>$', email):
        print(user, email)
