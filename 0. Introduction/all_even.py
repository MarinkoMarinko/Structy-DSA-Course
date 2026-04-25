def all_even(nums):
    for num in nums:        # O(n)
        if num % 2 != 0:
            return False
    return True


if __name__ == "__main__":
    print(all_even([4, 90, 68, 6, -2])) # -> True
    print(all_even([14, 40, 36, 3])) # -> False
    print(all_even([30, 24, 2048, 0, 12, 50])) # -> True
    print(all_even([7, 7, 7, 7])) # -> False
    print(all_even([100])) # -> True
    print(all_even([1, 2, 4, 6, 8])) # -> False
    print(all_even([42, 18, 96, 4, 70, 12, 58, 30, 84, 26])) # -> True