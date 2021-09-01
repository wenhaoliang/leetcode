"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false
示例 2：
输入: [1,3,2,6,5]
输出: true
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
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
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        首先划分树为根节点，左子树，右子树
        (left,right)：left为左边界 right为右边界
        后序遍历最后一个节点为根节点，即j为根节点
        在二叉搜索树中，从左到右遍历，第一个比根节点大的树为右子树的首位节点设为[m]
        那么左子树区间为： [left, m-1]
        右子树区间为:     [m, right-1]

        如何确认该树是不是二叉搜索树呢？
            1、由于第一步已经确认了左子树区间[left, m-1]中所有元素都小于根节点，所以只需判断右子树即可
            2、右子树： 遍历右子树区间[m,right-1]看其中数值是否比根节点大，若都大则表明是符合的，
        """

        def recur(left, right):
            if left >= right:
                return True

            p = left
            while postorder[p] < postorder[right]:
                p += 1
            m = p
            while postorder[p] > postorder[right]:
                p += 1
            return p == right and recur(left, m - 1) and recur(m, right - 1)

        return recur(0, len(postorder) - 1)


class Solution1:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(left, right):
            if left >= right:
                return True

            p = left

            while postorder[p] < postorder[right]:
                p += 1
            m = p

            while postorder[p] > postorder[right]:
                p += 1

            return p == right and recur(left, m - 1) and recur(m, right - 1)

        return recur(0, len(postorder) - 1)


if __name__ == "__main__":
    """
    输入: [1,3,2,6,5]
    输出: false
    """

    A = Solution()
    print(A.verifyPostorder([1, 3, 2, 6, 5]))
    A = Solution1()
    print(A.verifyPostorder([1, 3, 2, 6, 5]))
