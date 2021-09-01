"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树: root =[6,2,8,0,4,7,9,null,null,3,5]
         6
      2     8
    0  4  7  9
      3  5
示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
                 6
              2     8
            0  4  7  9
              3  5
        根据二叉搜索树的定义
        公共祖先只有以下情况:
            p、q分居root左右
            p或q为root
        """
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                break

        return root


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


if __name__ == "__main__":
    """
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    输出: 6 
    解释: 节点 2 和节点 8 的最近公共祖先是 6。
         6
      2     8
    0  4  7  9
      3  5
    """

    n = TreeNode(6)
    n1 = TreeNode(2)
    n2 = TreeNode(8)
    n3 = TreeNode(0)
    n4 = TreeNode(4)
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(3)
    n8 = TreeNode(5)
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
    PrintTree(A.lowestCommonAncestor(n, n1, n2))
    A = Solution1()
    PrintTree(A.lowestCommonAncestor(n, n1, n2))
