def foo(m, n):
    if m > n:
        return "m cannot be greater than n"
    
    result = []
    for i in range(1, n):
        if i % m == 0:
            result.append(i)
    
    return result

if __name__ == "__main__":
    print(foo(10, 9))
    print(foo(2, 10))