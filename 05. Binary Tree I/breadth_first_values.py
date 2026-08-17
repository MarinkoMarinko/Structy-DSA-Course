from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):     # TC: O(n)
    if not root:                    # SC: O(n), where n is num of nodes
        return []

    result = []

    nodes = deque([ root ])
    while nodes:
        node = nodes.popleft()
        result.append(node.val)

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return result