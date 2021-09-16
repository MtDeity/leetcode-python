class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        spiral = [0] * m * n
        s_i = i = j = direction = 0
        while s_i < m * n:
            spiral[s_i] = matrix[i][j]
            matrix[i][j] = 101
            if direction == 0:
                if j + 1 >= n or matrix[i][j + 1] > 100:
                    i += 1
                    direction += 1
                else:
                    j += 1
            elif direction == 1:
                if i + 1 >= m or matrix[i + 1][j] > 100:
                    j -= 1
                    direction += 1
                else:
                    i += 1
            elif direction == 2:
                if j - 1 < 0 or matrix[i][j - 1] > 100:
                    i -= 1
                    direction += 1
                else:
                    j -= 1
            else:
                if matrix[i - 1][j] > 100:
                    j += 1
                    direction = 0
                else:
                    i -= 1
            s_i += 1
        return spiral
