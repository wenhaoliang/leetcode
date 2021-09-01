"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
"""
import sys


def PrintTree(root):
    if root is None:
        sys.stdout.write("{}")
        return
    sys.stdout.write("该树为{")
    v = [root]
    c = 0
    none = ""
    while c < len(v):
        if c == 0:
            sys.stdout.write("%d" % v[c].val)
            v.append(v[c].left)
            v.append(v[c].right)
        else:
            if v[c] is None:
                none = none + ",#"
            else:
                sys.stdout.write("%s,%d" % (none, v[c].val))
                none = ""
                v.append(v[c].left)
                v.append(v[c].right)
        c = c + 1
    sys.stdout.write("}")
    print()


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            return max(left, right) + 1

        return dfs(root)


class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            return max(left, right) + 1

        return dfs(root)


if __name__ == "__main__":
    """
         4
      2     7
    1  3  6  9
    """

    n = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(7)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(6)
    n6 = TreeNode(9)
    n.left = n1
    n.right = n2
    # n1.left = n3
    # n1.right = n4
    # n2.left = n5
    # n2.right = n6

    PrintTree(n)

    A = Solution()
    print(A.maxDepth(n))
    A = Solution1()
    print(A.maxDepth(n))
