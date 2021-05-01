class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        for i, c in enumerate(s):
            if i % 2 == 0:
                res += c
            else:
                res += self.shift(s[i - 1], int(c))
        return res

    def shift(self, c: str, n: int) -> str:
        return chr(ord(c) + n)
