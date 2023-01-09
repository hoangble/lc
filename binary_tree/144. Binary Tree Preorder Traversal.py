class Solution:
    # def __init__(self):
    #     self.ans = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        # self.ans.append(root.val)
        # self.preorderTraversal(root.left)
        # self.preorderTraversal(root.right)
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
