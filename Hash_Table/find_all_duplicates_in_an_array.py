class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res: list[int] = list()
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                res.append(abs(num))
        return res
