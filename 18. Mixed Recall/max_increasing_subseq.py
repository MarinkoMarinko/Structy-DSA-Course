def max_increasing_subseq(numbers):                                 # TC: O(n^2)
    return _max_increasing_subseq(numbers, 0, float("-inf"), {})    # SC: O(n^2), where n = len(numbers) 


def _max_increasing_subseq(numbers, i, prev, memo):
    key = (i, prev)

    if key in memo:
        return memo[key]
    if i == len(numbers):
        return 0

    current = numbers[i]
    options = []
    without_current = _max_increasing_subseq(numbers, i + 1, prev, memo)
    options.append(without_current)

    if current > prev:
        with_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo)
        options.append(with_current)

    memo[key] = max(options)
    return max(options)
