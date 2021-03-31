from collections import Counter
from typing import Dict, List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq: Dict[int, int] = Counter(arr)
        return len(freq) == len(set(freq.values()))
