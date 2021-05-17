class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s < 1:
            return True
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i >= len_s:
                    return True
        return False
