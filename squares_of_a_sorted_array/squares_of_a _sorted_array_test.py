import unittest
from example_squares_of_a_sorted_array import Solution

class Test(unittest.TestCase):
    def test_basic(self):
        solution = Solution()

        data = [-2, -1, 0, 3, 4, 6]
        expected = [0, 1, 4, 9, 16, 36]
        result = solution.sortedSquares(data)
        self.assertEqual(result, expected)

        data = [-7,-3,2,3,11]
        expected = [4,9,9,49,121]
        result = solution.sortedSquares(data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()