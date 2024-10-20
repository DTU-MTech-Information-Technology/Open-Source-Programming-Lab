def strobogrammatic(n):
    return internal(n, n)

def internal(n, l):
    if n == 0: return [""]
    if n == 1: return ["1", "0", "8"]

    middles = internal(n - 2, l)
    result = []

    for middle in middles:
        if n != l:
            result.append("0" + middle + "0")

        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")

    return result

print(strobogrammatic(3))