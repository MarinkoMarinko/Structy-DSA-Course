# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# SEE TC AND SC EXPLANATION BELOW!!!

def binary_search_tree_includes(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    if target < root.val:
        return binary_search_tree_includes(root.left, target)
    else:
        return binary_search_tree_includes(root.right, target)


def binary_search_tree_includes(root, target):
    current = root
    while current:
        if target < current.val:
            current = current.left
        elif target > current.val:
            current = current.right
        else:
            return True

    return False


# Recursive solution:
    # Worst case TC and SC: O(n) (if tree isn't balanced)
    # Best case TC and SC: O(log(n)) (if tree is balanced)

# Iterative solution:
    # Worst case TC: O(n) (if tree isn't balanced)
    # Best case TC: O(log(n)) (if tree is balanced)
    # O(1) SC in both cases