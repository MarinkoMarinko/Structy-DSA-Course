# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flatten_tree(root):      # TC: O(n)
    prev = None              # SC: O(n), where n is num of nodes
    stack = [ root ]
    while stack:
        current = stack.pop()

        if prev:
            prev.right = current
        prev = current

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        current.left = None
        current.right = None

    return root