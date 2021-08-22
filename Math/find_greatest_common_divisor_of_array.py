class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        while mn:
            mn, mx = mx % mn, mn
        return mx
