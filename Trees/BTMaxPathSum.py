# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxpath = float(-inf)
        self.dfs(root)
        return self.maxpath

    def dfs(self, node):
        if not node:
            return 0
        
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))

        self.maxpath = max(self.maxpath, left + right + node.val)

        return node.val + max(left, right)