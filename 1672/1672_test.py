import unittest
from example_1672 import maximumWealth_2


class Test1672(unittest.TestCase):
    def test_basic(self):
        data = [[1, 1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1]]
        result = maximumWealth_2(data)
        self.assertEqual(result,8)


if __name__ == '__main__':
    unittest.main()
