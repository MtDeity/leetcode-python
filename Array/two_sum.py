from typing import Dict, List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff: Dict[int, int] = defaultdict(int)
        for i, num in enumerate(nums):
            if num in diff:
                return [diff[num], i]
            diff[target - num] = i
        return []
