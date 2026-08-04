# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):      # TC: O(n)
    if head.val == target_val:          # SC: O(1), where n is num of nodes
        return head.next

    prev = None
    current = head
    while current:
        if current.val == target_val:
            prev.next = current.next
            break

        prev = current
        current = current.next

    return head


def remove_node(head, target_val):    # TC: O(n)
    if not head:                      # SC: O(n), where n is num of nodes
        return None

    if head.val == target_val:
        return head.next

    head.next = remove_node(head.next, target_val)
    return head