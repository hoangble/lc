# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return head is None
        
        if head is None:
            return False

        return self.contain(head, root)

    def contain(self, list_node, tree_node):
        if tree_node is None: return False 
        if self.dfs(list_node, tree_node): return True

        return self.contain(list_node, tree_node.left) or self.contain(list_node, tree_node.right) 

    def dfs(self, list_node, tree_node) -> bool:
        if list_node is None: return True
        if tree_node is None: return False
        if list_node.val != tree_node.val:
            return False
        return self.dfs(list_node.next, tree_node.left) or self.dfs(list_node.next, tree_node.right) 
        