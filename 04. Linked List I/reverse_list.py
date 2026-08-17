# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):      # TC: O(n)
    prev = None              # SC: O(1), where n is num of nodes
    current = head

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def reverse_list(head, prev = None):  # TC: O(n)
    if head is None:                  # SC: O(n), where n is num of nodes
        return prev

    next = head.next
    head.next = prev
    return reverse_list(next, head)

  