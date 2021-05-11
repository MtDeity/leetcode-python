from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        mx = cur = sum(cardPoints[:k])
        for i in range(1, k + 1):
            cur += cardPoints[-i] - cardPoints[k - i]
            mx = max(mx, cur)
        return mx
