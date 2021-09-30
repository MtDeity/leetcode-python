class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(1 if o[1] == '+' else -1 for o in operations)
