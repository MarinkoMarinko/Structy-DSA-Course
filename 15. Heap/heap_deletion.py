class MinHeap:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def swap(self, index_1, index_2):
        self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]

    def sift_up(self, index):
        current_index = index
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.list[current_index] < self.list[parent_index]:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break

    def insert(self, val):
        self.list.append(val)
        self.sift_up(self.size() - 1)

    def downheap(self, index):
        current_index = index
        while current_index < self.size() - 1:
            left_index = current_index * 2 + 1
            right_index = current_index * 2 + 2

            left_val = float("inf") if left_index >= self.size() else self.list[left_index]
            right_val = float("inf") if right_index >= self.size() else self.list[right_index]

            smaller_val = min(left_val, right_val)
            smaller_index = left_index if left_val == smaller_val else right_index

            if self.list[current_index] > smaller_val:
                self.swap(current_index, smaller_index)
                current_index = smaller_index
            else:
                break
        
    def extract_min(self):      # TC: O(log(n))
        if self.is_empty():     # SC: O(1), where n is num of items in heap
            return

        if self.size() == 1:
            return self.list.pop()

        min_el = self.list[0]
        self.list[0] = self.list.pop()
        self.downheap(0)
        return min_el