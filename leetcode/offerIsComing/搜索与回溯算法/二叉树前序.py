class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode):
        def preorder(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)
        return res


class Solution1:
    def preorderTraversal(self, root: TreeNode):
        def preOrder(root):
            if not root:
                return
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)

        res = list()
        preOrder(root)
        return res


if __name__ == "__main__":
    """
                  4
             2         5
        1       3
        [4, 2, 1, 3, 5]
    """

    n = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    print('Solution:\n', Solution().preorderTraversal(n))
    print('Solution1:\n', Solution1().preorderTraversal(n))
