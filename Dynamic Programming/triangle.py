from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i, row in enumerate(triangle[-2::-1]):
            prev = triangle[~i]
            for j in range(len(row)):
                row[j] += min(prev[j], prev[j + 1])
        return triangle[0][0]
