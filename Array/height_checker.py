class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        srtd = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != srtd[i]:
                cnt += 1
        return cnt
