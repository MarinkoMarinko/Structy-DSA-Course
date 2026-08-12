class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(values):      # TC: O(n)
    dummy = Node(None)               # SC: O(n), where n is num of nodes
    tail = dummy

    for val in values:
        tail.next = Node(val)
        tail = tail.next

    return dummy.next
