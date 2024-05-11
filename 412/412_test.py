import unittest
from example_412 import fizzBuzz

class Test412(unittest.TestCase):
    def test_basic(self):
        data = 3
        expectedResult = ["1", "2 - Add Two Numbers", "Fizz"]
        result = fizzBuzz(data)
        self.assertEqual(result, expectedResult)

if __name__ == '__main__':
    unittest.main()