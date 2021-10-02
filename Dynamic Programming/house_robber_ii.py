class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        num0, num1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            num0, num1 = num1, max(num1, num0 + nums[i])
        return max(num0, num1)
