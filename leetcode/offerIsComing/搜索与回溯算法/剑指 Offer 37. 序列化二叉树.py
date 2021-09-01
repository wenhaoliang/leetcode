"""
请实现两个函数，分别用来序列化和反序列化二叉树。
你需要设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
示例：
          1
    2         3
          4        5
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
"""
import collections
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


class Codec:

    def serialize(self, root):
        """
        将二叉树bfs遍历，并记录叶子节点
        """
        if not root:
            return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """
        根据bfs来复原二叉树
        """
        if data == "[]":
            return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root


class Codec1:

    def serialize(self, root):
        if not root:
            return
        deque = collections.deque()
        deque.append(root)
        res = []
        while deque:
            node = deque.popleft()
            if node:
                res.append(str(node.val))
                deque.append(node.left)
                deque.append(node.right)
            else:
                res.append('null')
        return res

    def deserialize(self, data):
        if not data:
            return

        deque = collections.deque()
        root = TreeNode(int(data[0]))
        print("1:", root.val)
        deque.append(root)
        i = 1
        while deque:
            node = deque.popleft()
            if data[i] != 'null':
                node.left = TreeNode(int(data[i]))
                deque.append(node.left)
            i += 1

            if data[i] != 'null':
                node.right = TreeNode(int(data[i]))
                deque.append(node.right)
            i += 1

        return root


if __name__ == "__main__":
    """
          1
    2         3
          4        5 
    """

    n = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    n4 = TreeNode(5)
    n.left = n1
    n.right = n2
    n2.left = n3
    n2.right = n4
    codec = Codec()
    PrintTree(n)
    data = codec.serialize(n)
    print(data)
    PrintTree(codec.deserialize(data))
    print('---')
    codec = Codec1()
    PrintTree(n)
    data = codec.serialize(n)
    print(data)
    PrintTree(codec.deserialize(data))
