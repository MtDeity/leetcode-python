from __future__ import annotations
from typing import Optional, Union


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self,
                   root: Optional[TreeNode],
                   low: Union[int, float] = float('-inf'),
                   high: Union[int, float] = float('inf')) -> bool:
        if not root:
            return True
        elif root.val <= low or root.val >= high:
            return False
        else:
            return self.isValidBST(root.left, low, root.val)\
                and self.isValidBST(root.right, root.val, high)
