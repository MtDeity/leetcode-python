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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right \
            = self.invertTree(root.right), self.invertTree(root.left)
        return root
