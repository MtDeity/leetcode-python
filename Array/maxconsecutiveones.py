class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = count = 0
        for num in nums:
            if num > 0:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
        return longest
