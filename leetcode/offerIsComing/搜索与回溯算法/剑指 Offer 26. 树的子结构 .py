"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
例如:
给定的树 A:
     3
    /  \
   4    5
  / \
 1  2
给定的树 B：
  4
 /
1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
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
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        名词规定：树 A 的根节点记作 节点 A，树 B 的根节点称为 节点 B 。
        recur(A, B) 函数：
            终止条件：
                当节点 B 为空：说明树 B已匹配完成（越过叶子节点），因此返回 true；
                当节点 A 为空：说明已经越过树 A 叶子节点，即匹配失败，返回 false；
                当节点 A 和 B 的值不同：说明匹配失败，返回 false ；
            返回值：
                判断 A 和 B 的左子节点是否相等，即 recur(A.left, B.left) ；
                判断 A 和 B 的右子节点是否相等，即 recur(A.right, B.right) ；

        isSubStructure(A, B) 函数：
            特例处理： 当 树 A 为空 或 树 B为空 时，直接返回 false ；
            返回值：若树 B 是树 A 的子结构，则必满足以下三种情况之一，因此用或 | 连接；
                1.以 节点 A 为根节点的子树 包含树 B ，对应 recur(A, B)；
                2.树 B 是 树 A 左子树 的子结构，对应 isSubStructure(A.left, B)；
                3.树 B 是 树 A 右子树 的子结构，对应 isSubStructure(A.right, B)；
            以上 2. 3. 实质上是在对树 A 做 先序遍历 。
        """

        def recur(node1, node2):
            if not node2:
                return True
            if not node1 or node1.val != node2.val:
                return False

            return recur(node1.left, node2.left) and recur(node1.right, node2.right)

        if A is None or B is None:
            return False
        result1 = recur(A, B)
        result2 = self.isSubStructure(A.left, B)
        result3 = self.isSubStructure(A.right, B)
        return result1 or result2 or result3


class Solution1:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        名词规定：树 A 的根节点记作 节点 A，树 B 的根节点称为 节点 B 。
        recur(A, B) 函数：
            终止条件：
                当节点 B 为空：说明树 B已匹配完成（越过叶子节点），因此返回 true；
                当节点 A 为空：说明已经越过树 A 叶子节点，即匹配失败，返回 false；
                当节点 A 和 B 的值不同：说明匹配失败，返回 false ；
            返回值：
                判断 A 和 B 的左子节点是否相等，即 recur(A.left, B.left) ；
                判断 A 和 B 的右子节点是否相等，即 recur(A.right, B.right) ；

        isSubStructure(A, B) 函数：
            特例处理： 当 树 A 为空 或 树 B为空 时，直接返回 false ；
            返回值：若树 B 是树 A 的子结构，则必满足以下三种情况之一，因此用或 | 连接；
                1.以 节点 A 为根节点的子树 包含树 B ，对应 recur(A, B)；
                2.树 B 是 树 A 左子树 的子结构，对应 isSubStructure(A.left, B)；
                3.树 B 是 树 A 右子树 的子结构，对应 isSubStructure(A.right, B)；
            以上 2. 3. 实质上是在对树 A 做 先序遍历 。
        """

        def recur(node1, node2):
            if not node2:
                return True
            if not node1 or node1.val != node2.val:
                return False

            return recur(node1.left, node2.left) and recur(node1.right, node2.right)

        if A is None or B is None:
            return False

        result1 = recur(A, B)
        result2 = self.isSubStructure(A.left, B)
        result3 = self.isSubStructure(A.right, B)
        return result1 or result2 or result3


if __name__ == "__main__":
    """
          给定的树 A:
                  3
             9         20
        15       7
        给定的树 B：
             9
        15
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

    m = TreeNode(9)
    m1 = TreeNode(15)
    m.left = m1

    PrintTree(n)
    PrintTree(m)
    A = Solution()
    print(A.isSubStructure(n, m))
    A = Solution1()
    print(A.isSubStructure(n, m))
