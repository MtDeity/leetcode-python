class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        prev = ord('a')
        for c in word:
            diff = max(ord(c) - prev, prev - ord(c))
            time += 1 + min(diff, 26 - diff)
            prev = ord(c)
        return time
