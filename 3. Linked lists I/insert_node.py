class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):        # TC: O(n)
    new = Node(value)                       # SC: O(1)
    if index == 0:
        new.next = head
        head = new
    else:
        prev = head
        current = head.next
        count_index = 1
        while count_index != index:
            prev = prev.next
            current = current.next
            count_index += 1
        prev.next = new
        new.next = current
    return head