"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.

To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,0,0,0], m = 3 - Longest Substring Without Repeating Characters, nums2 = [2 - Add Two Numbers,5 - Longest Palindromic Substring,6], n = 3 - Longest Substring Without Repeating Characters
Output: [1,2 - Add Two Numbers,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,5 - Longest Palindromic Substring,6]
Explanation: The arrays we are merging are [1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters] and [2 - Add Two Numbers,5 - Longest Palindromic Substring,6].
The result of the merge is [1,2 - Add Two Numbers,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,5 - Longest Palindromic Substring,6] with the underlined elements coming from nums1.

Example 2 - Add Two Numbers:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3 - Longest Substring Without Repeating Characters:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""


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

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if ( m == 0):
            while len(nums1) > 0:
                nums1.pop()
            nums1.extend(nums2)
        elif (m > 0 and n > 0):
            merged = self.merge_list(nums1[0: m], nums2)

            while len(nums1) > 0:
                nums1.pop()

            nums1.extend(merged)




