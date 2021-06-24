from typing import List, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits: List[Tuple[int, int, str]] = []
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != '.':
                    digits += [(i, -1, cell), (-1, j, cell),
                               (i // 3, j // 3, cell)]
        return len(digits) == len(set(digits))
