# https://www.youtube.com/watch?v=zwZXiutgrUE
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        res = 0
        sign = 1
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -(2 ** 31)
        # whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        # checking +/- sign
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        valid_digits = set('0123456789')
        while i < len(s) and s[i] in valid_digits:
            res = res*10 + int(s[i])
            i += 1

        res = sign*res

        return min(MAX_INT, res) if sign > 0 else max(MIN_INT, res)



