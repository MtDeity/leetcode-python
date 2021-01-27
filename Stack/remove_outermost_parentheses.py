class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        removed = []
        opened = 0
        for c in S:
            if c == "(" and opened > 0:
                removed.append(c)
            elif c == ")" and opened > 1:
                removed.append(c)
            opened += 1 if c == "(" else -1
        return "".join(removed)
