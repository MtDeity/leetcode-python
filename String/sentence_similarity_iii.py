from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1: List[str] = sentence1.split()
        words2: List[str] = sentence2.split()
        while words1 and words2:
            if words1[0] == words2[0]:
                words1.pop(0)
                words2.pop(0)
            else:
                break
        while words1 and words2:
            if words1[-1] == words2[-1]:
                words1.pop()
                words2.pop()
            else:
                break
        return not words1 or not words2
