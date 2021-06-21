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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid],
                        self.sortedArrayToBST(nums[:mid]),
                        self.sortedArrayToBST(nums[mid + 1:]))
        return node
