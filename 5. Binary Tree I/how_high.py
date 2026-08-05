# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):      # TC: O(n)
    if not root:         # SC: O(n), where n is num of nodes
        return -1

    return 1 + max(how_high(root.left), how_high(root.right))
