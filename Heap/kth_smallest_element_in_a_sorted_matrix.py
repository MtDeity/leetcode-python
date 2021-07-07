from typing import List, Union
from heapq import heappop, heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hq: List[List[Union[int, List[int]]]] = []
        for i in range(min(k, len(matrix))):
            heappush(hq, [matrix[i][0], matrix[i], 0])
        kth_min = matrix[0][0]
        count = 0
        while hq:
            kth_min, row, i = heappop(hq)
            count += 1
            if count == k:
                break
            if i + 1 < len(row):  # type: ignore
                heappush(hq, [row[i + 1], row, i + 1])  # type: ignore
        return kth_min  # type: ignore
