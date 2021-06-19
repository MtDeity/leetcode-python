from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        num1 = num2 = 0
        for num in nums:
            num1, num2 = num2, max(num1 + num, num2)
        return max(num1, num2)
