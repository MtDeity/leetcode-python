class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        i, m = 0, len(grid[0])
        for row in reversed(grid):
            while i < m:
                if row[i] < 0:
                    count += m - i
                    break
                i += 1
        return count
