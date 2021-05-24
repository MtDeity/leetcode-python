class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join([chr(ord(c) + ord('a') - ord('A'))
                       if ord('A') <= ord(c) <= ord('Z') else c for c in s])
