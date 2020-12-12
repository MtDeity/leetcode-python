class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        count = 0
        straight = 0
        i = 0
        while i < nums_len - 1:
            count += 1
            if nums[i] == nums[i + 1]:
                straight += 1
                if straight > 1:
                    count -= 1
                    nums_len -= 1
                    nums.pop(i)
                    i -= 1
            else:
                straight = 0
            i += 1
        return count + 1
