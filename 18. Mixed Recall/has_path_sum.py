# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def has_path_sum(root, target):      # TC: O(n)
    if not root:                     # SC: O(n), where n is num of nodes
        return False

    if not root.left and not root.right and root.val == target:
        return True

    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)
