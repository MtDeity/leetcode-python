from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(
            self, val: Optional[int] = None,
            children: Optional[List[Node]] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(child) for child in root.children) + 1
