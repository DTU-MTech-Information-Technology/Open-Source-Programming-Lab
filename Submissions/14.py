def divisible_by_m(m, n): 
    if m <= n and m > 0 and n > 0: 
        return [num for num in range(1, n + 1) if num % m == 0]     
    else:         
        return [] 

m, n = 3, 20
print(divisible_by_m(m, n)) 
