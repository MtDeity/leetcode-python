from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, price in enumerate(prices[1:]):
            if price > prices[i]:
                profit += price - prices[i]
        return profit
