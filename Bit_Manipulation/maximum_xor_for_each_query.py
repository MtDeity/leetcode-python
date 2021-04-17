from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        length: int = len(nums)
        k: int = 2 ** maximumBit - 1
        res: List[int] = [0] * length
        for i in range(length):
            k ^= nums[i]
            res[~i] = k
        return res
