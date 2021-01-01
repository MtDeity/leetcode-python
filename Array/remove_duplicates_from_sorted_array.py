class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        i = 1
        for num in nums:
            if nums[i - 1] != num:
                nums[i] = num
                i += 1
        return i
