def pairs(elements):        # TC: O(n^2)
  result = []               # SC: O(n^2), where n = len(elements)
  for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
      result.append([elements[i], elements[j]])

  return result