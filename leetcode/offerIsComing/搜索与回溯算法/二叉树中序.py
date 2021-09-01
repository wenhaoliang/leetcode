class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = list()
        inorder(root)
        return res


class Solution1:
    def inorderTraversal(self, root: TreeNode):
        res = list()
        if not root:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res


if __name__ == "__main__":
    """
              3
         9         20
    15       7
    [15, 9, 7, 3, 20]
    """

    n = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n3 = TreeNode(15)
    n4 = TreeNode(7)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    print('Solution:\n', Solution().inorderTraversal(n))
    print('Solution1:\n', Solution1().inorderTraversal(n))

