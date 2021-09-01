class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        def inorder(root: TreeNode):
            if not root:
                return
            inorder(root.left)
            inorder(root.right)
            res.append(root.val)

        res = list()
        inorder(root)
        return res


class Solution1:
    def postorderTraversal(self, root: TreeNode):
        res = []
        if not root:
            return res

        stack = []
        prev = None
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right

        return res




if __name__ == "__main__":
    """
                  4
             2         5
        1       3   6     7
        [1, 3, 2, 6, 7, 5, 4]
    """

    n = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(6)
    n6 = TreeNode(7)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    solution = Solution1()
    print(solution.postorderTraversal(n))
