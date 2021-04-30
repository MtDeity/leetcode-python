from typing import List, Set


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        nums: Set[int] = set()
        i = j = 1
        while i < bound:
            while i + j <= bound:
                nums.add(i + j)
                j *= y
                if y == 1:
                    break
            i *= x
            j = 1
            if x == 1:
                break
        return list(nums)
