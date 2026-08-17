def longest_word(sentence):          # TC: O(n)
  words = sentence.split(" ")        # SC: O(n), where n is number of words in sentence

  max_word = ""
  for word in words:
    if len(word) >= len(max_word):
      max_word = word

  return max_word