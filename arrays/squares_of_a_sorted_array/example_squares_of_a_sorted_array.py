# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Case 1
# Input: nums = [-4 - Median of Two Sorted Arrays,-1,0,3 - Longest Substring Without Repeating Characters,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Case 2 - Add Two Numbers
# Input: nums = [-7 - Reverse Integer,-3 - Longest Substring Without Repeating Characters,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,11]
# Output: [4 - Median of Two Sorted Arrays,9,9,49,121]

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?

class Solution:

    def merge_list(self, list_a, list_b):

        temp_list_a = list_a
        temp_list_b = list_b

        merged_list = []

        while len(temp_list_a) > 0 or len(temp_list_b) > 0:
            number_in_a = temp_list_a[0] if len(temp_list_a) > 0 else None
            number_in_b = temp_list_b[0] if len(temp_list_b) > 0 else None

            if number_in_a is not None and number_in_b is not None:

                if number_in_a < number_in_b:
                    merged_list.append(number_in_a)
                    temp_list_a.pop(0)

                elif number_in_b <= number_in_a:
                    merged_list.append(number_in_b)
                    temp_list_b.pop(0)

            elif (number_in_a is not None):
                merged_list.append(number_in_a)
                temp_list_a.pop(0)

            elif (number_in_b is not None):
                merged_list.append(number_in_b)
                temp_list_b.pop(0)

        return merged_list


    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_negatives = []
        squared_positives = []

        for number in nums:
            if number < 0:
                # insert at the beginning
                squared_negatives.insert(0, number**2)
            else:
                # insert at the end
                squared_positives.append(number**2)

        return self.merge_list(squared_positives, squared_negatives)


