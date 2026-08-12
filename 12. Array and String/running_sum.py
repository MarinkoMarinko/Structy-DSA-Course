def running_sum(numbers):      # TC: O(n)
    total = 0                  # SC: O(n), where n = len(numbers)

    result = []
    for num in numbers:
        total += num
        result.append(total)

    return result