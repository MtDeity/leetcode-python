from typing import Set


class Solution:
    def isHappy(self, n: int) -> bool:
        seen: Set[int] = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = self.get_square_sum(n)
        return False

    def get_square_sum(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        return res
