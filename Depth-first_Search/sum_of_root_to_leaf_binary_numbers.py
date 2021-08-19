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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total = 0
        stack: list[tuple[TreeNode, int]] = [(root, total)]
        while stack:
            top, sub_total = stack.pop()
            sub_total = sub_total << 1 | top.val
            if top.left:
                stack.append((top.left, sub_total))
            if top.right:
                stack.append((top.right, sub_total))
            if not top.left and not top.right:
                total += sub_total
        return total
