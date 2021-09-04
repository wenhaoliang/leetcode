"""
给定n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

链接：https://leetcode-cn.com/problems/trapping-rain-water
"""
import collections
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)
        heightLen = len(height)
        stack = collections.deque()
        res = 0
        index = 0
        while index < heightLen:

            while index < heightLen and (len(stack) == 0 or height[stack[-1]] >= height[index]):
                stack.append(index)
                index += 1

            if index == heightLen:
                break

            while len(stack) != 0 and height[stack[-1]] < height[index]:
                currentIndex = stack.pop()
                if len(stack) == 0:
                    break

                width = index - stack[-1] - 1
                height1 = min(height[index], height[stack[-1]]) - height[currentIndex]
                res += height1 * width

        return res


class Solution1:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = collections.deque()
        res = 0
        index = 0

        while index < n:
            while index < n and (len(stack) == 0 or height[stack[-1]] >= height[index]):
                stack.append(index)
                index += 1

            if index == n:
                break

            while index < n and len(stack) != 0 and height[stack[-1]] < height[index]:
                currentIndex = stack.pop()

                if len(stack) == 0:
                    break

                width = index - stack[-1] - 1
                height1 = min(height[index], height[stack[-1]]) - height[currentIndex]
                res += width * height1

        return res




if __name__ == "__main__":
    """
    """
    num = [4, 2, 0, 3, 2, 5]
    A = Solution()
    print(A.trap(num))
    A = Solution1()
    print(A.trap(num))