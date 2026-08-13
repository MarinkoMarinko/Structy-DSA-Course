def subsets(elements):          # TC: ~O(2^n)
    if not elements:            # SC: ~O(2^n), where n = len(elements)
        return [ [] ]

    first = elements[0]
    subsets_without_first = subsets(elements[1:])

    subsets_with_first = []
    for sub in subsets_without_first:
        subsets_with_first.append([first, *sub])

    return subsets_without_first + subsets_with_first