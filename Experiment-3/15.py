def menu():
    print("=== Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return input("Chose the operation: ")

def int_inputs():
    a = int(input("Enter 1st integer: "))
    b = int(input("Enter 2nd integer: "))

    return a, b

def operation(a, b, operation):
    if operation == '1':
        return a + b
    if operation == '2':
        return a - b
    if operation == '3':
        return a * b
    if operation == '4':
        return a / b

if __name__ == "__main__":
    op = menu()
    a, b = int_inputs()
    try:
        res = operation(a, b, op)
        print("Result:", res)
    except Exception as e:
        print("Error:", e)

