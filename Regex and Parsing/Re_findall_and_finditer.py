import re
vovels = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])", input())
print('\n'.join(vovels) if vovels else -1)