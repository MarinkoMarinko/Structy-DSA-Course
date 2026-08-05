# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):            # TC: O(n)
    leaves = []                 # SC: O(n), where n is num of nodes
    _leaf_list(root, leaves)
    return leaves


def _leaf_list(root, leaves):
    if not root:
        return None

    if not root.left and not root.right:
        leaves.append(root.val)

    _leaf_list(root.left, leaves)
    _leaf_list(root.right, leaves)