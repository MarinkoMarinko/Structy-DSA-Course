# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):        # TC: O(n)
    if not root:               # SC: O(n), where n is num of nodes
        return float("-inf")

    if not root.left and not root.right:
        return root.val

    left_sum = max_path_sum(root.left)
    right_sum = max_path_sum(root.right)

    return root.val + max(left_sum, right_sum)