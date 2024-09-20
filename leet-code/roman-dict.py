def roman_num(s: str) -> int:

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for i in range(len(s)):

        prev = roman_dict[s[i - 1]]
        current = roman_dict[s[i]]
        if prev < current:
            addition = current - prev
            sum += addition
        else:
            sum += roman_dict[s[i]]

    return sum


print(roman_num("LVIII"))
# print(roman_num("MCMXCIV"))
