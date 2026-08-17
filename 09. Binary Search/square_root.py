def square_root(n):        # TC: O(logn)
    lo = 0                 # SC: O(1), where n is input
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        square = mid ** 2

        if square < n:
            lo = mid + 1
        elif square > n:
            hi = mid - 1
        else:
            return mid

    return hi