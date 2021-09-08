class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        acc = 0
        res = ''
        for i in reversed(range(len(s))):
            res += self.shift(s[i], shifts[i] + acc)
            acc += shifts[i]
        return res[::-1]

    def shift(self, s: str, n: int) -> str:
        return chr((ord(s) - ord('a') + n) % 26 + ord('a'))
