class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]
            total += mat[i][- (i + 1)]
        if len(mat) % 2 == 1:
            mid = len(mat) // 2
            total -= mat[mid][mid]
        return total
