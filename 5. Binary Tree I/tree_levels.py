from collections import deque


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_levels(root):      # TC: O(n)
    if not root:            # SC: O(n), where n is num of nodes
        return []

    result = []

    nodes = deque([ (root, 0) ])
    while nodes:
        node, lvl = nodes.popleft()

        if len(result) == lvl:
            result.append([ node.val ])
        else:
            result[lvl].append(node.val)

        if node.left:
            nodes.append((node.left, lvl + 1))
        if node.right:
            nodes.append((node.right, lvl + 1))

    return result