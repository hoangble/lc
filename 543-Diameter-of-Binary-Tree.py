# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        self.path = []
        self.dfs(root)
        return self.dia
    
    def dfs(self, node) -> Tuple[int, List[TreeNode]]:
        if not node: 
            return 0, [None]

        left_dia, left_dia_path = self.dfs(node.left)
        right_dia, right_dia_path = self.dfs(node.right)

        if left_dia + right_dia > self.dia:
            self.dia = left_dia + right_dia
            self.path = left_dia_path + [node] +right_dia_path
        # self.dia = max(self.dia, left_dia + right_dia)

        if left_dia > right_dia:
            return left_dia + 1, left_dia_path + [node]
        else:
            return right_dia + 1, right_dia_path + [node]

        # return max(left_dia, right_dia) + 1
