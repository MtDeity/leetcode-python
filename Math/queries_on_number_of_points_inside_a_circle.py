from typing import List
from math import sqrt


class Solution:
    def countPoints(self,
                    points: List[List[int]],
                    queries: List[List[int]]) -> List[int]:
        # (x - a) ** 2 + (y - b) ** 2 = r ** 2
        res: List[int] = [0] * len(queries)
        for i, query in enumerate(queries):
            a, b, r = query
            for x, y in points:
                distance: float = sqrt((x - a) ** 2 + (y - b) ** 2)
                if distance <= r:
                    res[i] += 1
        return res
