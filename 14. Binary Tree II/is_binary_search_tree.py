# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def is_binary_search_tree(root):          # TC: O(n)
    values = []                           # SC: O(n), where n is num of nodes
    _in_order_traversal(root, values)

    for i in range(0, len(values) - 1):
        if values[i] > values[i + 1]:
            return False

    return True

def _in_order_traversal(root, values):
    if not root:
        return None

    _in_order_traversal(root.left, values)
    values.append(root.val)
    _in_order_traversal(root.right, values)