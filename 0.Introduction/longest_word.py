def longest_word(sentence):        # O(n)
    words = sentence.split(" ")    # list of words
    longest_word = ""
    for word in words:             # O(n)
        if len(word) >= len(longest_word):
            longest_word = word
    return longest_word


if __name__ == "__main__":
    print(longest_word("what a wonderful world")) # -> "wonderful"
    print(longest_word("have a nice day")) # -> "nice"
    print(longest_word("the quick brown fox jumped over the   lazy dog")) # -> "jumped"
    print(longest_word("who did eat the ham")) # -> "ham"
    print(longest_word("potato")) # -> "potato"