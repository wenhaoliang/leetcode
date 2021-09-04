"""
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
链接：https://leetcode-cn.com/problems/number-of-islands
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        print("initCount:", self.count)

    def getCount(self):
        print("self.count:", self.count)
        return self.count

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def merge(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            self.parent[rootP] = rootQ
            self.count -= 1
        else:
            return


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        并查集中维护连通分量的个数，在遍历的过程中：
        相邻的陆地（只需要向右看和向下看）合并，只要发生过合并，岛屿的数量就减少 1；
        在遍历的过程中，同时记录海洋的数量；
        并查集中连通分量的个数 - 海洋的个数，就是岛屿数量。
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        def getIndex(x, y):
            return x * col + y

        # 水域的个数
        ocean = 0
        uf = UnionFind(row * col)

        # 1、统计水域的个数；2、合并陆地
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    ocean += 1
                else:
                    if i + 1 < row and grid[i + 1][j] == '1':
                        uf.merge(getIndex(i, j), getIndex(i + 1, j))
                    if j + 1 < col and grid[i][j + 1] == '1':
                        uf.merge(getIndex(i, j), getIndex(i, j + 1))

        print("ocean:", ocean)
        return uf.getCount() - ocean


class UnionFind1:
    def __init__(self):
        self.father = {}
        self.numOfSets = 0

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.numOfSets += 1

    def find(self, x):
        root = x

        while self.father[root] is not None:
            root = self.father[root]

        # while x != root:
        #     originalFather = self.father[x]
        #     self.father[x] = root
        #     x = originalFather

    def merge(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX != rootY:
            self.father[rootX] = rootY
            self.numOfSets -= 1


class Solution1:

    def numIslands(self, grid: List[List[str]]) -> int:
        return 1


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
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(A.numIslands(n))

    A = Solution1()
    n = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(A.numIslands(n))
