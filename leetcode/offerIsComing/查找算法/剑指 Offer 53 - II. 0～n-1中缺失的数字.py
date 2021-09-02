"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
示例 1:
输入: [0,1,3]
输出: 2
示例2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            if nums[0] == 1:
                return 0
        if len(nums) == nums[-1] + 1:
            return nums[-1] + 1

        for i in range(nums[0], nums[-1]):
            if i != nums[i]:
                return i


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:

            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    """
    输入: [0,1,3]
    输出: 2
    排序数组中的搜索问题，首先想到 二分法 解决。
    """
    A = Solution1()
    nums = [0, 1, 2, 3, 5]

    print(A.missingNumber(nums))
    A = Solution2()
    nums = [0, 1, 2, 3, 5]

    print(A.missingNumber(nums))
