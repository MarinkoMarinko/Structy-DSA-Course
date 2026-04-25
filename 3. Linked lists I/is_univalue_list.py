class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def is_univalue_list(head):          # TC: O(n)
#   current = head.next                # SC: O(1)
#   while current is not None:
#     if current.val != head.val:
#       return False
#     current = current.next
#   return True


def is_univalue_list(head, prev_val = None):    # TC: O(n)
  if head is None:                              # SC: O(n)
    return True
  if prev_val is None or head.val == prev_val:
    return is_univalue_list(head.next, head.val)
  else:
    return False
