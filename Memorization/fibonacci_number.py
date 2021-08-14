class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        first = 0
        second = 1
        for _ in range(n - 1):
            first, second = second, first + second
        return second
