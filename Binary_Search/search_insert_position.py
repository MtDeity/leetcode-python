class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid: int = (s + e) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return s
