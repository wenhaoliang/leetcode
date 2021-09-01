"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
示例:
给定如下二叉树，以及目标和target = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
"""
import sys
from typing import List


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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        深度优先搜索： 可以理解为暴力法遍历矩阵中所有字符串可能性。DFS通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推。
        剪枝： 在搜索中，遇到这条路不可能和目标字符串匹配成功 的情况，则应立即返回，称之为 可行性剪枝 。

        对二叉树节点进行left, right搜索

        1、递归参数：二叉树节点
        2、终止条件：
            此次搜索节点和等于target 以及 node.left node.right 为空
            并将path数组保存至res数组中
        3、递推工作：
            1、将当前node.val保存至path数组
            2、target = target - node.val
            3、recur(node.left, target) recur(node.right, target)
            4、将当前node.val从path数组中删除
        4、回溯返回值：res

        值得注意的是，记录路径时若直接执行 res.append(path) ，
        则是将 path 对象加入了 res ；后续 path 改变时，
        res 中的 path 对象也会随之改变。
        正确做法：res.append(list(path)) ，相当于复制了一个 path 并加入到 res 。
        """
        path, res = [], []

        def recur(node, target):
            if node is None:
                return
            path.append(node.val)
            target -= node.val
            if target == 0 and node.left is None and node.right is None:
                res.append(list(path))
            recur(node.left, target)
            recur(node.right, target)
            path.pop()

        recur(root, sum)
        return res


class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, target):
            if not node:
                return
            path.append(node.val)
            target = target - node.val

            if target == 0 and not node.left and not  node.right:
                res.append(list(path))

            dfs(node.left, target)
            dfs(node.right, target)
            path.pop()

        res = []
        if not root:
            return res
        path = []
        dfs(root, sum)
        return res


if __name__ == "__main__":
    """
                  3
             9         20
        15       7
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
    target = 23
    A = Solution()
    print(A.pathSum(n, target))
    A = Solution1()
    print(A.pathSum(n, target))
