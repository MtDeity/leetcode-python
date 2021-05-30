from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mn = prices[0]
        for price in prices[1:]:
            profit = max(profit, price - mn)
            mn = min(mn, price)
        return profit
