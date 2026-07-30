def fibonacci(n):       # TC: O(2^n)
    if n in [0, 1]:     # SC: O(n), where n is the input
        return n          

    return fibonacci(n - 2) + fibonacci(n - 1)


# The time and space complexity is explained well in Alvins approach video for this problem.

# a solution that is more optimized is shown in a later module called "Dynamic Programming".