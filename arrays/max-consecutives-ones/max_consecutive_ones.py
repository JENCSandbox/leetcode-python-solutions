# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.

class Solution():
    def findMaxConsecutiveOnes(self, nums):
        """
                :type nums: List[int]
                :rtype: int
                """
        max_consecutive_ones = 0
        temporal_accumulator = 0

        # traverse the array of binary value
        for binaryValue in nums:
            # if the value is Zero, we must check:
            if binaryValue == 0:
                # if the current count of ones is greater that the current max, replace it
                if temporal_accumulator > max_consecutive_ones:
                    max_consecutive_ones = temporal_accumulator
                # restore the accumulator to start counting again
                temporal_accumulator = 0
            # for the other case, if the binaryValue is 1
            elif binaryValue == 1:
                # increment the current accumulator
                temporal_accumulator = temporal_accumulator + 1
        else: # at the of the loop if the current count of ones is greater that the current max, replace it
            if temporal_accumulator > max_consecutive_ones:
                max_consecutive_ones = temporal_accumulator

        return max_consecutive_ones
