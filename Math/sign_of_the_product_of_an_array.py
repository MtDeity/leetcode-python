from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res: int = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                res *= -1
        return res
