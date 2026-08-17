def is_subsequence(string_1, string_2):  # TC: O(m)
    i = 0                                # SC: O(1), where m = len(string_2)
    j = 0
    while i < len(string_1) and j < len(string_2):
        if string_1[i] == string_2[j]:
            i += 1
            j += 1
        else:
            j += 1
        
    return i == len(string_1)