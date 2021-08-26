# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        values = []
        while stack:
            current = stack.pop()
            if current:
                values.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
        return values
