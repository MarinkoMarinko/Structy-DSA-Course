# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def is_tree_balanced(root):           # TC: O(n)
    res = _is_tree_balanced(root)     # SC: O(n), where n is num of nodes
    if res == -1:
        return False
    return True

def _is_tree_balanced(root):
    if not root:
        return 0

    left_height = _is_tree_balanced(root.left)
    if left_height == -1:
        return -1

    right_height = _is_tree_balanced(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1
    else:
        return 1 + max(left_height, right_height)