import re
for _ in range(int(input())):
    hex_code = re.findall(r'(?<=[^\n])#[a-fA-F0-9]{3,6}', input())
    if hex_code:
        print(*hex_code, sep='\n')
