def prefix_product(numbers):    # TC: O(n)
    total = 1                   # SC: O(n), where n = len(numbers)

    result = []
    for num in numbers:
        total *= num
        result.append(total)

    return result