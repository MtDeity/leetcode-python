from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        left = 0
        mx = right = 1
        seen: dict[str, int] = defaultdict(int)
        seen[s[left]] += 1
        while right < n:
            seen[s[right]] += 1
            while seen[s[right]] >= 2:
                seen[s[left]] -= 1
                left += 1
            right += 1
            mx = max(mx, right - left)
        return mx
