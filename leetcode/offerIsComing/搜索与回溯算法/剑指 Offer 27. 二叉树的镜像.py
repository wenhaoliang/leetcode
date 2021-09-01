"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
例如输入：
     4
  2     7
1  3  6  9
镜像输出：
    4
  7    2
9  6  3  1
示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
链接：https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof
"""
import collections
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
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root


class Solution1:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = collections.deque()
        stack.append(root)
        while stack:
            node = stack.popleft()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left

        return root


class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        deque = collections.deque()
        deque.append(root)
        while deque:
            node = deque.popleft()
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)

            node.left, node.right = node.right, node.left

        return root

if __name__ == "__main__":
    """
    例如输入：
         4
      2     7
    1  3  6  9
    镜像输出：
        4
      7    2
    9  6  3  1
    """

    n = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(7)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(6)
    n6 = TreeNode(9)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6

    PrintTree(n)

    A = Solution1()
    PrintTree(A.mirrorTree(n))

    stack = [1, 2, 3]
    print(stack.pop(0))
