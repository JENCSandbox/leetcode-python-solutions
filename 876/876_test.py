import unittest
from example_876 import *

class Test876(unittest.TestCase):
    def test_basic(self):
        # 1 - 2 - Add Two Numbers - 3 - Longest Substring Without Repeating Characters - 4 - Median of Two Sorted Arrays - 5 - Longest Palindromic Substring
        headNode1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
        headNode2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))

        head = headNode1
        expectedValue = 3
        solution = Solution()
        result = solution.middleNode(head=head)
        self.assertEqual(result.val, expectedValue)

        head = headNode2
        expectedValue = 4
        result = solution.middleNode(head=head)
        self.assertEqual(result.val, expectedValue)

if __name__ == '__main__':
    unittest.main()
