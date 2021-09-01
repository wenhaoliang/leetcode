"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树[1,2,2,3,4,4,3] 是对称的。
   1
 2   2
3 4 4 3
但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:
   1
 2    2
  3    3

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
"""
import collections
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
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        if not root:
            return True
        else:
            return dfs(root.left, root.right)


class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False

            return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

        if not root:
            return True
        return dfs(root.left, root.right)


if __name__ == "__main__":
    """
       1
     2   2
    3 4 4 3
    """

    n = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(4)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    PrintTree(n)

    A = Solution()
    print(A.isSymmetric(n))
    A = Solution1()
    print(A.isSymmetric(n))
