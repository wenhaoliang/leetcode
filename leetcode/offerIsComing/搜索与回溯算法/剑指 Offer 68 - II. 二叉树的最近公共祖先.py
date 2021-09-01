"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树: root =[3,5,1,6,2,0,8,null,null,7,4]

         3
      5     1
    6  2  0  8
      7  4
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        采用先序遍历，若当前节点不存在或当前节点为p、q时返回当前节点

        当left,right都为空时返回空
        当left为空时，表示p,q都在右边，返回right
        当right为空时，表示p,q都在左边，返回left
        否则表示left, right分局root两侧，返回root
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        return root


class Solution1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not right and not left:
            return
        if not left:
            return right
        if not right:
            return left
        return root


if __name__ == "__main__":
    """
         3
      5     1
    6  2  0  8
      7  4
    """

    n = TreeNode(3)
    n1 = TreeNode(5)
    n2 = TreeNode(1)
    n3 = TreeNode(6)
    n4 = TreeNode(2)
    n5 = TreeNode(0)
    n6 = TreeNode(8)
    n7 = TreeNode(7)
    n8 = TreeNode(4)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    n4.left = n7
    n4.right = n8

    PrintTree(n)

    A = Solution()
    PrintTree(A.lowestCommonAncestor(n, n4, n7))
    A = Solution1()
    PrintTree(A.lowestCommonAncestor(n, n4, n7))
