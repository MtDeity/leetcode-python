class Solution:
    def sortString(self, s: str) -> str:
        result = []
        s = list(s)
        while s:
            for c in sorted(set(s)):
                s.remove(c)
                result.append(c)
            for c in sorted(set(s), reverse=True):
                s.remove(c)
                result.append(c)
        return "".join(result)
