from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        is_decreacing = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if is_decreacing:
                    return False
                is_decreacing = True
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
        return True
