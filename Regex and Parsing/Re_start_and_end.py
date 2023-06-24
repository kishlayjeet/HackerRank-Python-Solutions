import re
string = input()
substring = input()
if re.search(f'(?={substring})',string):
    for i in re.finditer(f'(?={substring})',string):
        print((i.start(),i.start()+len(substring)-1))
else:
    print((-1,-1))
