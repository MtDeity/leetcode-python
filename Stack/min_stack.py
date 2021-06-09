from typing import List


class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.min: List[int] = []

    def push(self, val: int) -> None:
        self.stack += [val]
        if not self.min or val <= self.min[-1]:
            self.min += [val]

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min = self.min[:-1]
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
