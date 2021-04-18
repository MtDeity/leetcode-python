from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = paid = 0
        for cost in sorted(costs):
            if coins - paid < cost:
                break
            count += 1
            paid += cost
        return count
