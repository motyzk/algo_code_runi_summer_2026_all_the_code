# 5n
def solve(nums):
    if len(nums) < 5:
        return sum(nums)
    left, right = 0, 5
    # TODO

# 5n
def solve(nums):
    if len(nums) < 5:
        return sum(nums)
    greatest = 0
    for i in range(5, len(nums)+1):
        curr = sum(nums[i-5:i])
        if curr > greatest:
            greatest = curr
    return greatest


# O(n)
def solve(nums):
    if len(nums) < 5:
        return sum(nums)
    greatest = sum(nums[:5])
    left, right = 0, 5
    while right < len(nums):
        curr = greatest - nums[left] + nums[right]
        greatest = max(greatest, curr)
        left += 1
        right += 1
    return greatest
    # TODO

assert solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 45, solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
assert solve([1, 2, 3, 4]) == 10