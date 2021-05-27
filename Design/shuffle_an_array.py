from random import randrange
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.nums = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        # random.shuffle(self.nums)
        for i in range(len(self.nums)):
            j = randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
