class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += 2 if (i == 0 or not grid[i - 1][j]) else 0
                    res += 2 if (j == 0 or not grid[i][j - 1]) else 0
        return res
