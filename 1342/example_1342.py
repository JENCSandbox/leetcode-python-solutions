class Solution(object):
    def isEven(self, number):
        return number % 2 == 0

    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        stepToZeroReduce = 0
        tempNumber = num
        while (tempNumber > 0):
            if self.isEven(tempNumber):
                tempNumber = tempNumber / 2
            else:
                tempNumber = tempNumber - 1

            stepToZeroReduce = stepToZeroReduce + 1
        return stepToZeroReduce
