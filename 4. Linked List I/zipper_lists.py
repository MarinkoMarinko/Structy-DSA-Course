# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):  # TC: O(min(n, m))
    tail = head_1                  # SC: O(1), where n = len of list1 and m = len of list2
    current_1 = head_1.next
    current_2 = head_2

    count = 0
    while current_1 and current_2:
        if count % 2 == 0:
            tail.next = current_2
            current_2 = current_2.next
        else:
            tail.next = current_1
            current_1 = current_1.next

        tail = tail.next
        count += 1

    if current_1:
        tail.next = current_1
    if current_2:
        tail.next = current_2

    return head_1


def zipper_lists(head_1, head_2):    # TC: O(min(n, m))
    if not head_1 and not head_2:    # SC: O(min(n, m)), where n = len of list1 and m = len of list2num of nodes
        return head_1

    if not head_1:
        return head_2

    if not head_2:
        return head_1

    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists(next_1, next_2)

    return head_1