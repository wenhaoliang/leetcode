"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
为了让您更好地理解问题，以下面的二叉搜索树为例：
          4
     2         5
1       3
我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
【图2】
特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，
树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
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
    def treeToDoublyList(self, root):
        """
        二叉搜索树中序遍历为递增序列

        1、首先找到第一个节点，即中序遍历查到最小值，设置cur、pre指向该节点
        2、然后遍历到下一个节点，此时cur指向当前节点，pre指向上一个节点，
            pre.next = cur -> pre.right = cur
            cur.up = pre   -> cur.left = pre
        3、最后cur指向最后一个节点,这里通过self.pre指向了cur，此时需要将头节点和最后节点连接起来
            cur.next = head -> cur.right = head
            这里由于cur只是在dfs()中，而dfs()中最后会【self.pre = cur】 ，所以用self.pre代替了cur，即
            【self.pre.next = head -> self.pre.right = head】
            head.up = cur   -> head.left = cur
        """

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return root


class Solution1:

    def treeToDoublyList(self, root):
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            else:
                self.head = cur

            self.pre = cur
            dfs(cur.right)

        if not root:
            return
        self.pre = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return root


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
    A = Solution()
    print(A.treeToDoublyList(n))

    n = TreeNode(4)
    n1 = TreeNode(2)
    n2 = TreeNode(5)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n.left = n1
    n.right = n2
    n1.left = n3
    n1.right = n4
    A = Solution1()
    print(A.treeToDoublyList(n))
