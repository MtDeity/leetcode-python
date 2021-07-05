from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        candidate = nums[0]

        for num in nums[1:]:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
