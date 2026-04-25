class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# def get_node_value(head, index):        # TC: O(n)
#   counter = 0                           # SC: O(1)
#   current = head
#   while current is not None:
#     if counter == index:
#       return current.val
#     counter += 1
#     current = current.next
#   return None


def get_node_value(head, index):            # TC: O(n)
  if head is None:                          # SC: O(n)
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next, index - 1)