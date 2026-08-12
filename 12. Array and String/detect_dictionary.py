def detect_dictionary(dictionary, alphabet):    # TC: O(nk)
    char_index = {}                             # SC: O(1), where n = len(dictionary) and k = len of longest word in dictionary
    for idx, char in enumerate(alphabet):
        char_index[char] = idx

    for i in range(0, len(dictionary) - 1):
        if is_ordered(dictionary[i], dictionary[i + 1], char_index) == False:
            return False

    return True


def is_ordered(word_1, word_2, alphabet):
    i = 0
    while i < len(word_1) and i < len(word_2):
        char_1 = word_1[i]
        char_2 = word_2[i]
        if alphabet[char_1] > alphabet[char_2]:
            return False
        elif alphabet[char_1] < alphabet[char_2]:
            return True
        i += 1
    return i == len(word_1)    