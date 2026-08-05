# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):      # TC: O(n)
    values = []                    # SC: O(n), where n is num of nodes
    _depth_first_values(root, values)
    return values


def _depth_first_values(root, values):
    if root is None:
        return None

    values.append(root.val)
    _depth_first_values(root.left, values)
    _depth_first_values(root.right, values)

    return values
  