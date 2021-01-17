# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # Recursive
        if not root:
            return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

        # # Iterative
        # total = 0
        # stack = [root]
        # while stack:
        #     top = stack.pop()
        #     if not top:
        #         continue
        #     elif top.val < low:
        #         stack.append(top.right)
        #     elif top.val > high:
        #         stack.append(top.left)
        #     else:
        #         total += top.val
        #         stack.append(top.left)
        #         stack.append(top.right)
        # return total
