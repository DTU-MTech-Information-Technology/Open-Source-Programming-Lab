def add(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a

print(add(4, 5))