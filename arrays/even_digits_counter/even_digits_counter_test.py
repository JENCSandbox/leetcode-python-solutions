import unittest
from even_digits_counter import Solution


class TestEvenDigits(unittest.TestCase):
    def test_basic(self):
        data = [1, 22, 333, 4444, 55555, 666666]
        expected = 3
        solution = Solution()

        result = solution.findNumbers(data)
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()
