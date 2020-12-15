class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in mapping:
                if not brackets or mapping[c] != brackets.pop():
                    return False
            else:
                brackets.append(c)
        return not brackets
