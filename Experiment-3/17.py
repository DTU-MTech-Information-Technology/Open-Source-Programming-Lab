def count_cases(str):
    lower_count = 0
    upper_count = 0
    for c in str:
        if c.islower():
            lower_count += 1
        if c.isupper():
            upper_count += 1
    
    return lower_count, upper_count


if __name__ == "__main__":
    lower_count, upper_count = count_cases("The quick Brown Fox")
    print("No. of Uppercase characters:", upper_count)
    print("No. of Lowercase Characters:", lower_count)