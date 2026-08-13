# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def lowest_common_ancestor(root, val1, val2):    # TC: O(n)
    path1_set = set(find_path(root, val1))       # SC: O(n), where n is num of nodes
    path2 = find_path(root, val2)
    for val in path2:
        if val in path1_set:
            return val
    return None

def find_path(root, target):
    if not root:
        return None

    if root.val == target:
        return [ root.val ]

    left_path = find_path(root.left, target)
    if left_path:
        left_path.append(root.val)
        return left_path

    right_path = find_path(root.right, target)
    if right_path:
        right_path.append(root.val)
        return right_path

    return None