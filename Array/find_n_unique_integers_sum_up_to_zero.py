class Solution:
    def sumZero(self, n: int) -> List[int]:
        # nums = [0] * n
        # for i in range(n // 2):
        #     nums[i * 2] = i + 1
        #     nums[i * 2 + 1] = - (i + 1)
        # return nums
        return range(1 - n, n, 2)
