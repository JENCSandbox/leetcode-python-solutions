# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(0, None)
        result_temp = result_head

        nth_node = head
        while nth_node is not None:
            if nth_node.val == 0 and result_temp.val != 0:
                if nth_node.next is not None:
                    result_temp.next = ListNode(0, None)
                    result_temp = result_temp.next
            elif nth_node.val != 0:
                result_temp.val += nth_node.val

            nth_node = nth_node.next

        return result_head

