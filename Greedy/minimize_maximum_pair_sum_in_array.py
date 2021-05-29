from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return max(
            asc + desc for asc, desc in zip(
                sorted(nums),
                sorted(nums,reverse=True)))
