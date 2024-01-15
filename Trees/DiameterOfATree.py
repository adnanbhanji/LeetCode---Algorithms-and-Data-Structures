# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.calculate_height(root)
        return self.diameter


    def calculate_height(self, node):
        if not node:
            return 0
        
        left = self.calculate_height(node.left)
        right = self.calculate_height(node.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)
    
    
