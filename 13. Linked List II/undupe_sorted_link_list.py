class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def undupe_sorted_linked_list(head):    # TC: O(n)
    dummy = Node(None)                  # SC: O(n), where n is num of nodes
    tail = dummy

    current = head
    while current:
        if current.val != tail.val:
            tail.next = Node(current.val)
            tail = tail.next
        current = current.next

    return dummy.next