class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        lgth = len(arr)
        # for i in range(1, lgth + 1, 2):
        #     for j in range(lgth + 1 - i):
        #         total += sum(arr[j: j + i])
        for i in range(lgth):
            freq = (((lgth - i) * (i + 1) + 1)) // 2
            total += freq * arr[i]
        return total
