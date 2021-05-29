class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        return sum(s[i] is not s[i - 1] is not s[i - 2] is not s[i]
                   for i in range(2, len(s)))
