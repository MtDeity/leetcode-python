from collections import Counter
from typing import Dict, List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diffs: Dict[int, int] = Counter([n - int(str(n)[::-1]) for n in nums])
        return sum((v * (v - 1)) // 2 for v in diffs.values()) % (10 ** 9 + 7)
