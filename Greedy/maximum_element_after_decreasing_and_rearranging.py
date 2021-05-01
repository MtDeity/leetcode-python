from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(
            self, arr: List[int]) -> int:
        arr.sort()
        pre = 0
        for n in arr:
            pre = min(pre + 1, n)
        return pre
