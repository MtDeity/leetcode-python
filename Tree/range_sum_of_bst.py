from __future__ import annotations
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(
            self,
            root: Optional[TreeNode],
            low: int,
            high: int) -> int:
        if not root:
            return 0
        res = 0
        d: deque[Optional[TreeNode]] = deque([root])
        while d:
            node = d.popleft()
            if not node:
                continue
            if node.val < low:
                d.append(node.right)
            elif node.val > high:
                d.append(node.left)
            else:
                res += node.val
                d.append(node.left)
                d.append(node.right)
        return res
