class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum: int = 0
        for account in accounts:
            max_sum = max(max_sum, sum(account))
        return max_sum
