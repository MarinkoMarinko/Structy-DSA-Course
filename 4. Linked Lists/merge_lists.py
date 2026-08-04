class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):    # TC: O(min(n, m))
    dummy = Node(None)              # SC: O(1), where n = len of list1 and m = len of list2
    tail = dummy

    current_1 = head_1
    current_2 = head_2
    while current_1 and current_2:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next

        tail = tail.next

    if current_1:
        tail.next = current_1
    if current_2:
        tail.next = current_2

    return dummy.next

def merge_lists(head_1, head_2):    # TC: O(min(n, m))
    if not head_1 and not head_2:   # SC: O(min(n, m)), where n = len of list1 and m = len of list2
        return None

    if not head_1:
        return head_2

    if not head_2:
        return head_1

    if head_1.val < head_2.val:
        next_1 = head_1.next
        head_1.next = merge_lists(next_1, head_2)
        return head_1
    else:
        next_2 = head_2.next
        head_2.next = merge_lists(head_1, next_2)
        return head_2