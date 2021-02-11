import collections

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0
        num_count = collections.Counter(nums)
        for key, value in num_count.items():
            total += key if value == 1 else 0
        return total
