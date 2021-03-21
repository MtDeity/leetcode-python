import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            heapq.heappush(neg_stones, heapq.heappop(neg_stones) - heapq.heappop(neg_stones))
        return -neg_stones[0]
