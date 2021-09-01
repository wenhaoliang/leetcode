"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
"""
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quickSort(start, end):
            if start >= end:
                return
            left, right = start, end
            while left < right:
                while left < right and arr[right] >= arr[start]:
                    right -= 1
                while left < right and arr[left] <= arr[start]:
                    left += 1
                arr[left], arr[right] = arr[right], arr[left]
            arr[left], arr[start] = arr[start], arr[left]
            if left < k:
                return quickSort(left + 1, end)
            elif left > k:
                return quickSort(start, left - 1)
            else:
                return arr[0:k]

        quickSort(0, len(arr) - 1)
        return arr[0:k]


class Solution1:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quickSort(start, end):
            if start >= end:
                return

            left, right = start, end

            while left < right:
                while left < right and arr[right] >= arr[start]:
                    right -= 1
                while left < right and arr[left] <= arr[start]:
                    left += 1
                arr[left], arr[right] = arr[right], arr[left]
            arr[left], arr[start] = arr[start], arr[left]

            if k > left:
                return quickSort(left + 1, end)
            elif k < left:
                return quickSort(start, left - 1)
            else:
                return arr[:k]

        quickSort(0, len(arr) - 1)
        return arr[:k]


if __name__ == "__main__":
    """
    输入：arr = [3,2,1], k = 2
    输出：[1,2] 或者 [2,1]
    """
    nums = [3, 2, 1]
    k = 2
    print(Solution().getLeastNumbers(nums, k))
    print(Solution1().getLeastNumbers(nums, k))
