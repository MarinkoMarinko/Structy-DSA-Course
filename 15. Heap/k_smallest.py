import heapq

def k_smallest(nums, k):        # TC: O(n * log(k))
    heap = []                   # SC: O(k), where n = len(nums) and k is input
    for num in nums:
        item = (-num, num)
        heapq.heappush(heap, item)
        if len(heap) > k:
            heapq.heappop(heap)

    result = []
    while len(heap) > 0:
        item = heapq.heappop(heap)
        result.append(item[1])

    return result[::-1]