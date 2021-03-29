class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        stack = [root]
        i = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != voyage[i]:
                return [-1]
            i += 1
            if node.right and node.right.val == voyage[i]:
                if node.left:
                    res.append(node.val)
                stack.extend([node.left, node.right])
            else:
                stack.extend([node.right, node.left])
        return res
