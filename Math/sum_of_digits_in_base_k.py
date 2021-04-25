class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n // k:
            return self.sumBase(n // k, k) + n % k
        return n
