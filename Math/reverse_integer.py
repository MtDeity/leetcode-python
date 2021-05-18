class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        rev_x = sign * int(str(sign * x)[::-1])
        if rev_x < -2 ** 31 or rev_x > 2 ** 31 - 1:
            return 0
        return rev_x
