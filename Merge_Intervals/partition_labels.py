from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ends = {c: i for i, c in enumerate(S)}
        end = 0
        prev_end = -1
        sizes: List[int] = []
        for i, c in enumerate(S):
            end = max(end, ends[c])
            if i == end:
                sizes.append(i - prev_end)
                prev_end = i
        return sizes
