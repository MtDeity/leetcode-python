from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp: List[int] = [num for num in nums]
        for i in range(1, len(dp)):
            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]
        return max(dp)
