# import library
import unittest
from example_1480 import running_sum


class Test1480(unittest.TestCase):

    # define a function
    def test_basic(self):
        data = [3, 1, 2, 10, 1]
        result = running_sum(data)
        self.assertEqual(result, [3, 4, 6, 16, 17])


# driver code
if __name__ == '__main__':
    unittest.main()
