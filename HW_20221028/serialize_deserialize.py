# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        """
        do a preorder dfs to have the string stored
        """
        self.preorder = []        
        def dfs_preorder(node):
            if not node: 
                self.preorder.append("null")
            else:
                self.preorder.append(str(node.val))
                dfs_preorder(node.left)
                dfs_preorder(node.right)
        dfs_preorder(root)
        ans = ",".join(self.preorder)
        return ans
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        preorder = [int(float(x)) if x != "null" else "null" for x in data.split(",")]
        print(preorder)
        
        def buildtree():
            val = preorder.pop(0)
            if val == "null": 
                return None
            node = TreeNode(val=val)
            node.left = buildtree()
            node.right = buildtree()
            return node
        
        root = buildtree()
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))