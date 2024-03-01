class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_odd_binary_number = ""

        one_digits = ""
        zero_digits = ""

        for binary_digit in s:
            if binary_digit == "1":
                one_digits = one_digits + "1"
            else:
                zero_digits = zero_digits + "0"

        if len(one_digits) == 1:
            max_odd_binary_number = zero_digits + one_digits

        if len(one_digits) > 1:
            one_digits = one_digits[0:len(one_digits)-1]
            max_odd_binary_number = one_digits + zero_digits + "1"

        return max_odd_binary_number
