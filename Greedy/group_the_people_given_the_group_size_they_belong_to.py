from typing import List, Dict
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups: Dict[int, List[int]] = defaultdict(list)
        res: List[List[int]] = []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if size == len(groups[size]):
                res.append(groups.pop(size))
        return res
