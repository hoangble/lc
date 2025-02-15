# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ans = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # bfs
        # if root is None:
        #     return 0
        
        # curr = [root]
        # ans = 0

        # while curr:
        #     next_ = []
        #     for node in curr:
        #         if node is None:
        #             continue
        #         if low <= node.val <= high:
        #             ans += node.val
                
        #         if node.val > low and node.left:
        #             next_.append(node.left)
        #         if node.val < high and node.right:
        #             next_.append(node.right)
        #     curr = next_
        # return ans

        # dfs
        ans = 0
        ans = self.dfs(root, low, high, ans)
        return ans

    def dfs(self, node, low, high, ans) -> int:
        if node is None:
            return 0
        ans = 0
        if low <= node.val <= high:
            ans += node.val

        if node.val > low and node.left is not None:
            ans += self.dfs(node.left, low, high, ans)
        if node.val < high and node.right is not None:
            ans += self.dfs(node.right, low, high, ans)
        return ans
        
