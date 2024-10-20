import re

def regex(string):
    pattern = '^ab?'
    return bool(re.search(pattern, string))

print(regex("ac"))
print(regex("abc"))
print(regex("a"))
print(regex("ab"))
print(regex("abb"))