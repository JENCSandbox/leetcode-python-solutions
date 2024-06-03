import collections
from typing import Deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


node5 = TreeNode(5)
node4 = TreeNode(4)

node3 = TreeNode(3)
node3.left = node4
node3.right = node5

node2 = TreeNode(2)

node1 = TreeNode(1)
node1.left = node2
node1.right = node3


class Codec:
    def serialize(self, root):
        if root == None:
            return ''
        result = []
        de = collections.deque([root])
        while bool(de):
            node = de.popleft()
            data = node.val if node is not None else None
            result.append(data)
            if node is not None:
                de.append(node.left)
                de.append(node.right)
        return ','.join(map(str, result))

    def deserialize(self, data):
        if data == '':
            return None

        root = None

        def string_to_int (str):
            if str == 'None':
                return None
            else:
                return int(str)
        data_as_list = map(string_to_int, data.split(','))

        data_queue = collections.deque(data_as_list)

        temp_deque = collections.deque()
        temp_deque.append(TreeNode(data_queue.popleft()))

        while bool(temp_deque):

            node = temp_deque.popleft()
            left = data_queue.popleft()
            right = data_queue.popleft()

            if root is None:
                root = node

            if left is not None:
                left_node = TreeNode(left)
                node.left = left_node
                temp_deque.append(left_node)
            else:
                node.left = left

            if right is not None:
                right_node = TreeNode(right)
                node.right = right_node
                temp_deque.append(right_node)
            else:
                node.right = right

        return root


raw_serialized = '1,2,3,None,None,4,5,None,None,None,None'
deser = Codec()
tree = deser.deserialize(raw_serialized)
ser = Codec()
serialized_tre = ser.serialize(tree)

print(raw_serialized)
print(serialized_tre)

raw_serialized = ''
deser = Codec()
tree = deser.deserialize(raw_serialized)
ser = Codec()
serialized_tre = ser.serialize(tree)