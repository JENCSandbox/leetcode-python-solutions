# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def length(self, head):
        length = 0
        tempNode = head
        while (tempNode.next != None):
            length = length + 1
            tempNode = tempNode.next
        return length

    def getAtPosition(self, head, position):
        currentPosition = 0
        tempNode = head
        while (currentPosition != position):
            tempNode = tempNode.next
            currentPosition = currentPosition + 1
        return tempNode

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = self.length(head)
        middle = length / 2 if length % 2 == 0 else (length + 1) / 2
        return self.getAtPosition(head, middle)

