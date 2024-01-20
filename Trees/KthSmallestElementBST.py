# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.k = k
        self.check(root)
        return self.result
    
    def check(self, node):
        if not node:
            return 
        
        left = self.check(node.left)
        
        self.k-=1
        if self.k == 0:
            self.result = node.val
            return

        right = self.check(node.right)
