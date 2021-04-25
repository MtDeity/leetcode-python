from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix) // 2):
            for j in range((len(matrix[0]) + 1) // 2):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] \
                    = matrix[~j][i], matrix[i][j], matrix[j][~i], \
                    matrix[~i][~j]
