from typing import Set


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        seen: Set[str] = set()
        longest, left = 0, -1
        for right, c in enumerate(word):
            if right > 0 and c < word[right - 1]:
                seen = set()
                left = right - 1
            seen.add(c)
            if len(seen) == 5:
                longest = max(longest, right - left)
        return longest
