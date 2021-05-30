class Solution:
    def isSumEqual(
            self,
            firstWord: str,
            secondWord: str,
            targetWord: str) -> bool:
        return self.toNum(firstWord) + \
            self.toNum(secondWord) == self.toNum(targetWord)

    def toNum(self, word: str) -> int:
        num = 0
        for c in word:
            num = num * 10 + ord(c) - ord('a')
        return num
