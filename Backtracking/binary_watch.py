from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times: List[str] = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    times.append(f'{h}:{m:02}')
        return times
