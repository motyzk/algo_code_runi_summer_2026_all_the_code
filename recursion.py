def fact(n):
    if not n:  # if n == 0:
        return 1
    return n * fact(n - 1)


assert fact(3) == 6
assert fact(4) == 24


def fib(n):
    if n < 3:
        return 1
    return fib(n - 2) + fib(n - 1)


memo = {}


def fib(n):
    if n < 3:
        return 1
    if n not in memo:
        memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]


memo = {1: 1, 2: 1}


def fib(n):
    if n not in memo:
        memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]


assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3


# print(fib(60))


def my_sum(l):
    if not len(l):
        return 0
    return l[0] + my_sum(l[1:])


def my_sum(l, carry=0):
    if not len(l):
        return carry
    return my_sum(l[1:], carry + l[0])


def my_sum(l):
    def helper(i):
        if i == len(l):
            return 0
        return l[i] + helper(i+1)
    return helper(0)


nums = [1, 2, 3, 4, 6, 7, 90]
assert my_sum(nums) == sum(nums)
nums = []
assert my_sum(nums) == sum(nums)
nums = [0]
assert my_sum(nums) == sum(nums)
nums = [1, 2, 3, 4, 6, 7, 90, 1, 2, 3, 4, 6, 7, 90]
assert my_sum(nums) == sum(nums)


def flip_in_pairs(n):
    pass


assert flip_in_pairs(2841) == 8214
assert flip_in_pairs(9) == 9
assert flip_in_pairs(90) == 9
assert flip_in_pairs(123) == 132
assert flip_in_pairs(91) == 19
assert flip_in_pairs(100) == 100




