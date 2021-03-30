import heapq
from typing import List, Tuple


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength_heap: List[Tuple[int, int]] = []
        heapq.heapify(strength_heap)
        for i, row in enumerate(mat):
            heapq.heappush(strength_heap, (self.get_strength(row), i))
        weakest: List[int] = []
        for _ in range(k):
            weakest.append(heapq.heappop(strength_heap)[1])
        return weakest

    def get_strength(self, row: List[int]) -> int:
        low = 0
        high = len(row) - 1
        mid = (low + high + 1) // 2
        while mid > 0 and low < high:
            mid = (low + high + 1) // 2
            if row[mid] == 0 and row[mid - 1] == 1:
                return mid
            elif row[mid] == 1:
                low = mid
            else:
                high = mid - 1
        return len(row) if row[0] else 0
