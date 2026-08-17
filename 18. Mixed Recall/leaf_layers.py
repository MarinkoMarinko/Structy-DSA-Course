# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_layers(root):          # TC: O(n)
    layers = []                 # SC: O(n), where n is num of nodes
    _leaf_layers(root, layers)
    return layers

def _leaf_layers(root, layers):
    if not root:
        return -1

    left_height = _leaf_layers(root.left, layers)
    right_height = _leaf_layers(root.right, layers)

    height = 1 + max(left_height, right_height)

    if len(layers) == height:
        layers.append( [] )

    layers[height].append(root.val)

    return height