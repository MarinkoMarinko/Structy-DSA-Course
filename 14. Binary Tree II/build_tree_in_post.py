class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_in_post(in_order, post_order):    # TC: O(n^2)
    if len(in_order) == 0:                       # SC: O(n^2), where n is len(array)
        return None

    val = post_order[-1]
    root = Node(val)
    mid = in_order.index(val)
    left_in = in_order[:mid]
    right_in = in_order[mid + 1:]
    left_post = post_order[:len(left_in)]
    right_post = post_order[len(left_in): -1]
    root.left = build_tree_in_post(left_in, left_post)
    root.right = build_tree_in_post(right_in, right_post)
    return root
  
  