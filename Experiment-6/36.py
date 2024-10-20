import re

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

for found in re.finditer(pattern, text):
    print(f"Found at index {found.start()}")