class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def remove_node(head, target_val):          # TC: O(n)
    if head.val == target_val:              # SC: O(1)
        return head.next
    prev = head
    current = head.next
    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break;
        prev = prev.next
        current = current.next
    return head
