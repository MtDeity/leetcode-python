class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = sum([self.transform(self.convert(c)) for c in s])
        for _ in range(k - 1):
            res = self.transform(res)
        return res

    def convert(self, c: str) -> int:
        return ord(c) - ord('a') + 1

    def transform(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total
