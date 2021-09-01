# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return int整型二维数组
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(tmp)
        return res


class Solution1:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        tmp = [root]

        while len(tmp) > 0:
            temp = []
            res = []
            for i in tmp:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                res.append(i.val)
            tmp = temp
            result.append(res)
        return result


if __name__ == "__main__":
    n = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(6)
    n4 = TreeNode(7)
    n5 = TreeNode(4)
    n6 = TreeNode(5)
    n.left = n1
    n.right = n2
    n1.left = n5
    n1.right = n6
    n2.left = n3
    n2.right = n4

    solution = Solution1()
    print(solution.levelOrder(n))
