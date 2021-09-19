from collections import defaultdict


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        seen: dict[int, int] = defaultdict(int)
        cnt = 0
        for num in nums:
            cnt += seen[num - k] + seen[num + k]
            seen[num] += 1
        return cnt
