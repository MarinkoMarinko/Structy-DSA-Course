class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def longest_streak(head):          # TC: O(n)
    max_count = 0                  # SC: O(1)
    count = 0
    current = head
    prev = head
    while current is not None:
        if current.val == prev.val:
            count += 1
        else: 
            count = 1
        if count > max_count:
            max_count = count
        prev = current
        current = current.next
    return max_count
