# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):    # TC: O(n)
    count = 0                       # SC: O(1), where n is the number of nodes

    current = head
    while current is not None:
        if count == index:
            return current.val
        count += 1
        current = current.next

    return None


def get_node_value(head, index):   # TC: O(n)
    if head is None:               # SC: O(n), where n is the number of nodes
        return None  

    if index == 0:
        return head.val

    return get_node_value(head.next, index - 1)