from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode], nodes: int = 0) -> int:
        if not root:
            return nodes
        return self.countNodes(root.left, nodes) + self.countNodes(root.right, nodes) + 1
    # def countNodes(self, root: Optional[TreeNode]) -> int:
        # stack = [root]
        # cnt = 0
        # while stack:
        #     cur = stack.pop()
        #     if cur:
        #         cnt += 1
        #         stack.append(cur.left)
        #         stack.append(cur.right)
        # return cnt
