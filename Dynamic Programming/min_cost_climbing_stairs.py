from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_2 = cost[0]
        prev_1 = cost[1]
        for c in cost[2:]:
            prev_2, prev_1 = prev_1, min(prev_2, prev_1) + c
        return min(prev_2, prev_1)
