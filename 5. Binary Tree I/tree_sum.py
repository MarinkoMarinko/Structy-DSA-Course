from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):     # TC: O(n)
    if not root:        # SC: O(n), where n is num of nodes
        return 0

    return root.val + tree_sum(root.left) + tree_sum(root.right)


def tree_sum(root):     # TC: O(n)
    if not root:        # SC: O(n), where n is num of nodes
        return 0

    nodes = deque([ root ])
    s = 0
    while nodes:
        node = nodes.popleft()
        s += node.val

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return s