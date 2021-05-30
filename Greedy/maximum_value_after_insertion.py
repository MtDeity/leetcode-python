class Solution:
    def maxValue(self, n: str, x: int) -> str:
        is_negative = 1 if n[0] == '-' else 0
        for i in (range(is_negative, len(n))):
            if is_negative and x < int(n[i]) \
                    or not is_negative and x > int(n[i]):
                return n[:i] + str(x) + n[i:]
        return n + str(x)
