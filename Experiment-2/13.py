a = 0
b = 1

print(a, b, end=" ")
while True:
    temp = b
    b += a
    a = temp
    if b > 50:
        break
    print(b, end=" ")
