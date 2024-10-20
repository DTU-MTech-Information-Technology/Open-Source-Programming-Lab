n = int(input("Enter the value of n: "))

value = sum(list(map(lambda x: x**3, range(1, n+1))))
print(value)