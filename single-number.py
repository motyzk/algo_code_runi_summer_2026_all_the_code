# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums):
        seen_odd_num_of_times = set()
        for n in nums:
            if n in seen_odd_num_of_times:
                seen_odd_num_of_times.remove(n)
            else:
                seen_odd_num_of_times.add(n)
        return seen_odd_num_of_times.pop()

    def singleNumber(self, nums):
        single = 0
        for num in nums:
            single ^= num  # single = single ^ num
        return single

    # only works for positive numbers
    def singleNumber(self, nums):
        single = 0
        for i in range(15):
            curr = 0
            for n in nums:
                if (n & (1 << i)):
                    curr += 1
            single += (curr % 2) * (2 ** i)
        return single

    def singleNumber(self, nums):
        pos_result = 0
        neg_result = 0
        for i in range(15):
            pos_curr = 0
            neg_curr = 0
            for n in nums:
                if n > 0 and (n & (1 << i)):
                    pos_curr += 1
                if n < 0 and (-n & (1 << i)):
                    neg_curr += 1
            pos_result += (pos_curr % 2) * (2 ** i)
            neg_result += (neg_curr % 2) * (2 ** i)
        return pos_result - neg_result

s = Solution()
assert s.singleNumber([2, 2, 1]) == 1
assert s.singleNumber([2, 2, -1]) == -1
assert s.singleNumber([2, 2, 4, 4, 1]) == 1
assert s.singleNumber([2, 4, 2, 4, 1]) == 1
assert s.singleNumber([2, 4, 2, 1, 4]) == 1
assert s.singleNumber([1]) == 1
assert s.singleNumber([2, -4, 2, -4, 1]) == 1
assert s.singleNumber(list(range(999)) + list(range(999)) + [999]) == 999
