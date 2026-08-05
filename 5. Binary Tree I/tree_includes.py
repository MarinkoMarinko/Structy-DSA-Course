from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):    # TC: O(n)
    if not root:                    # SC: O(n), where n is num of nodes
        return False

    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)


def tree_includes(root, target):    # TC: O(n)
    if not root:                    # SC: O(n), where n is num of nodes
        return False

    nodes = deque([ root ])
    while nodes:
        node = nodes.popleft()
        if node.val == target:
            return True

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return False