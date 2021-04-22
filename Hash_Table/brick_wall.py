from typing import Dict, List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count: Dict[int, int] = defaultdict(int)
        for row in wall:
            acc = 0
            for brick in row[:-1]:
                acc += brick
                count[acc] += 1
        return len(wall) - max(count.values() or [0])
