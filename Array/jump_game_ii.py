from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        cnt = left = 1
        right = nums[0]
        while right < len(nums) - 1:
            cnt += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right + 1, nxt
        return cnt
