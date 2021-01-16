class Solution:
    def maxDepth(self, s: str) -> int:
        max_vps = current_vps = 0
        for char in s:
            if char == "(":
                current_vps += 1
                max_vps = max(max_vps, current_vps)
            elif char == ")":
                current_vps -= 1
        return max_vps
