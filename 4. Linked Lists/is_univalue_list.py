# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):    # TC: O(n)
    current = head             # SC: O(1), where n is num of nodes
    while current:
        if current.val != head.val:
            return False
        current = current.next

    return True


def is_univalue_list(head, prev = None):    # TC: O(n)
    if not head:                            # SC: O(n), where n is num of nodes
        return True  

    if prev is not None and prev.val != head.val:
        return False

    return is_univalue_list(head.next, head)