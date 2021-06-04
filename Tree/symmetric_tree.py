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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)
        # if not root or root.left and root.right:
        #     return True
        # elif not root.left or not root.right:
        #     return False
        # lefts: List[Optional[TreeNode]] = [root.left]
        # rights: List[Optional[TreeNode]] = [root.right]
        # while lefts or rights:
        #     if not lefts or not rights:
        #         return False
        #     left = lefts.pop()
        #     right = rights.pop()
        #     if not left and not right:
        #         continue
        #     elif (not left or not right) or left.val != right.val:
        #         return False
        #     lefts.append(left.left)
        #     lefts.append(left.right)
        #     rights.append(right.right)
        #     rights.append(right.left)
        # return True

    def is_mirror(
            self,
            t1: Optional[TreeNode],
            t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        return t1.val == t2.val \
            and self.is_mirror(t1.left, t2.right) \
            and self.is_mirror(t1.right, t2.left)
