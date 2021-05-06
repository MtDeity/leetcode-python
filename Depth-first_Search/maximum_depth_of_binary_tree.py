from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if not root:
            return depth
        return max(
            self.maxDepth(root.left, depth + 1),
            self.maxDepth(root.right, depth + 1))
