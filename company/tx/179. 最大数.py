"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
nums
示例 1：
输入：nums = [10,2]
输出："210"
示例nums2：
输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：
输入：nums = [1]
输出："1"
示例 4：
输入：nums = [10]
输出："10"
链接：https://leetcode-cn.com/problems/largest-number
"""

from typing import List
import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            return 1 if x + y < y + x else -1

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(cmp))
        res = str(int("".join(nums)))
        return res


# 冒泡排序
class Solution1:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        a = list(map(str, nums))
        # 冒泡排序 从后往前起泡，大的放在前面
        for i in range(n):
            for j in range(n - 1, i, -1):
                if a[j] + a[i] > a[i] + a[j]:
                    a[i], a[j] = a[j], a[i]

        if a[0] == "0":
            return "0"
        return ''.join(a)


# 选择排序
class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str, nums))
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        return str(int("".join(nums)))


class Solution3:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str, nums))
        print(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        return str(int("".join(nums)))


if __name__ == "__main__":
    print(Solution().largestNumber([3, 30, 34, 5, 9]))
    print(Solution3().largestNumber([3, 30, 34, 5, 9]))
