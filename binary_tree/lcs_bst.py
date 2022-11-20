# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        # first number that is <= p and >= q or vice versa, or (p.val-root.val)*(q.val-root.val) <= 0
        # if (root.val <= p.val and root.val >= q.val) or (root.val >= p.val and root.val <= q.val): return root
        if (p.val - root.val) * (q.val - root.val) <= 0: return root

        if self.lowestCommonAncestor(root.left, p, q):
            return self.lowestCommonAncestor(root.left, p, q)

        if self.lowestCommonAncestor(root.right, p, q):
            return self.lowestCommonAncestor(root.right, p, q)

    ### even better to cut down half the tree (O(log N))
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        # first number that is <= p and >= q or vice versa, or (p.val-root.val)*(q.val-root.val) <= 0
        # if (root.val <= p.val and root.val >= q.val) or (root.val >= p.val and root.val <= q.val): return root
        if (p.val - root.val) * (q.val - root.val) <= 0: return root

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


# l1l1l1 = TreeNode(7)

# r1l1 = TreeNode(13)
# r1r1 = TreeNode(4)
# r1r1l1 = TreeNode(5)
# r1r1r1 = TreeNode(1)

r1l2 = TreeNode(7)
r1r2 = TreeNode(9)

r1 = TreeNode(8, left=r1l2, right=r1r2)

l1r2l3 = TreeNode(3)
l1r2r3 = TreeNode(5)
l1r2 = TreeNode(4, left=l1r2l3, right=l1r2r3)
l1l2 = TreeNode(0)

l1 = TreeNode(2, left=l1l2, right=l1r2)
root = TreeNode(6, left=l1, right=r1)

sol = Solution()
p = TreeNode(3)
q = TreeNode(5)

print(sol.lowestCommonAncestor(root, p=p, q=q).val)

#%%
list_ = [1, 2, 3]
print(list_.pop(0))
print(list_)