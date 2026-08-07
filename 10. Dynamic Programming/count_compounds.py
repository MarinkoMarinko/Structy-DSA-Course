def count_compounds(compound, elements):                    # TC: O(c * e)
    return _count_compounds(compound, elements, 0, {})      # SC: O(c), where c = len(compound) and e = len(elements)


def _count_compounds(compound, elements, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(compound):
        return 1

    num_ways = 0
    for elem in elements:
        if compound.startswith(elem.lower(), i):
            num_ways += _count_compounds(compound, elements, i + len(elem), memo)

    memo[i] = num_ways
    return num_ways
