from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter_dic = {}

        for num in nums:
            if counter_dic.get(num) is not None:
                counter_dic[num] = counter_dic[num] + 1
            else:
                counter_dic[num] = 1
        for value in counter_dic.values():
            if value % 2 != 0:
                return False

        return True
