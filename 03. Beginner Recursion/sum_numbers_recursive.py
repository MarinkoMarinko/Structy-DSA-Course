def sum_numbers_recursive(numbers):      # TC: O(n^2)
    if len(numbers) == 0:                # SC: O(n^2), where n = len(numbers)
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])
