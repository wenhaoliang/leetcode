"""
给定一个仅包含0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
示例 1：
[
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
]
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：        "1", "1", "1"],
             "1", "1", "1"],
最大矩形如上图所示。
示例 2：
输入：matrix = []
输出：0
示例 3：
输入：matrix = [["0"]]
输出：0
示例 4：
输入：matrix = [["1"]]
输出：1
示例 5：
输入：matrix = [["0","0"]]
输出：0

链接：https://leetcode-cn.com/problems/maximal-rectangle
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        if row == 0:
            return 0

        heights = [0] * col
        maxArea = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea, self.largestRectangleArea(heights))

        return maxArea


# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#


if __name__ == "__main__":
    """
    """
    num = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    A = Solution()
    print(A.maximalRectangle(num))
    # A = Solution1()
    # print(A.maximalRectangle(num))
