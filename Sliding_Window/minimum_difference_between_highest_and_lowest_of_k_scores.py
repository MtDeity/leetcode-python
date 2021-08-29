class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if k < 2:
            return 0
        k -= 1
        nums.sort()
        min_diff = nums[-1]
        for i in range(len(nums) - k):
            min_diff = min(min_diff, nums[i + k] - nums[i])
        return min_diff
