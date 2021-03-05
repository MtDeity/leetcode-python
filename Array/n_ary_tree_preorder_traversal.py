class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # return sum(sorted(nums)[::2])
        limit = 10000
        counter = [0] * (limit * 2 + 1)
        for num in nums:
            counter[num + limit] += 1
        total = d = 0
        for i in range(len(counter)):
            total += (counter[i] - d + 1) // 2 * (i - limit)
            d = (counter[i] + d) % 2
        return total
