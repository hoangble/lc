# https://leetcode.com/problems/path-sum-ii/submissions/
# 113. Path Sum II

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


[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
22

l1 = TreeNode(4)
l1l1 = TreeNode(11)
l1l1l1 = TreeNode(7)
l1l1r1 = TreeNode(2)

r1 = TreeNode(8)
r1l1 = TreeNode(13)
r1r1 = TreeNode(4)
r1r1l1 = TreeNode(5)
r1r1r1 = TreeNode(1)

root = TreeNode(5, left=l1, right=r1)

# r1 = TreeNode(8)

# root = TreeNode(5, right=right)

sol = Solution()
print(sol.pathSum(root, -5))
