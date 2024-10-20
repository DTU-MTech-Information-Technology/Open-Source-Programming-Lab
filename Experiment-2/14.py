m = int(input("Enter m: "))
n = int(input("Enter n: "))

matrix = [[i*j for j in range(n)] for i in range(m)]

print(matrix)