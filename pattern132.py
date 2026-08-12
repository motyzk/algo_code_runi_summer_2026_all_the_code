# https://leetcode.com/problems/132-pattern/

test_dict = {
    (1, 3, 2): True,
    (2, 3, 1): False,
    (-2, -3, 1): False,
    (-3, -1, -2): True,
    (-1, 1, 0, 1, 0): True,
    (5, 6, 7, 8): False,
    (-5, -6, -7, -8): False,
    (4, 3, 2, 1): False,
    (1, 2, 4, 3): True,
    (): False,
    (1, 2, 4): False,
    (2, 3, 1): False,
    (2,): False,
    (3, 4): False,
    tuple(range(1, 11)): False,
    (3, 5, 0, 3, 4): True,
    (-2, 1, 2, -2, 1, 2): True,
    (1, 0, 1, 2, 1, 2, 0, 1, 0, 0, 1, 1, 0, 2, 1, 2, 2, 1, 2, 0, 2, 0, 1, 0, 0, 0, 1, 1, 2, 1, 0, 1, 0, 2, 2, 0, 2, 1,
     2, 0, 2, 1, 0, 1, 2, 2, 1, 1, 0, 1, 1, 1, 2, 0, 1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 2, 2, 2, 0,
     1, 0, 0, 2, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 1, 2, 1, 0, 1, 2, 0, 1, 2, 1, 2, 1, 1, 1, 0, 0, 2, 0, 0, 1, 2, 0, 1, 1,
     1, 0, 2, 0, 1, 2, 1, 0, 2, 1, 0, 1, 2, 1, 0, 1, 2, 0, 1, 0, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 1, 2, 2, 0, 1, 1,
     0, 2, 0, 2, 0, 2, 2, 2, 0, 2, 1, 0, 0, 1, 0, 1, 0, 1, 2, 2, 2, 1, 1, 0, 0, 1, 2, 1, 0, 0, 2, 2, 0, 1, 0, 2, 0, 0,
     2, 2, 1, 1, 2, 1, 2, 1, 1, 0, 0, 1, 2, 0, 0, 2, 1, 2, 1, 0, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 0, 2, 1, 0, 2, 1,
     0, 0, 1, 2, 2, 0, 1, 0, 1, 2, 2, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 0, 1, 1, 0, 0, 2, 1, 0, 1, 2, 1,
     2, 1, 1, 2, 0, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 2, 2, 0, 0, 2, 0, 2, 2, 1, 0, 1, 0, 2, 1, 1, 0, 2, 0,
     2, 2, 1, 0, 1, 0, 2, 1, 1, 1, 2, 1, 2, 2, 1, 0, 1, 0, 2, 0, 0, 0, 0, 1, 1, 2, 0, 0, 2, 1, 2, 0, 1, 2, 2, 0, 1, 1,
     2, 1, 2, 1, 1, 0, 0, 1, 2, 1, 1, 1, 1, 2, 0, 2, 0, 2, 1, 2, 0, 1, 2, 1, 0, 2, 0, 0, 2, 1, 2, 1, 0, 2, 0, 0, 0, 2,
     2, 1, 1, 1, 2, 2, 1, 0, 2, 2, 2, 1, 1, 0, 0, 1, 1, 2, 1, 2, 0, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 1, 1, 0, 2,
     2, 1, 1, 2, 2, 1, 2, 1, 0, 2, 2, 1, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 1, 0, 0, 1, 2, 1, 0, 1, 0, 2, 0, 1, 1, 1, 0,
     1, 2, 2, 1, 1, 0, 0, 0, 2, 2, 0, 2, 1, 2, 0, 1, 0, 2, 0, 2, 1, 1, 1, 2, 1, 1, 0, 2, 2, 1, 1, 0, 0, 2, 2, 1, 2, 2,
     1, 1, 2, 1, 0, 1, 2, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 2, 2, 0, 1, 1, 1, 2, 2, 1, 1, 0, 1, 0, 2, 2, 0, 0, 1, 1, 1, 2,
     2, 1, 1, 0, 1, 0, 2, 0, 1, 2, 1, 2, 2, 2, 0, 1, 1, 2, 0, 1, 2, 1, 2, 1, 1, 0, 2, 1, 0, 0, 2, 2, 1, 0, 1, 2, 0, 2,
     0, 0, 0, 2, 0, 1, 2, 0, 1, 2, 1, 2, 2, 0, 0, 2, 1, 2, 0, 0, 2, 2, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 1,
     2, 0, 2, 2, 2, 2, 2, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2, 2, 1, 1, 0, 2, 2, 0, 2, 2, 1, 2, 1, 1, 0, 1, 0, 2, 1, 2,
     0, 1, 2, 2, 2, 0, 2, 0, 2, 2, 0, 1, 1, 2, 2, 2, 0, 0, 2, 2, 0, 0, 1, 2, 1, 0, 0, 0, 0, 2, 2, 1, 2, 1, 1, 2, 1, 2,
     2, 1, 0, 2, 1, 1, 2, 0, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 0, 2, 2, 1, 0, 0, 1, 0, 2, 0,
     2, 1, 0, 1, 2, 1, 1, 2, 2, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 2, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0,
     2, 1, 2, 2, 0, 0, 0, 0, 2, 1, 1, 2, 0, 1, 2, 2, 2, 2, 0, 1, 2, 1, 1, 0, 2, 2, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1, 2, 1,
     1, 2, 2, 0, 1, 0, 2, 1, 0, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 0, 2, 1, 2, 0, 1, 2, 1, 1, 1, 2, 2, 1, 0, 1, 1, 2, 0, 1,
     2, 0, 1, 2, 1, 2, 1, 1, 0, 2, 0, 2, 2, 1, 2, 1, 0, 2, 1, 2, 0, 2, 1, 1, 1, 2, 2, 2, 0, 2, 2, 2, 2, 0, 0, 1, 2, 2,
     0, 2, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 2, 1, 1, 0, 2, 0, 2, 2, 0, 0, 2,
     1, 1, 0, 2, 2, 1, 1, 2, 0, 2, 0, 0, 1, 0, 0, 1, 2, 2, 0, 0, 1, 1, 1, 0, 2, 2, 0, 2, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1,
     2, 2, 1, 1, 1, 0, 2, 1, 2, 0, 2, 2, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 1, 2, 2, 0, 1, 2, 1, 1, 2, 0, 1, 1, 1, 0, 1,
     0, 1, 0, 1, 1, 2, 1, 1, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 0, 1, 2, 2, 0, 0, 2, 1, 2, 0, 1, 2, 2, 2, 0, 1,
     1, 2, 1, 0): True,
}


# O(n**3)
class Solution:
    def find132pattern(self, nums):
        l = len(nums)
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    if i < j < k and nums[i] < nums[k] < nums[j]:
                        return True
        return False


# O(n**3)
class Solution:
    def find132pattern(self, nums):
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False


# O(n*(max(n)-min(n))) time, O(max(n)-min(n)) space
class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False
        glob_max = max(nums)
        glob_min = min(nums)
        range_dict = {k: False for k in range(glob_min, glob_max+1)}
        curr_range_min = curr_range_max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > curr_range_max:
                curr_range_max = nums[i]
                for k in range(curr_range_min+1, curr_range_max):
                    range_dict[k] = True
            if range_dict[nums[i]]:
                return True
            if nums[i] < curr_range_min:
                curr_range_min = curr_range_max = nums[i]
        return False


# algorithm with no code - does it work??? think about it
# if it works - implement it. if it doesn't - find an input that demonstrates it.
# find the max1, find the max2 in the subarray right to the max1, then look in the subarray left to max1,
# for a number smaller than max2. if you didn't find any - run this algorithm on the subarray left to max1 and the
# subarray right to max1
# class Solution:
#     def find132pattern(self, nums):
#         TODO implement


s = Solution()
for tpl, solution in test_dict.items():
    assert s.find132pattern(tpl) == solution, tpl