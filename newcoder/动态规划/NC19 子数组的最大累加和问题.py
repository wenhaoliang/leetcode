"""
给定一个数组arr，返回子数组的最大累加和
例如，arr = [1, -2, 3, 5, -2, 6, -1]，所有子数组中，[3, 5, -2, 6]可以累加出最大的和12，所以返回12.
题目保证没有全为负数的数据
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)
示例1 输入：[1, -2, 3, 5, -2, 6, -1] 返回值：12
"""

#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
from typing import List


# class Solution:
#     def maxsumofSubarray(self, arr):
#         # write code here
#         return arr


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = maxRes = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            maxRes = max(maxRes, dp[i])
        return maxRes




if __name__ == "__main__":
    arr = [1, -2, 3, 5, -2, 6, -1]
    A = Solution1()
    print(A.maxSubArray(arr))
