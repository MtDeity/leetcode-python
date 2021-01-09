class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        words1 = "".join(word1)
        words2 = "".join(word2)
        return words1 == words2
