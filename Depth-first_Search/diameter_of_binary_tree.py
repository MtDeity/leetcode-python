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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = get_height(node.left)
            right = get_height(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        get_height(root)
        return self.ans
