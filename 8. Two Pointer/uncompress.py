def uncompress(s):       # TC: O(n * m)
    nums = "123456789"   # SC: O(n * m), where n is number of groups and m is max number in any group       
    result = []

    i = j = 0
    while i < len(s):
        if s[j] in nums:
            j += 1
        else:
            num = int(s[i:j])
            result.append(s[j] * num)
            j += 1
            i = j

    return "".join(result)