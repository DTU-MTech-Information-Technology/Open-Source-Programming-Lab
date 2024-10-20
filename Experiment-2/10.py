def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


if __name__ == "__main__":
    print("(1) Convert Celsius to Fahrenheit")
    print("(2) Convert Fahrenheit to Celsius")
    choice = input("Enter the numeric choice for the action you want to perform: ")
    print()

    if choice == "1":
        temp = int(input("Enter temperature in Celsius: "))
        print(f"{temp}°C is {int(celsius_to_fahrenheit(temp))}°F")

    elif choice == "2":
        temp = int(input("Enter temperature in Fahrenheit: "))
        print(f"{temp}°F is {int(fahrenheit_to_celsius(temp))}°C")

    else:
        print("ERROR: Invalid choice!")