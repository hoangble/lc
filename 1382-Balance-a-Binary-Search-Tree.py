# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        arr = []
        self.inorder(root, arr)
        root = self.construct(arr, 0, len(arr) - 1)
        return root
    
    def inorder(self, root, arr):
        if not root:
            return
        
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    
    def construct(self, arr, start, end) -> TreeNode:
        if start > end:
            return
        
        mid = (start + end) // 2
        l = self.construct(arr, start, mid - 1)
        r = self.construct(arr, mid + 1, end)
        node = TreeNode(arr[mid], l, r)
        return node

        