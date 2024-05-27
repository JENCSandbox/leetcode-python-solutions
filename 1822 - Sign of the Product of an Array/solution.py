from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0

        for number in nums:
            if number == 0:
                return 0
            elif number < 0:
                negatives += 1

        return -1 if negatives % 2 != 0 else 1