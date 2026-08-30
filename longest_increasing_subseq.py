# https://leetcode.com/problems/longest-increasing-subsequence

# brute force, O(n * 2**n)
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        sequences = [[nums[0]]]
        for i in range(1, len(nums)):
            curr_sequences = []
            for seq in sequences:
                if nums[i] > seq[-1]:
                    curr_sequences.append(seq+[nums[i]])
            sequences.extend(curr_sequences)
            sequences.append([nums[i]])
        return len(max(sequences, key=len))


# dynamic, O(n**2) time, O(n) space
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        longest_by_end = []
        for i in range(len(nums)):
            longest_by_end.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_by_end[i] = max(
                        longest_by_end[i],
                        longest_by_end[j] + 1
                    )
        return max(longest_by_end)


# not dynamic, O(nlogn) time, O(n) space
import bisect
class Solution:
    def lengthOfLIS(self, nums):
        longest = []
        for n in nums:
            i = bisect.bisect_left(longest, n)
            if i == len(longest):
                longest.append(n)
            longest[i] = n
        return len(longest)



s = Solution()
assert s.lengthOfLIS([1,2]) == 2
assert s.lengthOfLIS([20,1,2,3]) == 3
assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
