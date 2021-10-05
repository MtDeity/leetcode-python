from collections import Counter
from heapq import nlargest


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums
        counter = Counter(nums)
        return nlargest(k, counter.keys(), key=lambda x: counter[x])
