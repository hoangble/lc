# 98. Validate Binary Search Tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_ = float("inf")
        min_ = -float("inf")

        return self.isValidBSTwithrange(root, min_, max_)

    def isValidBSTwithrange(self, root, min_, max_):
        if root is None:
            return True

        # find a new range
        if root.val < min_ or root.val > max_:
            return False
        else:
            return self.isValidBSTwithrange(
                root.left, min_, root.val - 1
            ) and self.isValidBSTwithrange(root.right, root.val + 1, max_)
        # false if out of range
