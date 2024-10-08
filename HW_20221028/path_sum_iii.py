# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from collections import defaultdict

    def __init__(self):
        self.ans = 0

    """
    O(n^2) as each node is visited twice. O(1) space
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.dfs(root, targetSum)

        return self.ans

    def dfs(self, node, target):
        if not node:
            return

        self.check_reach_target(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def check_reach_target(self, node, target) -> None:
        if not node:
            return

        self.ans += int(node.val == target)
        self.check_reach_target(node.left, target - node.val)
        self.check_reach_target(node.right, target - node.val)

    """
    O(n) as we save all the calculation from the root to the leaf in a cache. O(n) space
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.cache = defaultdict(int)
        self.currSum = 0
        self.dfs(root, targetSum, currSum)

        return self.ans

    def dfs(self, node, target, currSum):
        if not node:
            return None
        currSum += node.val
        self.ans += int(currSum == target)
        self.ans += self.cache[currSum - target]

        self.cache[currSum] += 1
        self.dfs(node.left, target, currSum)
        self.dfs(node.right, target, currSum)
        self.cache[currSum] -= 1
