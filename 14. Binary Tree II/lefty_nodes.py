# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def lefty_nodes(root):            # TC: O(n)
    values = []                   # SC: O(n), where n is num of nodes
    _lefty_nodes(root, 0, values)
    return values


def _lefty_nodes(root, lvl, values):
    if not root:
        return None

    if len(values) == lvl:
        values.append(root.val)

    _lefty_nodes(root.left, lvl + 1, values)
    _lefty_nodes(root.right, lvl + 1, values)
  