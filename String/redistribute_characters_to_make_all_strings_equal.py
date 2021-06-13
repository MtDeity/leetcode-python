from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter(''.join(words))
        return all([v % len(words) == 0 for v in counter.values()])
