# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):    # TC: O(n)
    result = []                  # SC: O(n), where n is the number of nodes

    current = head
    while current is not None:
        result.append(current.val)
        current = current.next

    return result


def linked_list_values(head):
    values = []
    _linked_list_values(head, values)
    return values

def _linked_list_values(head, values):  # TC: O(n)
    if head is None:                    # SC: O(n), where n is the number of nodes
        return []

    values.append(head.val)
    _linked_list_values(head.next, values)