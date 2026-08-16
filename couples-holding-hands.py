# https://leetcode.com/problems/couples-holding-hands/description/

# O(n) time, O(n) space
class Solution:
    def minSwapsCouples(self, row):
        swaps = 0
        rev_map = {x: i for i, x in enumerate(row)}
        # print(rev_map)
        for i in range(0, len(row), 2):
            coupled_num = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
            coupled_num_i = rev_map[coupled_num]
            if coupled_num_i != i+1:
                rev_map[coupled_num], rev_map[row[i+1]] = rev_map[row[i+1]], rev_map[coupled_num]
                row[i+1], row[coupled_num_i] = row[coupled_num_i], row[i+1]
                swaps += 1
        return swaps


s = Solution()
assert s.minSwapsCouples([3, 2, 0, 1]) == 0
assert s.minSwapsCouples([0, 2, 1, 3]) == 1
# assert s.minSwapsCouples([]) == 0
# assert s.minSwapsCouples([0, 1]) == 0
