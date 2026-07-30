from collections import defaultdict

def most_frequent_char(s):      # TC: O(n)
    count = defaultdict(int)    # SC: O(n), where n = len(s)
    for char in s:
        count[char] += 1

    most_frequent = s[0]
    for char in count:
        if count[char] > count[most_frequent]:
            most_frequent = char

    return most_frequent