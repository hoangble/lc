# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/submissions/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = []
        ans = []
        current_sum = 0

        def dfs(node, stack, current_sum, ans):
            if not node:
                return
            stack.append(node.val)
            if not node.left and not node.right and current_sum + node.val == targetSum:
                ans.append(stack.copy())
            dfs(node.left, stack, current_sum + node.val, ans)
            dfs(node.right, stack, current_sum + node.val, ans)
            stack.pop()

        dfs(root, stack, current_sum, ans)
        return ans
