from typing import List, Dict, Set
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(
        self,
        logs: List[List[int]],
        k: int
    ) -> List[int]:
        freqs: Dict[int, Set[int]] = defaultdict(set)
        for id_, time in logs:
            freqs[id_].add(time)
        answer: List[int] = [0] * k
        for key in freqs:
            answer[len(freqs[key]) - 1] += 1
        return answer
