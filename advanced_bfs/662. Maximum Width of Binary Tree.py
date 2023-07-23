from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    from collections import deque

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        # technically O(n) but tle
        # q = [root]

        # while q:
        #     ans = max(ans, len(q))
        #     # print()
        #     # print(q)
        #     next_lvl = []
        #     null_buffer = []

        #     for i, node in enumerate(q):
        #         if node:
        #             if node.left:
        #                 if null_buffer and next_lvl:
        #                     next_lvl.extend(null_buffer)
        #                 null_buffer = []

        #                 next_lvl.append(node.left)
        #             else:
        #                 null_buffer.append(node.left)

        #             if node.right:
        #                 if null_buffer and next_lvl:
        #                     next_lvl.extend(null_buffer)
        #                 null_buffer = []

        #                 next_lvl.append(node.right)
        #             else:
        #                 null_buffer.append(node.right)

        #         elif not node and next_lvl:
        #             null_buffer.append(node)
        #             null_buffer.append(node)
        #     q = next_lvl

        q = [(0, root)]
        while q:
            n = len(q)
            nodes = []
            for _ in range(n):
                idx, node = q.pop(0)
                nodes.append(idx)

                if node.left:
                    q.append((idx * 2 + 1, node.left))

                if node.right:
                    q.append((idx * 2 + 2, node.right))
            ans = max(ans, nodes[-1] - nodes[0] + 1)

        return ans
