"""
请根据每日 气温 列表 temperatures，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出:[1,1,4,2,1,1,0,0]
示例 2:
输入: temperatures = [30,40,50,60]
输出:[1,1,1,0]
示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]

链接：https://leetcode-cn.com/problems/daily-temperatures
"""
import collections
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        res = [0] * n
        index = 0
        stack = collections.deque()

        while index < n:
            while index < n and (len(stack) == 0 or temperatures[stack[-1]] >= temperatures[index]):
                stack.append(index)
                index += 1

            while index < n and len(stack) != 0 and temperatures[stack[-1]] < temperatures[index]:
                currentIndex = stack.pop()
                res[currentIndex] = index - currentIndex

        return res

# class Solution1:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         heightsLen = len(heights)
#         arr = [0] * (heightsLen + 2)
#         for i in range(heightsLen):
#             arr[i + 1] = heights[i]
#         arrLen = len(arr)
#
#         stack = collections.deque()
#         stack.append(0)
#         res = 0
#         index = 1
#
#         while index < arrLen:
#             while index < arrLen and (len(stack) == 0 or arr[stack[-1]] <= arr[index]):
#                 stack.append(index)
#                 index += 1
#
#             while index < arrLen and arr[stack[-1]] > arr[index]:
#                 currentIndex = stack.pop()
#                 width = index - stack[-1] - 1
#                 height = arr[currentIndex]
#                 res = max(res, height * width)
#
#             stack.append(index)
#             index += 1
#
#         return res


if __name__ == "__main__":
    """
        [73, 72, 75, 71, 69, 72, 76, 73]
        [2, 1, 4, 2, 1, 1, 0, 0]
    """
    num = [73, 72, 75, 71, 69, 72, 76, 73]
    A = Solution()
    print(A.dailyTemperatures(num))
    # A = Solution1()
    # print(A.largestRectangleArea(num))
