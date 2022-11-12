class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(grid: list[list[str]], i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
        cnt = 0
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == '1':
                    cnt += 1
                    dfs(grid, i, j)
        return cnt
