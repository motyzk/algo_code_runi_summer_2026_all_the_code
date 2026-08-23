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


s = Solution()
assert s.lengthOfLIS([1,2]) == 2
assert s.lengthOfLIS([20,1,2,3]) == 3
assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4