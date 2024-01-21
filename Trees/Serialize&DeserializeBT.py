# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        return f"{root.val},{left},{right}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        token = data.split(',')
        return self.main_deserialize(token)

    def main_deserialize(self, token):
        if not token:
            return None
        
        node = token.pop(0)
        if node == "#":
            return None
        
        node = TreeNode(int(node))
        node.left = self.main_deserialize(token)
        node.right = self.main_deserialize(token)

        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))