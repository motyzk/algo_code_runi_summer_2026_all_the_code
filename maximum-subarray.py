def solve(nums):
    biggest_sum = max(nums)
    curr_sum = 0
    for n in nums:
        curr_sum += n
        if curr_sum > biggest_sum:
            biggest_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return biggest_sum


assert solve([2, 1, -30, 4, -1, 2, 1, -5, 4]) == 6
assert solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert solve([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == -1
# desired output - 6
# why? because 4, -1, 2, 1
# example input 2 - [1, 2, 3, 4]
# desired output - 10
# why? because 1, 2, 3, 4
# example input 3 - [1, -2, 3, 4]
# desired output - 7
# why? because 3, 4
