class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def sum_list(head):              # TC: O(n)
#   current = head                 # SC: O(1)
#   s = 0
#   while current is not None:
#     s += current.val
#     current = current.next
#   return s


def sum_list(head):                # TC: O(n)
  if head is None:                 # SC: O(n)
    return 0
  return head.val + sum_list(head.next)