"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
例如:
给定二叉树:[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回：
[3,9,20,15,7]

链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
"""
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        deque = collections.deque()
        deque.append(root)

        while deque:
            node = deque.popleft()
            res.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)

        return res


class Solution1:
    def levelOrder(self, root: TreeNode) -> List[int]:
        deque = collections.deque()
        deque.append(root)
        res = []
        while deque:
            node = deque.popleft()
            res.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)

        return res


if __name__ == "__main__":
    """
                  3
             9         20
        15       7
        [3, 9, 20, 15, 7]
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
