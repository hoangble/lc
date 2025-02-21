# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        st = [root]
        for i in range(1, len(preorder)):
            node, child = st[-1], TreeNode(preorder[i])
            while st and st[-1].val < preorder[i]:
                node = st.pop()
            
            if node.val < preorder[i]:
                node.right = child
            else:
                node.left = child
            st.append(child)
        return root