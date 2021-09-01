"""
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
给定的二叉树是{3,9,20,#,#,15,7},
          3
    9         20
 8    10   15     7
该二叉树之字形层序遍历的结果是
[[3],[20,9],[15,7]]
示例1: {1,#,2} 返回值：[[1],[2]]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        # write code here
        if root is None:
            return []
        result = []
        tmp = [root]
        flag = False
        while len(tmp) > 0:
            temp = []
            res = []
            for i in tmp:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                if not flag:
                    res.append(i.val)
                else:
                    res.insert(0, i.val)
            tmp = temp
            flag = not flag
            result.append(res)
        return result


class Solution1:
    def zigzagLevelOrder(self, root):
        # write code here
        if not root:
            return []

        tmp = [root]
        result = []
        flag = False

        while len(tmp) > 0:
            temp = []
            res = []
            for i in tmp:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                if flag:
                    res.append(i.val)
                else:
                    res.insert(0, i.val)
            flag = not flag
            tmp = temp
            result.append(res)

        return result


if __name__ == "__main__":
    """
              3
        9         20
     8    10   15     7
    """
    n = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n3 = TreeNode(8)
    n4 = TreeNode(10)
    n5 = TreeNode(15)
    n6 = TreeNode(7)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6

    solution = Solution()
    print(solution.zigzagLevelOrder(n))
