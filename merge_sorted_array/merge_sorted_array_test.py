


import unittest
from merge_sorted_array import Solution


class Test(unittest.TestCase):
    def test_basic(self):
        solution = Solution()

        nums1 = [1, 2, 5, 0, 0, 0]
        solution.merge(nums1, 3, [2, 3, 6], 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])


if __name__ == '__main__':
    unittest.main()
