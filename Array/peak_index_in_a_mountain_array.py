class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        idx = mx = 0
        for i, num in enumerate(arr):
            if num > mx:
                mx = num
                idx = i
        return idx
