def add_without_plus(a, b):     
    while b != 0:         
        carry = a & b         
        a = a ^ b         
        b = carry << 1     
        return a 

num1 = 6 
num2 = 9 

result = add_without_plus(num1, num2) 
print("Sum of", num1, "and", num2, "is:", result) 
