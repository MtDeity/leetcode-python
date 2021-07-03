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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.helper(root, [])

    def helper(self, root: TreeNode, traversal: List[int]) -> List[int]:
        if root.left:
            self.helper(root.left, traversal)
        traversal.append(root.val)
        if root.right:
            self.helper(root.right, traversal)
        return traversal
