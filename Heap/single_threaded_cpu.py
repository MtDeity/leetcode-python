from typing import List, Tuple
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order: List[int] = []
        available: List[Tuple[int, int]] = []
        tasks_: List[Tuple[int, int, int]] = sorted(
            [(task[0], task[1], index) for index, task in enumerate(tasks)])
        i = time = 0
        while available or i < len(tasks_):
            while i < len(tasks_) and tasks_[i][0] <= time:
                heapq.heappush(available, (tasks_[i][1], tasks_[i][2]))
                i += 1
            if available:
                processing, index = heapq.heappop(available)
                order.append(index)
                time += processing
            elif i < len(tasks_):
                time = tasks_[i][0]
        return order
