class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                left = a ** 2 + b ** 2
                root = int(left ** 0.5)
                if root <= n and left == root ** 2:
                    count += 2
        return count
