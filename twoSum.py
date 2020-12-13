class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Brute Force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j > i and nums[i] + nums[j] == target:
        #             break
        #     else:
        #         continue
        #     break
        # return [i, j]

        # One-pass Hash Table
        dict = {}
        for i, num in enumerate(nums):
            if num in dict:
                return [dict[num], i]
            else:
                diff = target - num
                dict[diff] = i
