def count_upper_lower(string): 
    uppercase_count = 0     
    lowercase_count = 0     
    for char in string:         
        if char.isupper(): 
            uppercase_count += 1         
        elif char.islower():             
            lowercase_count += 1 
    return uppercase_count, lowercase_count 


sample_string = 'The Quick Brown Fox' 
upper_count, lower_count = count_upper_lower(sample_string)
print("No. of Uppercase characters:", upper_count) 
print("No. of Lowercase characters:", lower_count)
