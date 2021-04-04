from typing import List
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        total_diff: int = 0
        diffs: List[int] = []
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            total_diff += diff
            diffs.append(diff)
        mn = float('inf')
        sort1: List[int] = sorted(nums1)
        for n2, diff in zip(nums2, diffs):
            idx = bisect.bisect_left(sort1, n2)
            if idx > 0:
                mn = min(mn, total_diff - diff + abs(sort1[idx - 1] - n2))
            if idx < len(sort1):
                mn = min(mn, total_diff - diff + abs(sort1[idx] - n2))
        return mn % (10 ** 9 + 7)
