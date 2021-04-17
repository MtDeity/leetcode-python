from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count: int = 0
        prev: int = nums[0]
        for num in nums[1:]:
            if num > prev:
                prev = num
            else:
                prev += 1
                count += prev - num
        return count
