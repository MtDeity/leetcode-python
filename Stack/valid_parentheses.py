from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        brackets: List[str] = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in mapping:
                if not brackets or brackets.pop() != mapping[c]:
                    return False
            else:
                brackets.append(c)
        return not brackets
