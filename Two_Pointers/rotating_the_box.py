from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        rotated = [[''] * m for _ in range(n)]
        for i in reversed(list(range(m))):
            row = '*'.join([''.join(sorted(list(part), reverse=True))
                            for part in ''.join(box[i]).split('*')])
            for j in range(n):
                rotated[j][i] = row[j]
        return rotated
