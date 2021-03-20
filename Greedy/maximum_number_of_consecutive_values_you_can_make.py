class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        total_plus_one = 1
        for coin in sorted(coins):
            if coin > total_plus_one:
                break
            total_plus_one += coin
        return total_plus_one
