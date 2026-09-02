# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# O(n**2) time, O(n) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            seen = set()
            curr_len = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                curr_len += 1
            longest = max(longest, curr_len)
        return longest


# O(n) time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


s = Solution()
s.lengthOfLongestSubstring("") == 0
s.lengthOfLongestSubstring("abc") == 3
s.lengthOfLongestSubstring("aa") == 1
s.lengthOfLongestSubstring("abcabcaaa") == 3
