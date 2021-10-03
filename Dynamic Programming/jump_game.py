class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dist = len(nums) - 1
        for i in range(dist - 1, -1, -1):
            if i + nums[i] >= dist:
                dist = i
        return dist <= 0
