class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = lr = 0
        for char in s:
            lr += 1 if char == "L" else -1
            if lr == 0:
                count += 1
        return count
