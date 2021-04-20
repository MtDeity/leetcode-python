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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        answer: List[int] = []
        if not root:
            return []
        answer.append(root.val)
        if root.left:
            answer += self.preorderTraversal(root.left)
        if root.right:
            answer += self.preorderTraversal(root.right)
        return answer
