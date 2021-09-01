"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
例如，
    [2,3,4]的中位数是 3
    [2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
"""
from heapq import *


class MedianFinder:
    """
     A为小顶堆, B大顶堆，m, n 分别为A,B中元素的个数:
        A保存较大的一半、长度为N // 2 (N为偶数) 或 N+1 // 2 (N为奇数)
        B保存较小的一半、长度为N // 2 (N为偶数) 或 N+1 // 2 (N为奇数)
    中位数：
        A: am...a3a2a1    a1为堆顶   存储较大的一半
        B: b1b2b3...bm    b1为堆顶   存储较小的一半
        设共有 N = m + n 个元素，规定添加元素时保证：
        m = n + 1 = (N + 1) // 2   n为奇数
        m = n = N // 2             n为偶数

        中位数 =  a1                m != n
        中位数 =  (a1 + b1) // 2    m != n

        1.当 m == n 时，需要向A添加一个元素。实现方法：
            将新元素num加入B，再将B堆顶元素插入至A
        2.当 m != n 时，需要向B添加一个元素。实现方法：
            将新元素num加入A，再将A堆顶元素插入至B

                假设插入数字 num遇到情况 1. 。由于 num 可能属于 “较小的一半” （即属于 B），
                因此不能将 nums直接插入至 A 。而应先将 num插入至 B，
                再将 B 堆顶元素插入至 A 。这样就可以始终保持 A保存较大一半、 B保存较小一半。

                假设插入数字 num遇到情况 2. 。由于 num 可能属于 “较大的一半” （即属于A），
                因此不能将 nums直接插入至 B 。而应先将 num插入至 A，
                再将A堆顶元素插入至B。这样就可以始终保持 A保存较大一半、 B保存较小一半。

        ****这里重点是要确保A里有第一个数,即A,B都为空时，首先向A里加数，
            所以当A,B数量不等时，要向A里加，数量相等要向B里加

    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
        else:
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        print('A:', self.A, 'B:', self.B)

    def findMedian(self) -> float:
        print('1A:', self.A, 'B:', self.B)
        if len(self.A) == len(self.B):
            return (self.A[0] - self.B[0]) / 2.0
        else:
            return self.A[0]


class MedianFinder1:
    """
    首先要添加数据至数组中
    然后查找中位值
    使用快排来进行排序
    若是奇数则直接返回中间数
    若是偶数则返回中间两个 // 2

    这个方法超时了，每次查找都要排序，很费时间
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def quickSort(self, start, end):
        if start >= end:
            return
        left, right = start, end
        while left < right:
            while left < right and self.A[right] >= self.A[start]:
                right -= 1
            while left < right and self.A[left] <= self.A[start]:
                left += 1
            self.A[left], self.A[right] = self.A[right], self.A[left]
        self.A[left], self.A[start] = self.A[start], self.A[left]
        self.quickSort(left + 1, end)
        self.quickSort(start, left - 1)

    def quickSortThree(self, start, end):
        if start >= end:
            return
        left, right = start, end
        i = start + 1
        v = self.A[start]

        while i <= right:
            if self.A[i] < v:
                self.A[i], self.A[left] = self.A[left], self.A[i]
                i, left = i + 1, left + 1
            elif self.A[i] > v:
                self.A[i], self.A[right] = self.A[right], self.A[i]
                right -= 1
            else:
                i = i + 1
        self.quickSortThree(start, left - 1)
        self.quickSortThree(right + 1, end)

    def addNum(self, num: int) -> None:
        self.A.append(num)

    def findMedian(self) -> float:
        n = len(self.A)
        self.quickSortThree(0, n - 1)

        if n % 2 == 1:
            return self.A[n // 2]
        else:
            print(self.A)
            return (self.A[n // 2] + self.A[n // 2 - 1]) / 2


class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
        else:
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))

    def findMedian(self) -> float:
        if len(self.A) == len(self.B):
            return (self.A[0] - self.B[0]) / 2.0
        else:
            return self.A[0]


if __name__ == "__main__":
    """
    输入：
    ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
    [[],[1],[2],[],[3],[]]
    输出：[null,null,null,1.50000,null,2.00000]
    """
    A = MedianFinder()
    A.addNum(10)
    A.addNum(8)
    A.addNum(6)
    A.addNum(4)
    A.addNum(2)
    A.addNum(0)
    print(A.findMedian())
    A = MedianFinder()
    big = []
    heappush(big, 3)
    heappush(big, 6)
    print(big)

    heappush(big, 4)
    print(big)
    heappop(big)
    print(big)