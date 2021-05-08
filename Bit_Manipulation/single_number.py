from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(self.xor, nums, 0)

    def xor(self, x: int, y: int) -> int:
        return x ^ y
