from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        for price in prices[1:]:
            if price > low:
                profit += price - low
            low = price
        return profit
