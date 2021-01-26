class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odd_rows, odd_cols, row_count, col_count = [False] * n, [False] * m, 0, 0
        for r, c in indices:
            odd_rows[r] = not odd_rows[r]
            odd_cols[c] = not odd_cols[c]
            row_count += 1 if odd_rows[r] else -1
            col_count += 1 if odd_cols[c] else -1
        return m * row_count + n * col_count - 2 * row_count * col_count
