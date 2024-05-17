# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = True
        # negatives numbers
        if x < 0:
            result = False
        # one digit case
        elif x // 10 == 0:
            result = True

        # numbers is positive and has more than one digit
        number_as_string = str(x)

        if len(number_as_string) % 2 == 0:
            right = len(number_as_string)//2
            left = right - 1
        else:
            right = len(number_as_string) // 2 + 1
            left = len(number_as_string) // 2 - 1

        while left >= 0 and right < len(number_as_string):
            if number_as_string[left] != number_as_string[right]:
                result = False
                break
            left -= 1
            right += 1

        return result

