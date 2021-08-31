class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        mid = (left + right) // 2
        while nums[mid] < nums[mid + 1]:
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return nums[mid + 1]
