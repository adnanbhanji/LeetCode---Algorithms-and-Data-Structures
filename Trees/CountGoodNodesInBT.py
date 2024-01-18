# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0
        self.check(root, float(-inf))
        return self.counter
    
    def check(self, node, max_val):
        if not node:
            return 0
        
        if node.val >= max_val:
            self.counter += 1
        
        max_val = max(max_val, node.val)

        left = self.check(node.left, max_val)
        right = self.check(node.right, max_val)

