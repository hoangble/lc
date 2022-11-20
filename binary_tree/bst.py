class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        # if root.left is not None and root.right is not None:
        return self.isSymmetric_(root.left, root.right)
        # else:
            # return False
    
    def isSymmetric_(self, left, right):
        if left is None and right is None:
            return True
            
        if left is None or right is None:
            return False
        
        if left.val != right.val:
            return False
        
        return self.isSymmetric_(left.left, right.right) and self.isSymmetric_(left.right, right.left)