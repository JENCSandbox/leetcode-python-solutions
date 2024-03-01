import unittest
from solution import Solution

class Test(unittest.TestCase):

    def test_basic(self):
        solution = Solution()
        data = "0101"
        expected = "1001"
        result = solution.maximumOddBinaryNumber(data)

        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()