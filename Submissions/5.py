def seperate(numbers):     
    positive_numbers = []     
    negative_numbers = []

    for num in numbers:         
        if num >= 0:                        
            positive_numbers.append(num)         
        else: 
            negative_numbers.append(num)     
    return positive_numbers, negative_numbers 

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9] 
positive, negative = seperate(numbers)

print("Positive numbers:", positive) 
print("Negative numbers:", negative) 
