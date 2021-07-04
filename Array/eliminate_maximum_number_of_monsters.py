from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        turns = [(d + s - 1) // s for d, s in zip(dist, speed)]
        turns.sort()
        for i in range(len(dist)):
            if turns[i] < i + 1:
                return i
        return len(dist)
