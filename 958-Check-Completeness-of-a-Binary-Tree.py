# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        none_found = False
        q = deque([])

        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                none_found = True
            else:
                if none_found: return False
                q.append(node.left)
                q.append(node.right)
        return True
