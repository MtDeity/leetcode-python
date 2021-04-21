from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        half = sum(nums) // 2
        nums.sort(reverse=True)
        for i, num in enumerate(nums):
            half -= num
            if half < 0:
                return nums[:i + 1]
        return []
