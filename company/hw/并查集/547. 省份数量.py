"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，
且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
示例 1：
    1 ----------  2
           3
输入：isConnected = [[1, 1, 0],
                    [1, 1, 0],
                    [0, 0, 1]]
输出：2

示例 2：
    1             2
           3
输入：isConnected = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]
输出：3
链接：https://leetcode-cn.com/problems/number-of-provinces
"""
from typing import List


class UnionFind:
    def __init__(self):
        self.parent = {}
        # 额外记录集合的数量
        self.num_of_sets = 0

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = None
            # 集合的数量+1
            self.num_of_sets += 1

    def find(self, x):
        root = x

        while self.parent[root] is not None:
            root = self.parent[root]

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(M)):
            uf.add(i)
            for j in range(i):
                if M[i][j]:
                    uf.merge(i, j)

        return uf.num_of_sets


class UnionFind1:
    def __init__(self):
        self.parent = {}
        self.numOfSets = 0

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = None
            self.numOfSets += 1

    def find(self, x):
        root = x
        while self.parent[root] is not None:
            root = self.parent[root]
        return root

    def merge(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX != rootY:
            self.parent[rootX] = rootY
            self.numOfSets -= 1


class Solution1:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind1()

        for i in range(len(M)):
            uf.add(i)
            for j in range(i):
                if M[i][j]:
                    uf.merge(i, j)

        return uf.numOfSets


if __name__ == "__main__":
    """
    基本概念
        1.并查集是一种数据结构
        2.并查集这三个字，一个字代表一个意思。
        3.并（Union），代表合并
        4.查（Find），代表查找
        5.集（Set），代表这是一个以字典为基础的数据结构，它的基本功能是合并集合中的元素，查找集合中的元素
        6.并查集的典型应用是有关连通分量的问题
        7.并查集解决单个问题（添加，合并，查找）的时间复杂度都是O(1)O(1)
        8.因此，并查集可以应用到在线算法中
    """
    A = Solution()
    n = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(A.findCircleNum(n))

    A = Solution1()
    n = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    print(A.findCircleNum(n))
