def celsius_to_fahrenheit(celsius):     
    fahrenheit = (celsius * 9/5) + 32     
    return fahrenheit 

def fahrenheit_to_celsius(fahrenheit):     
    celsius = (fahrenheit - 32) * 5/9     
    return celsius 

print("Celsius to Fahrenheit : ", celsius_to_fahrenheit(48))  
print("Fahrenheit to Celsius : ", fahrenheit_to_celsius(56)) 
