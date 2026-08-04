# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):        # TC: O(n)
    total = 0              # SC: O(1), where n is the number of nodes

    current = head
    while current is not None:
        total += current.val
        current = current.next

    return total

def sum_list(head):      # TC: O(n)
    if head is None:     # SC: O(n), where n is the number of nodes
        return 0

    return head.val + sum_list(head.next)