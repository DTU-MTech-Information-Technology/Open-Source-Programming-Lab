def binomial(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
    
    return res

def pascal_triangle(n):
    for row in range(n):
        print(" " * (n - row), end="")
        for i in range(row+1):
            print(binomial(row, i), " ", end = "")
        print()

if __name__ == "__main__":
    pascal_triangle(5)