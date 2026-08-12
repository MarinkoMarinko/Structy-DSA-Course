class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, val):            # TC: O(1)
        new_node = Node(val)           # SC: O(1)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):                 # TC: O(1)
        if self.size == 0:             # SC: O(1)
            return None

        removed = self.head.val
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        self.size -= 1
        return removed