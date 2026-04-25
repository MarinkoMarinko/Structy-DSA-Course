def pairs(elements):                      # O(n^2)
  result = []
  for i in range(0, len(elements)):
    for j in range(i + 1, len(elements)):
      pair = [ elements[i], elements[j] ]
      result.append(pair)
  return result


if __name__ == "__main__":
    print(pairs(["a", "b", "c"])) # ->
    # [
    #    ["a", "b"],
    #    ["a", "c"],
    #    ["b", "c"]
    # ]
    print(pairs(["a", "b", "c", "d"])) # ->
    # [
    #    ["a", "b"],
    #    ["a", "c"],
    #    ["a", "d"],
    #    ["b", "c"],
    #    ["b", "d"],
    #    ["c", "d"]
    # ]
    print(pairs(["cherry", "cranberry", "banana", "blueberry", "lime", "papaya"])) # ->
    # [ 
    #   [ "cherry", "cranberry" ], 
    #   [ "cherry", "banana" ], 
    #   [ "cherry", "blueberry" ], 
    #   [ "cherry", "lime" ], 
    #   [ "cherry", "papaya" ], 
    #   [ "cranberry", "banana" ], 
    #   [ "cranberry", "blueberry" ], 
    #   [ "cranberry", "lime" ], 
    #   [ "cranberry", "papaya" ], 
    #   [ "banana", "blueberry" ], 
    #   [ "banana", "lime" ], 
    #   [ "banana", "papaya" ], 
    #   [ "blueberry", "lime" ], 
    #   [ "blueberry", "papaya" ], 
    #   [ "lime", "papaya" ] 