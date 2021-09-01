# -*- coding: utf-8 -*-
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5

链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
"""
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, left, mid, right):
            i, j, temp = left, mid + 1, []
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.count += mid - i + 1
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[left + i] = temp[i]

        def mergeSort(nums, left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, mid, right)

        self.count = 0
        mergeSort(nums, 0, len(nums) - 1)
        return self.count


class Solution1:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(nums, left, mid, right):
            i, j, temp = left, mid + 1, []
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.count += mid - i + 1
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= mid:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[left + i] = temp[i]

        def mergeSort(nums, left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, mid, right)

        self.count = 0
        n = len(nums)
        mergeSort(nums, 0, n - 1)
        return self.count


if __name__ == "__main__":
    A = Solution()
    print(A.reversePairs([7, 5, 3, 4]))
    A = Solution1()
    print(A.reversePairs([7, 5, 3, 4]))
