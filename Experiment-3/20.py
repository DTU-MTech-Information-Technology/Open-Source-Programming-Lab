def two_digit_letter_combinations(digits):
    string_maps = { 
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl", 
        "5": "mno", 
        "6": "pqrs", 
        "7": "tuv", 
        "8": "wxy", 
        "9": "z"
    }

    result = [""]
    for num in digits:
        temp = []
        for an in result:
            for char in string_maps[num]:
                temp.append(an + char)
        result = temp
    return result

print(two_digit_letter_combinations("47"))