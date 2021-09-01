"""
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
示例 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        前序遍历划分 [ 3 | 9 | 20 15 7 ]
        中序遍历划分 [ 9 | 3 | 15 20 7 ]
                       3
                    9    20
                       15   7
        """

        # root：根节点索引
        # left：中序遍历左边界
        # right 中序遍历右边界
        def recur(root, left, right):
            if left > right:
                return
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]
            # 左子树根节点 =当前根节点
            # 左边界 = 当前的左边界
            # 右边界 = 根据前序遍历找到的中序根节点坐标 - 1
            node.left = recur(root + 1, left, i - 1)
            # 右子树根节点 = （根据前序遍历找到的中序根节点坐标 - 中序左边界） + 前序根节点坐标 + 1
            # 括号里与左子树长度等价 ||
            # +1： 这里的+1表示去掉左子树长度，再去掉根节点，剩下的为右子树，而+1为在前序中的右子树根节点
            # 左边界 = 根据前序遍历找到的中序根节点坐标 + 1 表示 中序遍历左边界
            # 右边界 =  中序遍历右边界
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)


class Solution1:
    """
    前序遍历划分 [ 3 | 9 | 20 15 7 ]
    中序遍历划分 [ 9 | 3 | 15 20 7 ]
                   3
                9    20
                   15   7
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]
            # 根节点、左、右 =
            node.left = recur(root + 1, left, i - 1)
            # 根节点、左、右 =
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        dic = {}
        n = len(inorder)
        for i in range(n):
            dic[inorder[i]] = i
        return recur(0, 0, n - 1)


if __name__ == "__main__":
    """
        3
      9   20
        15   7 
    Input: 
        preorder = [3,9,20,15,7], 
        inorder = [9,3,15,20,7]
    Output: 
        [3,9,20,null,null,15,7]
    """
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    A = Solution()
    PrintTree(A.buildTree(preorder, inorder))
