# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        low = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif prices[i] - low > max_profit:
                max_profit = prices[i] - low
        return max_profit


class Solution:
    def maxProfit(self, prices):
        low = float("inf")
        max_profit = 0
        for price in prices:
            if price < low:
                low = price
            elif price - low > max_profit:
                max_profit = price - low
        return max_profit


s = Solution()
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([7, 6, 4, 3, 1]) == 0
assert s.maxProfit([6, 7, 4, 3, 1]) == 1
assert s.maxProfit([7, 6, 4, 3, 1, 2]) == 1
assert s.maxProfit([6, 7, 4, 3, 1, 2]) == 1
assert s.maxProfit([6, 7, 4, 6, 1]) == 2
assert s.maxProfit([7]) == 0
assert s.maxProfit([]) == 0
