class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left, right = (
            self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right)
        )
        return root if left and right else left or right


class Solution:
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        # self.contain_p_or_q(root, p , q)
        # if root == p or root == q: return root
        self.contain_p_or_q(root, p, q)
        return self.lca

    def contain_p_or_q(self, node, p, q):
        if not node:
            return False
        is_left = self.contain_p_or_q(node.left, p, q)
        is_right = self.contain_p_or_q(node.right, p, q)

        if node == p or node == q:
            if is_left or is_right:
                self.lca = node
            return True

        if is_left and is_right:
            self.lca = node
            # return True

        return is_left or is_right
