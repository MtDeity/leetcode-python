from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        if l1 > len(s2):
            return False
        c1 = Counter(s1)
        c2 = Counter(s2[:l1])
        for i, c in enumerate(s2[l1:]):
            if self.matches(c1, c2):
                return True
            c2[c] += 1
            c2[s2[i]] -= 1
        return self.matches(c1, c2)

    def matches(self, c1: dict[str, int], c2: dict[str, int]) -> bool:
        for k, v in c1.items():
            if c2[k] != v:
                return False
        return True
