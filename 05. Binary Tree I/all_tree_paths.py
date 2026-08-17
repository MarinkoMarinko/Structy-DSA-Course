# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):                # TC: O(n * logn)
    all_paths = _all_tree_paths(root)    # SC: O(n * logn), where n is num of nodes
    for path in all_paths:
        path.reverse()
    return all_paths

  
def _all_tree_paths(root):
    if not root:
        return []

    if not root.left and not root.right:
        return [[ root.val ]]

    all_paths = []

    left_paths = _all_tree_paths(root.left)
    for path in left_paths:
        path.append(root.val)
        all_paths.append(path)

    right_paths = _all_tree_paths(root.right)
    for path in right_paths:
        path.append(root.val)
        all_paths.append(path)

    return all_paths