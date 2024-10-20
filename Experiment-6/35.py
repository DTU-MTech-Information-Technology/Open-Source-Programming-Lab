import re

pattern_list = ['fox', 'dog', 'horse']
text = 'The quick brown fox jumps over the lazy dog.'

for pattern in pattern_list:
    if re.search(pattern, text):
        print(f'"{pattern}" found!')
    else:
        print(f'"{pattern}" not found!')