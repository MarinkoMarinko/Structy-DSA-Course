import heapq

def kth_largest(numbers, k):      # TC: O(n * log(k))
    heap = []                     # SC: O(k), where n = len(numbers) and k is input
    for num in numbers:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)