class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        a_array will be the smaller array
        b_array will be the biggest array
        """
        [a_array, b_array] = [nums1, nums2] if len(nums1) <= len(nums2) else [nums2, nums1]

        total = len(a_array) + len(b_array)
        half = total // 2

        l, r = 0, len(a_array)-1
        while True:
            i = (l+r) // 2  # med index for A array
            j = half - (i+1) - 1  # med index for B array

            left_a = a_array[i] if i >= 0 else -10_000_000
            right_a = a_array[i+1] if i+1 < len(a_array) else +10_000_000

            left_b = b_array[j] if j >= 0 else -10_000_000
            right_b = b_array[j + 1] if j + 1 < len(b_array) else +10_000_000

            # partition is correct
            if left_a <= right_b and left_b <= right_a:
                # odd
                if total % 2:
                    return min(right_a,right_b)
                # even
                else:
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2
            elif left_a > right_b:
                r = i - 1
            elif right_a < left_b:
                l = i + 1

solution = Solution()
#print(solution.findMedianSortedArrays([1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,4 - Median of Two Sorted Arrays,5 - Longest Palindromic Substring,6,7,8],[1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,4 - Median of Two Sorted Arrays]))
#print(solution.findMedianSortedArrays([1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,4 - Median of Two Sorted Arrays,5 - Longest Palindromic Substring,6,7],[1,2 - Add Two Numbers,3 - Longest Substring Without Repeating Characters,4 - Median of Two Sorted Arrays]))
print(solution.findMedianSortedArrays([3,4],[1,2]))
print(solution.findMedianSortedArrays([1,2],[3,4]))