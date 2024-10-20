import random

for _ in range(5):
    print(''.join(str(x) for x in random.sample(range(10), 3)))