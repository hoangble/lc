from typing import Optional, 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = height(node.left) + height(node.right) + 2 #left sub tree + right subtree

        # base cases
        if not root:
            return -1

        return max(
            self.get_height(root.left) + self.get_height(root.right) + 2,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )

    def get_height(self, node) -> int:
        # base case:
        if not node:
            return -1

        return max(self.get_height(node.left), self.get_height(node.right)) + 1


    def diameter_binary_tree(root):
        def dfs(root):
            if not root:
                return 0, []
            left_height, left_path = dfs(root.left)
            right_height, right_path = dfs(root.right)
            current_path = left_path + [root.val] + right_path
            current_height = max(left_height, right_height) + 1
            if left_height + right_height + 1 > len(diameter_path[0]):
                diameter_path[0] = current_path
            if left_height >= right_height:
                return current_height, left_path + [root.val]
            else:
                return current_height, [root.val] + right_path
            
        if not root:
            return 0
        diameter_path = [[]]
        dfs(root)
        print(diameter_path[0])
        return len(diameter_path[0])- 1

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int, List[TreeNode]
        """
        self.ans = 0
        self.diameter_path = []

        def height(root):
            if not root:
                return 0, []
            
            left_height, left_path = height(root.left)
            right_height, right_path = height(root.right)
            
            # Calculate diameter at current node
            if left_height + right_height > self.ans:
                self.ans = left_height + right_height
                self.diameter_path = left_path + [root.val] + right_path
            
            # Return the height of the current node and the path for the height
            if left_height > right_height:
                return left_height + 1, left_path + [root.val]
            else:
                return right_height + 1, right_path + [root.val]
        
        height(root)
        return self.ans, self.diameter_path