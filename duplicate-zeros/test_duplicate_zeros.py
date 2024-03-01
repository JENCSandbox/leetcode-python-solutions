import unittest
from duplicate_zeros import Solution

class TestCase(unittest.TestCase):
    def test_basic(self):
        data = [1,0,2,3,0,4,5,0]
        expeted = [1,0,0,2,3,0,0,4]

        solution = Solution()
        solution.duplicateZeros(data)

        self.assertEqual(data, [1,0,0,2,3,0,0,4,])

if __name__ == '__main__':
    unittest.main()
