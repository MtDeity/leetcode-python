class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum([self.toNum(c) * 26 ** i
                    for i, c in enumerate(reversed(columnTitle))])

    def toNum(self, c: str) -> int:
        return ord(c) - ord('A') + 1
