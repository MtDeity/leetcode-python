from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional[TreeNode] = None,
            right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        nums: list[int] = []
        stack = [root]
        while stack:
            top = stack.pop()
            nums.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        diffs: set[int] = set()
        for num in nums:
            if num in diffs:
                return True
            diffs.add(k - num)
        return False
