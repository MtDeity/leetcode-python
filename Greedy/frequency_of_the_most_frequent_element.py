from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        left = 0
        nums.sort()
        for right, num in enumerate(nums):
            k += num
            if (right - left + 1) * num > k:
                k -= nums[left]
                left += 1
        return len(nums) - left
