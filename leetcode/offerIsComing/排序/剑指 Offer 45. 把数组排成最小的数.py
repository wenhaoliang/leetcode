"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
示例 1:
输入: [10,2]
输出: "102"
示例2:
输入: [3,30,34,5,9]
输出: "3033459"
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
"""
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """
        设 x + y > y + x，则x > y
        x “小于” y代表：排序完成后，数组中 x 应在 y 左边；“大于” 则反之。
        """

        def quickSort(start, end):
            if start >= end:
                return
            left, right = start, end
            while left < right:
                while left < right and strs[right] + strs[start] >= strs[start] + strs[right]:
                    right -= 1
                while left < right and strs[left] + strs[start] <= strs[start] + strs[left]:
                    left += 1
                strs[left], strs[right] = strs[right], strs[left]
            strs[left], strs[start] = strs[start], strs[left]
            quickSort(start, left - 1)
            quickSort(left + 1, end)

        strs = []
        for num in nums:
            strs.append(str(num))
        quickSort(0, len(strs) - 1)
        return ''.join(strs)


class Solution1:
    def minNumber(self, nums: List[int]) -> str:
        def quickSort(start, end):
            if start >= end:
                return
            left, right = start, end
            while left < right:
                while left < right and strs[right] + strs[start] >= strs[start] + strs[right]:
                    right -= 1
                while left < right and strs[left] + strs[start] <= strs[start] + strs[left]:
                    left += 1
                strs[left], strs[right] = strs[right], strs[left]
            strs[left], strs[start] = strs[start], strs[left]

            quickSort(start, left - 1)
            quickSort(left + 1, end)

        strs = []
        for i in range(len(nums)):
            strs.append(str(nums[i]))

        quickSort(0, len(nums) - 1)
        return ''.join(strs)


if __name__ == "__main__":
    """
    输入: [3,30,34,5,9]
    输出: "102"
    """
    A = Solution()
    nums = [3, 30, 34, 5, 9]
    print(A.minNumber(nums))
    A = Solution1()
    nums = [3, 30, 34, 5, 9]
    print(A.minNumber(nums))
