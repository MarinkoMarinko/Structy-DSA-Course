# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_palindrome(head):    # TC: O(n)
    values = []                 # SC: O(n), where n is num of nodes

    current = head
    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]
