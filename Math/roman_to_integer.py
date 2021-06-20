symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        num = prev = 0
        for c in s[::-1]:
            cur = symbols[c]
            if cur < prev:
                num -= cur
            else:
                num += cur
            prev = cur
        return num
