"""
给定一棵二叉搜索树，请找出其中第k大的节点。
示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
  2
输出: 4
示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
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
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        二叉搜索树，中序遍历为递增，则中序倒序为递减。
        """

        def dfs(node):
            if not node:
                return
            dfs(node.right)

            self.k -= 1
            if self.k == 0:
                self.res = node.val
            dfs(node.left)

        self.k = k
        dfs(root)
        return self.res


class Solution1:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node:
                return

            dfs(node.right)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            dfs(node.left)


        self.k = k
        dfs(root)
        return self.res


if __name__ == "__main__":
    """
                  4
             2         5
        1       3
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
    k = 2
    A = Solution()
    print(A.kthLargest(n, k))
    A = Solution1()
    print(A.kthLargest(n, k))
