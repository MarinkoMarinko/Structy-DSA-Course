# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_cycle(head):      # TC: O(n)
    seen = set()                  # SC: O(n), where n is num of nodes
    current = head
    while current:
        if current.val in seen:
            return True
        seen.add(current.val)
        current = current.next

    return False


def linked_list_cycle(head):      # TC: O(n)
    slow = head                   # SC: O(1), where n is num of nodes
    fast = head
    first_iter = True
    while fast and fast.next:
        if not first_iter and slow == fast:
            return True
        first_iter = False
        slow = slow.next
        fast = fast.next.next

    return False