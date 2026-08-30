class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        memo = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            memo.append(max(memo[i-1], nums[i] + memo[i-2]))
        return memo[-1]


class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        memo = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            memo = [memo[-1], max(memo[-1], nums[i] + memo[-2])]
        return memo[-1]


# TODO improve! keys better be indices rather than looooooooong keys that deteriorate the hashmap performance
class Solution:
    def __init__(self):
        self.cache = {}
    def rob(self, nums) -> int:
        nums = tuple(nums)
        def rec(nums):
            if nums in self.cache:
                return self.cache[nums]
            if not nums:
                return 0
            if len(nums) <= 2:
                return max(nums)
            self.cache[nums] = nums[0] + max(rec(nums[2:]), rec(nums[3:]))
            return self.cache[nums]
        return max(rec(nums), rec(nums[1:]))



s = Solution()
assert s.rob([2,7,9,3,1]) == 12
