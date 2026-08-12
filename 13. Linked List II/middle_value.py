# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def middle_value(head):          # TC: O(n)
    values = []                  # SC: O(n), where n is num of nodes

    current = head
    while current:
        values.append(current.val)
        current = current.next

    return values[len(values) // 2]


def middle_value(head):          # TC: O(n)
    slow = head                  # SC: O(1), where n is num of nodes
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val
