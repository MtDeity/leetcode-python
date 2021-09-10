class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            left += num
        return -1
