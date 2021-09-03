class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1
        a = 0
        b = c = 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
