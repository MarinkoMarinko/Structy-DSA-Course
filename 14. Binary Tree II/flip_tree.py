# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):        # TC: O(n)
    if not root:            # SC: O(n), where n is num of nodes
        return None

    left = flip_tree(root.left)
    right = flip_tree(root.right)
    root.left = right
    root.right = left

    return root