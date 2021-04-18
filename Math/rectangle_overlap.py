from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left1, bottom1, right1, top1 = rec1
        left2, bottom2, right2, top2 = rec2
        if (left1 == right1
                or bottom1 == top1
                or left2 == right2
                or bottom2 == top2):
            return False
        return not (right1 <= left2
                    or top1 <= bottom2
                    or left1 >= right2
                    or bottom1 >= top2)
