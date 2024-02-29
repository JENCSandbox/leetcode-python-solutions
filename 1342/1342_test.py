import unittest
from example_1342 import Solution

class Test1342(unittest.TestCase):
    def test_basic(self):
        data = 14
        expected = 6
        solution = Solution()
        result = solution.numberOfSteps(data)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()