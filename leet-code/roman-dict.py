def roman_num(s: str) -> int:

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # TODO: edge cases:
    #   out of bounds

    sum = 0
    for i in range(len(s) - 1):

        current = roman_dict[s[i]]
        next = roman_dict[s[i + 1]]
        if current < next:
            sum -= current

        else:
            sum += current

    sum += roman_dict[s[-1]]
    return sum


print(roman_num("LVIII"))
print(roman_num("MCMXCIV"))
# if a roman numeral is less than the one that is after it, subtract it instead
# III = 3
# IV = 4, because I is one, and it comes before V which is 5. So, we subtract I(1)
