# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place and do not return anything.

"""
Example 1:

Input: arr = [1,0,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,0,4 - Median of Two Sorted Arrays,5 - Longest Palindromic Substring,0]
Output: [1,0,0,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,0,0,4 - Median of Two Sorted Arrays]
Explanation: After calling your function, the input array is modified to: [1,0,0,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,0,0,4 - Median of Two Sorted Arrays]
Example 2 - Add Two Numbers:

Input: arr = [1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters]
Output: [1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters]
Explanation: After calling your function, the input array is modified to: [1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters]


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9

"""
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        position_to_ignore = -1

        for position in range(0, len(arr)):
            if arr[position] == 0 and position_to_ignore != position:
                arr.insert(position, 0)
                position_to_ignore = position + 1
                arr.pop()