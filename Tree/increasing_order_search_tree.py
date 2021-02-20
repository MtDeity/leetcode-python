# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root: TreeNode):
            if not root:
                return
            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)

        answer = current = TreeNode()
        for val in inorder(root):
            current.right = TreeNode(val)
            current = current.right
        return answer.right
