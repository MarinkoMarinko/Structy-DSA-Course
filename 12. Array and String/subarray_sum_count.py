from collections import Counter

def subarray_sum_count(numbers, target_sum):    # TC: O(n)
    total = 0                                   # SC: O(n), where n = len(numbers)
    prefix_sums = [ 0 ]

    for num in numbers:
        total += num
        prefix_sums.append(total)

    seen = Counter()
    count = 0
    for current in prefix_sums:
        complement = current - target_sum
        count += seen[complement]
        seen[current] += 1

    return count