class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p = 0
        for i in range(1, n):
            p = (p + k) % (i + 1)
        return p + 1
