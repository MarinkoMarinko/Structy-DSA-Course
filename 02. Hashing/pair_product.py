def pair_product(numbers, target_product):  # TC: O(n)
    seen = {}                               # SC: O(n), where n = len(numbers)
    for i, num in enumerate(numbers):
        complement = target_product / num
        
        if complement in seen:
            return (seen[complement], i)
        
        seen[num] = i