import re

string = input()

lower_case = ''.join(sorted(re.findall(r"[a-z]", string)))
upper_case = ''.join(sorted(re.findall(r"[A-Z]", string)))
numeric = sorted(re.findall(r"[0-9]", string))
odd_numeric = ''.join([i for i in numeric if int(i) % 2 == 1])
even_numeric = ''.join([i for i in numeric if int(i) % 2 == 0])
print(lower_case + upper_case + odd_numeric + even_numeric)
