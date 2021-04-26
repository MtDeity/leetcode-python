from typing import List
from heapq import heappop, heappush


class Solution:
    def furthestBuilding(
            self,
            heights: List[int],
            bricks: int,
            ladders: int) -> int:
        hq: List[int] = []
        hq_length = used_bricks = 0
        for i, height in enumerate(heights[:-1]):
            diff = heights[i + 1] - height
            if diff > 0:
                heappush(hq, diff)
                hq_length += 1
            if hq_length > ladders:
                used_bricks += heappop(hq)
                hq_length -= 1
            if used_bricks > bricks:
                return i
        return len(heights) - 1
