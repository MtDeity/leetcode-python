class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        mx = cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                mx = max(mx, cnt)
                cnt = 0
        return max(mx, cnt)
