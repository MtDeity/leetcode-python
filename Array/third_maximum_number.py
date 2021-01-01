class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        mx1 = mx2 = mx3 = float('-inf')
        for n in nums:
            if n == mx1 or n == mx2 or n == mx3:
                continue
            elif n > mx1:
                mx3 = mx2
                mx2 = mx1
                mx1 = n
            elif n > mx2:
                mx3 = mx2
                mx2 = n
            elif n > mx3:
                mx3 = n
        return mx3 if mx3 > float('-inf') else mx1
