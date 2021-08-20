class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        row = {min(row) for row in matrix}
        col = {max(col) for col in zip(*matrix)}  # * = unpack
        return list(row & col)
