class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [0] * (rowIndex + 1)
        for i in (1, rowIndex + 1):
            for j in (i, 0, -1):
                res[j] += res[j - 1]
        return res
