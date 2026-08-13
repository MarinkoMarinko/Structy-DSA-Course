# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def post_order(root):          # TC: O(n)
    values = []                # SC: O(n), where n is num of nodes
    _post_order(root, values)
    return values


def _post_order(root, values):
    if not root:
        return None

    _post_order(root.left, values)
    _post_order(root.right, values)
    values.append(root.val)
  