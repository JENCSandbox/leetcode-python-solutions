# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_result_list = ListNode(0, None)
        temp_result_list = head_result_list
        carry = 0
        temp_l1 = l1
        temp_l2 = l2

        while temp_l1 is not None or temp_l2 is not None:
            n_l1 = temp_l1.val if temp_l1 is not None else 0
            n_l2 = temp_l2.val if temp_l2 is not None else 0

            n_result = (n_l1 + n_l2 + carry) % 10
            carry = (n_l1 + n_l2 + carry) // 10

            temp_result_list.val = n_result

            temp_l1 = temp_l1.next if temp_l1 is not None else None
            temp_l2 = temp_l2.next if temp_l2 is not None else None

            if temp_l1 is not None or temp_l2 is not None:
                temp_result_list.next = ListNode(0, None)
                temp_result_list = temp_result_list.next

        if carry > 0:
            temp_result_list.next = ListNode(carry,None)
        return head_result_list


l1 = ListNode(1, ListNode(1, ListNode(1, None)))
l2 = ListNode(1, ListNode(1, ListNode(1, None)))

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
temp = l3
while temp is not None:
    print(temp.val, end='->')
    temp = temp.next


print()


l1 = ListNode(2, ListNode(4, ListNode(5, None)))
l2 = ListNode(1, ListNode(1, ListNode(1, None)))

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
temp = l3
while temp is not None:
    print(temp.val, end='->')
    temp = temp.next

print()
l1 = ListNode(9, ListNode(4, ListNode(5, None)))
l2 = ListNode(1, ListNode(1, ListNode(1, None)))

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
temp = l3
while temp is not None:
    print(temp.val, end='->')
    temp = temp.next


print()
l1 = ListNode(9, ListNode(9, None))
l2 = ListNode(1, ListNode(1, ListNode(1, None)))

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
temp = l3
while temp is not None:
    print(temp.val, end='->')
    temp = temp.next

