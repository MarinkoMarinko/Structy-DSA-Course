class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):    # TC: O(n)
    if index == 0:                      # SC: O(1), where n is num of nodes
        new_head = Node(value)
        new_head.next = head
        return new_head

    count = 0
    current = head
    while current:
        if count == index - 1:
            temp = current.next
            current.next = Node(value)
            current.next.next = temp

        count += 1
        current = current.next

    return head

def insert_node(head, value, index, count = 0):     # TC: O(n)
    if index == 0:                                  # SC: O(n), where n is num of nodes
        new_head = Node(value)
        new_head.next = head
        return new_head

    if not head:
        return None

    if count == index - 1:
        temp = head.next
        head.next = Node(value)
        head.next.next = temp
        return

    insert_node(head.next, value, index, count + 1)
    return head