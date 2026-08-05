from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):      # TC: O(n)
    if not root:                         # SC: O(n), where n is num of nodes
        return 0

    left_count = tree_value_count(root.left, target)
    right_count = tree_value_count(root.right, target)

    if root.val == target:
        return 1 + left_count + right_count

    return left_count + right_count


def tree_value_count(root, target):      # TC: O(n)
    if not root:                         # SC: O(n), where n is num of nodes
        return 0

    count = 0

    nodes = deque([ root ])
    while nodes:
        node = nodes.popleft()
        if node.val == target:
            count += 1

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return count