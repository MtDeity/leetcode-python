from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        i = 0
        for num in nums:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return i + 1
