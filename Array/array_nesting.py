class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        mx = 0
        for i in range(len(nums)):
            count = 0
            while nums[i] >= 0:
                nums[i], i = -1, nums[i]
                count += 1
            mx = max(mx, count)
        return mx
