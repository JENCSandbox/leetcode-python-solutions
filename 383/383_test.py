import unittest
from example_383 import Solution

class Test383(unittest.TestCase):
    def test_basic(self):
        ransomeNote = "ab"
        magazine = "abcd"
        solution = Solution()
        result = solution.canConstruct(ransomeNote,magazine)
        self.assertEqual(result, True)

        ransomeNote = "xb"
        magazine = "abcd"
        result = solution.canConstruct(ransomeNote, magazine)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()