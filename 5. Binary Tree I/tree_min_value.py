from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):        # TC: O(n)
    if root is None:             # SC: O(n), where n is num of nodes
        return float("inf")

    left_min = tree_min_value(root.left)
    right_min = tree_min_value(root.right)
    return min(root.val, left_min, right_min)


def tree_min_value(root):       # TC: O(n)
    nodes = deque([ root ])     # SC: O(n), where n is num of nodes
    min_val = float("inf")
    while nodes:
        node = nodes.popleft()
        min_val = min(min_val, node.val)

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return min_val