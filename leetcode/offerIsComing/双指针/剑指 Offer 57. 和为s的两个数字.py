"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        while i < n - 1:
            sum = nums[i] + nums[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [nums[i], nums[j]]
        return None


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        while i < n - 1:
            sum = nums[i] + nums[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == "__main__":
    """
    输入：nums = [2,7,11,15], target = 9
    输出：[2,7] 或者 [7,2]
    """
    nums = [2, 7, 11, 15]
    target = 9
    A = Solution()
    print(A.twoSum(nums, target))
    A = Solution1()
    print(A.twoSum(nums, target))
