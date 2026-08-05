class Solution:
    def singleNumber(self, nums, k):
        pos_result = 0
        neg_result = 0
        for i in range(32):
            pos_curr = 0
            neg_curr = 0
            for n in nums:
                if n > 0 and (n & (1 << i)):
                    pos_curr += 1
                if n < 0 and (-n & (1 << i)):
                    neg_curr += 1
            pos_result += (pos_curr % k) * (2 ** i)
            neg_result += (neg_curr % k) * (2 ** i)
        return pos_result - neg_result

s = Solution()
assert s.singleNumber([2, 2, 2, 1], 3) == 1
assert s.singleNumber([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], 10) == 1
assert s.singleNumber([2, 2, 4, 4, 1], 2) == 1
assert s.singleNumber([2, 2, 4, 4, 2, 4, 4, 2, -1], 4) == -1
