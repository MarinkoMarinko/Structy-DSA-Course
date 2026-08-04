# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):  # TC: O(n)
    current = head                   # SC: O(1), where n is the number of nodes
    while current is not None:
        if current.val == target:
            return True
        current = current.next

    return False

def linked_list_find(head, target):  # TC: O(n)
    if head is None:                 # SC: O(n), where n is the number of nodes
        return False

    if head.val == target:
        return True

    return linked_list_find(head.next, target)