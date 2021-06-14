from __future__ import annotations
from typing import List, Optional


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        tree = [[root]]
        while True:
            level: List[TreeNode] = []
            for node in tree[-1]:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if not level:
                break
            tree.append(level)
        return [[node.val for node in level] for level in tree]
