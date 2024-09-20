def is_palindrome(word):
    if type(word) is int:
        word = str(word)

    reverse_word = ""
    end = len(word) - 1

    while end >= 0:
        reverse_word += word[end]
        end -= 1

    print(word)
    print(reverse_word)

    if reverse_word == word:
        return True
    return False


print(is_palindrome("racecar"))
print(is_palindrome(1221))
print(is_palindrome(-121))
test = -121
print(test)
print(str(test))
