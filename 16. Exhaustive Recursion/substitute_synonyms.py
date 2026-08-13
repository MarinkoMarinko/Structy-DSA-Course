def substitute_synonyms(sentence, synonyms):    # TC: ~O(m^n)
    words = sentence.split(' ')                 # SC: ~O(m^n), where m = max number of synonyms for a word and n is num of words in sentence
    subarrays = generate(words, synonyms)  
    return [ ' '.join(subarray) for subarray in subarrays ]


def generate(words, synonyms):
    if len(words) == 0:
        return [ [] ]

    first_word = words[0]
    subarrays = generate(words[1:], synonyms)

    if first_word in synonyms:
        result = []
        for synonym in synonyms[first_word]:
            result += [ [synonym, *subarray] for subarray in subarrays ]
        return result
    else:
        return [ [first_word, *subarray ] for subarray in subarrays ]