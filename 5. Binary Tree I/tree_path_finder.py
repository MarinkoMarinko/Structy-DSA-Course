# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):              # TC: O(n)
    result = _path_finder(root, target)     # SC: O(n), where n is num of nodes
    return result[::-1] if result else None

def _path_finder(root, target):
    if not root:
        return None

    if root.val == target:
        return [ root.val ]

    left_path = _path_finder(root.left, target)
    if left_path:
        left_path.append(root.val)
        return left_path

    right_path = _path_finder(root.right, target)
    if right_path:
        right_path.append(root.val)
        return right_path

    return None