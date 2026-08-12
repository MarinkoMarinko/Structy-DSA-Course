class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_lists(head_1, head_2):        # TC: O(max(n, m))
    dummy = Node(None)                # SC: O(max(n, m)), where n = len(list 1) and m = len(list 2)
    tail = dummy

    current_1 = head_1
    current_2 = head_2
    carry = 0
    while current_1 or current_2 or carry == 1:
        value_1 = current_1.val if current_1 else 0
        value_2 = current_2.val if current_2 else 0
        sum = value_1 + value_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10

        tail.next = Node(digit)
        tail = tail.next

        if current_1:
            current_1 = current_1.next
        if current_2:
            current_2 = current_2.next

    return dummy.next