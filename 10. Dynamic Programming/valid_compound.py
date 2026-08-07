def valid_compound(compound, elements):                  # TC: O(c * e)
    return _valid_compound(compound, elements, 0, {})    # SC: O(c), where c = len(compound) and e = len(elements)


def _valid_compound(compound, elements, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(compound):
        return True

    for elem in elements:
        if compound.startswith(elem.lower(), i) and _valid_compound(compound, elements, i + len(elem), memo):
            memo[i] = True
            return True

    memo[i] = False
    return False