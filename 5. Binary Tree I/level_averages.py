from collections import deque
from statistics import mean


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def level_averages(root):        # TC: O(n)
    levels = get_levels(root)    # SC: O(n), where n is num of nodes
    result = []
    for level in levels:
        result.append(mean(level))
    return result

def get_levels(root):
    if not root:
        return []

    levels = []

    nodes = deque([ (root, 0) ])
    while nodes:
        node, lvl = nodes.popleft()
        if len(levels) == lvl:
            levels.append( [node.val ])
        else:
            levels[lvl].append(node.val)

        if node.left:
            nodes.append((node.left, lvl + 1))
        if node.right:
            nodes.append((node.right, lvl + 1))

    return levels