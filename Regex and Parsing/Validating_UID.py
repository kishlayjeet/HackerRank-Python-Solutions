import re

for _ in range(int(input())):
    uid = input()
    try:
        match = re.match(r'^[0-9a-zA-Z]{10}$', uid)
        assert match
        assert len(set(match.group(0))) == 10
        assert len(re.findall(r'\d', uid)) >= 3
        assert len(re.findall(r'[A-Z]', uid)) >= 2
    except AssertionError:
        print('Invalid')
    else:
        print('Valid')
