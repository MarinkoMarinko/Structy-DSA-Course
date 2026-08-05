from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def bottom_right_value(root):       # TC: O(n)
    nodes = deque([ root ])         # SC: O(n), where n is num of nodes
    while nodes:
        node = nodes.popleft()
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return node.val