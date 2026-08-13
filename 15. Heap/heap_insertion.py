class MinHeap:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def swap(self, index_1, index_2):
        self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]

    def upheap(self, index):
        current_index = index           
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.list[current_index] < self.list[parent_index]:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break

    def insert(self, val):            # TC: O(logn)
        self.list.append(val)         # SC: O(1), where n is num of items in heap
        self.upheap(self.size() - 1)