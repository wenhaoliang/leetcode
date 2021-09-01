"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
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
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:
                return -1
            right = recur(root.right)
            if right == -1:
                return -1

            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return -1

        return recur(root) != -1


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                return -1

        return dfs(root) != -1


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
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6

    PrintTree(n)

    A = Solution()
    print(A.isBalanced(n1))
    A = Solution1()
    print(A.isBalanced(n1))
