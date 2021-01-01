class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
            # digit = 0
            # while num // 10 > 0:
            #     digit += 1
            #     num //= 10
            # if (digit + 1) % 2 == 0:
            #     count += 1
        return count
