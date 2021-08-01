class Solution:
    def isThree(self, n: int) -> bool:
        return self.countDivisor(n) == 3

    def countDivisor(self, n: int) -> int:
        return sum([n % i == 0 for i in range(1, n + 1)])
