from collections import Counter    

def intersection_with_dupes(a, b):   # TC: O(n + m)
    count_a = Counter(a)             # SC: O(n + m), where n = len(a) and m = len(b)
    count_b = Counter(b)
    result = []

    for elem in count_a:
        for i in range(0, min(count_a[elem], count_b[elem])):
            result.append(elem)

    return result
