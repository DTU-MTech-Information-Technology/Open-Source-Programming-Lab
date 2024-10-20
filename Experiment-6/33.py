import re

def regex(string):
    pattern = '^a(b*)$'
    return bool(re.search(pattern, string))

print(regex("ac"))
print(regex("abc"))
print(regex("a"))
print(regex("ab"))
print(regex("abb"))