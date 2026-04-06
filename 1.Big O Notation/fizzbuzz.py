def fizz_buzz(n):                       # O(n)
  list = []
  for i in range(1, n + 1):            
    if i % 3 == 0 and i % 5 == 0:
      list.append("fizzbuzz")
    elif i % 3 == 0:
      list.append("fizz")
    elif i % 5 == 0:
      list.append("buzz")
    else:
      list.append(i)
  return list


if __name__ == "__main__":
    print(fizz_buzz(11)) # -> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11]
    print(fizz_buzz(2)) # -> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11]
    print(fizz_buzz(16)) # -> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11]
    print(fizz_buzz(32)) # -> [1,2,"fizz",4,"buzz","fizz",7,8,"fizz","buzz",11]