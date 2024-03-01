import unittest
from max_consecutive_ones import Solution


class Test1672(unittest.TestCase):
    def test_basic(self):
        solution = Solution()

        result = solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
        self.assertEqual(result, 3)

        result = solution.findMaxConsecutiveOnes([1, 0, 1, 0, 1, 1, 1, 0, 1])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
