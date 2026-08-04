# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):  # TC: O(n)
    longest = 0            # SC: O(1), where n is num of nodes

    prev_val = None
    current = head
    while current:
        if current.val == prev_val:
            count += 1
        else:
            count = 1

        prev_val = current.val
        if count > longest:
            longest = count

        current = current.next

    return longest