"""
树可以看成是一个连通且 无环的无向图。
给定往一棵 n 个节点 (节点值1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n中间，
且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges，
edges[i] = [ai, bi]表示图中在 ai 和 bi 之间存在一条边。
请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。
如果有多个答案，则返回数组edges中最后出现的边。
示例 1：
    1----2
    |   /
    |  /
    | /
    3
输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]
示例 2：
    2 ----- 1 ------ 5
    |       |
    |       |
    |       |
    3-------4
输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
提示:
        n == edges.length
        3 <= n <= 1000
        edges[i].length == 2
        1 <= ai< bi<= edges.length
        ai != bi
        edges 中无重复元素
        给定的图是连通的
链接：https://leetcode-cn.com/problems/redundant-connection
"""
from typing import List


class UnionFind:
    def __init__(self):
        self.father = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]
        return root

    def merge(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX != rootY:
            self.father[rootX] = rootY


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        在一棵树中，边的数量比节点的数量少 1。如果一棵树有 N 个节点，
        则这棵树有 N-1条边。这道题中的图在树的基础上多了一条附加的边，因此边的数量也是 N。
        树是一个连通且无环的无向图，在树中多了一条附加的边之后就会出现环，
        因此附加的边即为导致环出现的边。
        可以通过并查集寻找附加的边。初始时，每个节点都属于不同的连通分量。遍历每一条边，
        判断这条边连接的两个顶点是否属于相同的连通分量。
        如果两个顶点属于不同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间不连通，
        因此当前的边不会导致环出现，合并这两个顶点的连通分量。
        如果两个顶点属于相同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间已经连通，
        因此当前的边导致环出现，为附加的边，将当前的边作为答案返回。
        """
        uf = UnionFind()

        for node1, node2 in edges:
            uf.add(node1)
            uf.add(node2)
            if uf.find(node1) != uf.find(node2):
                uf.merge(node1, node2)
            else:
                return [node1, node2]

        return []


class UnionFind1:
    def __init__(self):
        self.parent = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = None

    def find(self, x):
        root = x
        while self.parent[root] is not None:
            root = self.parent[root]

        return root

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            self.parent[x] = y


class Solution1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind1()

        for node1, node2 in edges:
            uf.add(node1)
            uf.add(node2)
            if uf.find(node1) != uf.find(node2):
                uf.merge(node1, node2)
            else:
                return [node1, node2]

        return []


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
    n = [[1, 2], [3, 4], [3, 2], [1, 4], [1, 5]]
    print(A.findRedundantConnection(n))

    A = Solution1()
    n = [[1, 2], [3, 4], [3, 2], [1, 4], [1, 5]]
    print(A.findRedundantConnection(n))
