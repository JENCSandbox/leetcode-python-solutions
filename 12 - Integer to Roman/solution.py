# 12. Integer to Roman

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_numbers = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',

            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',

            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',

            1000: 'M'
        }
        def generate_roman_auxiliar (digit, base):
            if digit < 5:
                return roman_numbers.get(base) * digit
            else:
                return roman_numbers.get(base*5) + (roman_numbers.get(base) * (digit-5))


        result = ''
        temp = num
        base = 1
        while temp > 0:
            digit = temp % 10
            positional_value = digit * base
            if digit != 0:
                print(digit, base)
                roman_value = roman_numbers.get(positional_value) if roman_numbers.get(positional_value) is not None else generate_roman_auxiliar(digit, base)
                result = roman_value + result

            temp = temp // 10
            base = base * 10

        return result


solution = Solution()


print(solution.intToRoman(40))
print(solution.intToRoman(41))
print(solution.intToRoman(1000))
print(solution.intToRoman(1950))
print(solution.intToRoman(3749))