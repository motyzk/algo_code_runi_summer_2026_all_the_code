# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums):
        xor_of_two_nums = 0
        for n in nums:
            xor_of_two_nums ^= n
        for bit in range(32):
            if xor_of_two_nums & (2 ** bit):
                break
        xor_where_bit_on = xor_where_bit_off = 0
        for n in nums:
            if n & (2 ** bit):
                xor_where_bit_on ^= n
            else:
                xor_where_bit_off ^= n
        return [xor_where_bit_on, xor_where_bit_off]


# using an existing solution but...not good! as it deteriorates space complexity
class Solution:
    def simpleSingleNumber(self, nums):
        single = 0
        for num in nums:
            single ^= num  # single = single ^ num
        return single
    def singleNumber(self, nums):
        xor_of_two_nums = 0
        for n in nums:
            xor_of_two_nums ^= n
        for bit in range(32):
            if xor_of_two_nums & (2 ** bit):
                break
        xor_where_bit_on = []
        xor_where_bit_off = []
        for n in nums:
            if n & (2 ** bit):
                xor_where_bit_on.append(n)
            else:
                xor_where_bit_off.append(n)
        return [self.simpleSingleNumber(xor_where_bit_off),
                self.simpleSingleNumber(xor_where_bit_on)]



s = Solution()
assert set(s.singleNumber([2, 2, 1, 3])) == {1, 3}
assert set(s.singleNumber([2, 2, -1, 1])) == {-1, 1}
assert set(s.singleNumber([2, 2, -1, -3])) == {-1, -3}
assert set(s.singleNumber([2, -1, 2, -3])) == {-1, -3}
assert set(s.singleNumber([2, 2, 4, 4, 1, 3])) == {1, 3}
assert set(s.singleNumber([2, 4, 2, 3, 4, 1])) == {1, 3}
assert set(s.singleNumber([2, 4, 2, 1, 3, 4])) == {1, 3}
assert set(s.singleNumber([1, 3])) == {1, 3}
assert set(s.singleNumber([3, 2, -4, 2, -4, 1])) == {1, 3}
assert set(s.singleNumber(list(range(999)) + list(range(999)) + [999, 1000])) == {999, 1000}
