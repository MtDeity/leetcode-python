class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = cur_sum = 0
        for i, num in enumerate(nums):
            if i > 0 and num <= nums[i - 1]:
                cur_sum = 0
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum
