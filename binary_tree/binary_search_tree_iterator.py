from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.i = -1
        self.arr = []
        self.traverse(root)
        print(self.arr)

    # Change the traversal order for different types of traversal
    # if postorder: traverse(left), traverse(right), node
    # if preorder: node, traverse(left), traverse(right)

    # if need for less space intensive, eg, streaming
    # do a left ony recursive traversal
    def traverse(self, node):
        # O(n)
        # in-order
        if not node:
            return

        self.traverse(node.left)
        self.arr.append(node.val)
        self.traverse(node.right)

    def next(self) -> int:
        # O(1)
        self.i += 1
        return self.arr[self.i]

        # O(1)

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.arr)


class BSTIteratorStreaming:
    def __init__(self, root: Optional[TreeNode]):
        self.i = -1
        self.stack = []
        self.left_traverse(root)

    def left_traverse(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        stack_top = self.stack.pop()

        if stack_top.right is not None:
            self.left_traverse(stack_top.right)
        return stack_top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class BSTIteratorPostOrder:
    def __init__(self, root: Optional[TreeNode]):
        self.i = -1
        self.stack = []
        self.post_order_traverse(root)

    def post_order_traverse(self, node):
        if not node:
            return

        self.post_order_traverse(node.left)
        self.post_order_traverse(node.right)
        self.stack.append(node.val)

    def next(self) -> int:
        self.i += 1
        return self.stack[self.i]

    def hasNext(self) -> bool:
        return self.i < len(self.stack)


class BSTIteratorPostOrderStreaming:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.last_visited = None
        self.left_traverse(root)

    def left_traverse(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        while self.stack:
            curr_node = self.stack[-1]

            # If there is no right child or it has already been visited, pop the current node
            if curr_node.right is None or curr_node.right == self.last_visited:
                self.last_visited = self.stack.pop()
                return self.last_visited.val

            self.left_traverse(curr_node.right)
        return None

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class BSTIteratorPostOrderConstantNext:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.last_visited = None
        self.left_traverse(root)

    def left_traverse(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Must be O(1) avg???
        res = self.stack.pop()
        self.left_traverse(res.right)
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

class BSTIteratorPostOrderModifyTree:
    # turn into a doubly linked list
    def __init__(self):
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15, TreeNode(9), TreeNode(20))

    non_stream = BSTIteratorPostOrder(root)
    print(non_stream.stack)

    obj = BSTIteratorPostOrderStreaming(root)
    param_1 = obj.next()
    param_2 = obj.next()
    param_3 = obj.hasNext()
    param_4 = obj.next()
    param_5 = obj.hasNext()
    param_6 = obj.next()
    param_7 = obj.hasNext()
    param_8 = obj.next()
    param_9 = obj.hasNext()
