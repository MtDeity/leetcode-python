from typing import List


class Solution:
    def makeFancyString(self, s: str) -> str:
        fancy: List[str] = []
        for c in s:
            if len(fancy) > 1 and c == fancy[-1] == fancy[-2]:
                continue
            fancy.append(c)
        return ''.join(fancy)
