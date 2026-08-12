def lexical_order(word_1, word_2, alphabet):
    char_index = {}
    for idx, char in enumerate(alphabet):
        char_index[char] = idx

    i = 0
    while i < len(word_1) and i < len(word_2):
        char_1 = word_1[i]
        char_2 = word_2[i]
        if char_index[char_1] < char_index[char_2]:
            return True
        if char_index[char_1] > char_index[char_2]:
            return False

        i += 1

    return i == len(word_1)