# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.check_balance(root)
        return self.diameter


    def check_balance(self, node):
        if not node:
            return 0
        
        left = self.check_balance(node.left)
        right = self.check_balance(node.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)
    
    
