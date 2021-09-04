"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：
输入： heights = [2,4]
输出： 4

链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
"""
import collections
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heightsLen = len(heights)
        arr = [0] * (heightsLen + 2)
        for i in range(heightsLen):
            arr[i + 1] = heights[i]
        arrLen = len(arr)

        stack = collections.deque()
        stack.append(0)
        res = 0
        index = 1

        while index < arrLen:
            while index < arrLen and (len(stack) == 0 or arr[stack[-1]] <= arr[index]):
                stack.append(index)
                index += 1

            while index < arrLen and arr[stack[-1]] > arr[index]:
                currentIndex = stack.pop()
                width = index - stack[-1] - 1
                height = arr[currentIndex]
                res = max(res, height * width)

            stack.append(index)
            index += 1

        return res


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heightsLen = len(heights)
        arr = [0] * (heightsLen + 2)
        for i in range(heightsLen):
            arr[i + 1] = heights[i]
        arrLen = len(arr)

        stack = collections.deque()
        stack.append(0)
        res = 0
        index = 1

        while index < arrLen:
            while index < arrLen and (len(stack) == 0 or arr[stack[-1]] <= arr[index]):
                stack.append(index)
                index += 1

            while index < arrLen and arr[stack[-1]] > arr[index]:
                currentIndex = stack.pop()
                width = index - stack[-1] - 1
                height = arr[currentIndex]
                res = max(res, height * width)

            stack.append(index)
            index += 1

        return res


if __name__ == "__main__":
    """
    输入：num = "1432219", k = 3
    输出："1219"
    """
    num = [2, 1, 5, 6, 2, 3]
    A = Solution()
    print(A.largestRectangleArea(num))
    A = Solution1()
    print(A.largestRectangleArea(num))
