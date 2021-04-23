class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = prev = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                count += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return count + min(prev, cur)
