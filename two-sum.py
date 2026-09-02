# https://leetcode.com/problems/two-sum/

# O(n**2) naive
# TODO

# O(n) time, O(n) space
class Solution:
    def twoSum(self, nums, target):
        complements = {}
        for i, n in enumerate(nums):
            if n in complements:
                return [complements[n], i]
            complements[target-n] = i


s = Solution()
assert s.twoSum([1, 2, 3, 4], 5) == [1, 2]
