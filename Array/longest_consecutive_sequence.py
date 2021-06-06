from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 in num_set:
                continue
            streak = 0
            while num in num_set:
                streak += 1
                num += 1
            longest = max(longest, streak)
        return longest
