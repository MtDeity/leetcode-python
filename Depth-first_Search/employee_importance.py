from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        e_map = {employee.id: employee for employee in employees}
        importance = 0
        stack = [id]
        while stack:
            employee = e_map[stack.pop()]
            importance += employee.importance
            stack += employee.subordinates
        return importance

        # def dfs(id: int):
        #     employee = e_map[id]
        #     importance = employee.importance
        #     for sub_id in employee.subordinates:
        #         importance += dfs(sub_id)
        #     return importance
        # return dfs(id)
