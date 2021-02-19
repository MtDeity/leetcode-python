class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        sum_map = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            sum_i = 0
            while i > 0:
                sum_i += i % 10
                i //= 10
            sum_map[sum_i] += 1
        return max(sum_map.values())
