class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = min(x, 46340)
        mid: int = (low + high) // 2
        while x < mid * mid or x >= (mid + 1) * (mid + 1):
            if x < mid * mid:
                high = mid - 1
            elif x >= (mid + 1) * (mid + 1):
                low = mid + 1
            mid = (low + high) // 2
        return mid
