from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = sorted(list(Counter(arr).values()), reverse=True)
        size = i = 0
        while size < len(arr) // 2:
            size += counter[i]
            i += 1
        return i
