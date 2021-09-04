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
    def isUnivalTree(
            self,
            root: Optional[TreeNode],
            num: int = -1) -> bool:
        if not root:
            return True
        if num < 0:
            num = root.val
        if root.val != num:
            return False
        left = self.isUnivalTree(root.left, num)
        right = self.isUnivalTree(root.right, num)
        return left and right
