class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        result = 0

        for i, letter in enumerate(number):
            if letter == str(digit) and int(number[0:i]+number[i+1:]) > result:
                result = int(number[0:i]+number[i+1:])

        return str(result) if result > 0 else number





sol = Solution()
print(sol.removeDigit("12345678", 4))