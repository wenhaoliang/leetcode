"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
例如:
给定二叉树:[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
"""
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        deque = collections.deque()
        deque.append(root)

        while deque:
            tmp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                tmp.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(tmp)
        return res


class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        deque = collections.deque()
        deque.append(root)

        while deque:
            temp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                temp.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(temp)

        return res


if __name__ == "__main__":
    """
                  3
             9         20
        15       7
        [15, 9, 7, 3, 20]
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
    A = Solution()
    print(A.levelOrder(n))
    A = Solution1()
    print(A.levelOrder(n))
