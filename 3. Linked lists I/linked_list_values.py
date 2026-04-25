class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# def linked_list_values(head):              # O(n)
#   current = head
#   result = []
#   while current is not None:
#     result.append(current.val)
#     current = current.next
#   return result


def linked_list_values(head):              # O(n)
  values = []
  _linked_list_values(head, values)
  return values

  
def _linked_list_values(head, values):      # helper function
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)
