# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        final = []
        queue = deque()
        queue.append(root)
    
        while queue:
            length_level = len(queue)
            level_arr = []

            for i in range(length_level):
                temp = queue.popleft()
                level_arr.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            final.append(level_arr)

        return final 
