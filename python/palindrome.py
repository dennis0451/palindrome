from audioop import reverse
from cmath import isnan, nan


def palindrome(word):
    word = str(word)
    lower_case_word = word.lower()
    # print(len(lower_case_word))
    # reverse_word = lower_case_word[::-1]
    reversed_word = ''.join(reversed(lower_case_word))
    # print((reverse_word))

    if lower_case_word == reversed_word:
        return True
    else:
        return False

print(palindrome('racecar') == True)
print(palindrome('Noon') == True)
print(palindrome('ciVic') == True)
print(palindrome('nice') == False)
print(palindrome(434) == True)
print(palindrome(123) == False)
print(palindrome('bomb') == False)