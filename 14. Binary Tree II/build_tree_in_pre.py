class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree_in_pre(in_order, pre_order):    # TC: O(n^2)
    if len(in_order) == 0:                     # SC: O(n^2), where n = len(array)
        return None

    val = pre_order[0]
    root = Node(val)
    mid = in_order.index(val)
    left_in = in_order[:mid]
    right_in = in_order[mid + 1:]
    left_pre = pre_order[1 : 1 + len(left_in)]
    right_pre = pre_order[1 + len(left_in):]
    root.left = build_tree_in_pre(left_in, left_pre)
    root.right = build_tree_in_pre(right_in, right_pre)
    return root
  

def build_tree_in_pre(in_order, pre_order):   # TC: O(n)
    in_order_index = {}                       # SC: O(n), where n = len(array)
    for i in range(0, len(in_order)):
        ele = in_order[i]
        in_order_index[ele] = i
    return _build_tree_in_pre(in_order, pre_order, in_order_index, 0, len(in_order) - 1, 0, len(pre_order) - 1)
  
def _build_tree_in_pre(in_order, pre_order, in_order_index, in_start, in_end, pre_start, pre_end):
    if in_end < in_start:
        return None
    value = pre_order[pre_start]
    root = Node(value)
    mid = in_order_index[value]
    left_size = mid - in_start
    root.left = _build_tree_in_pre(in_order, pre_order, in_order_index, in_start, mid - 1, pre_start + 1, pre_start + left_size)
    root.right = _build_tree_in_pre(in_order, pre_order, in_order_index, mid + 1, in_end, pre_start + left_size + 1, pre_end)
    return root