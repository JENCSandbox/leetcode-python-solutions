class Solution():

    def countDigits(self, num):
        numStr = str(num)
        return len(numStr)

    def isEven(self, num):
        return num % 2 == 0

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenDigitsCounter = 0
        for number in nums:
            digits = self.countDigits(number)
            if self.isEven(digits):
                evenDigitsCounter = evenDigitsCounter + 1

        return evenDigitsCounter
