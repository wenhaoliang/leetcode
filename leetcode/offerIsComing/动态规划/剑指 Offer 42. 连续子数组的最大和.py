"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:连续子数组[4,-1,2,1] 的和最大，为6。
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        状态定义：dp[i]为到i位置最大的子数组和
        转移方程：dp[i] = max(dp[i-1] + nums[i], nums[i])
        初始状态: dp[0] = nums[0]
        返回值:  ans
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]
        ans = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(ans, dp[i])
        print(dp)
        return ans


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        状态定义：dp[i]为到i位置最大的子数组和
        转移方程：
            判断前面的dp[i-1]是否为负数，若是负数，
            则表示加上当前的nums[i]肯定小于从Nums[i]开始计数的大，
            即对最大字数和贡献为负，所以不要之前的子树和
                dp[i] = max(dp[i-1] + nums[i], nums[i])
        初始状态: dp[0] = nums[0]
        返回值:  ans
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(dp[i], ans)
        return ans


if __name__ == "__main__":
    A = Solution()
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(A.maxSubArray(n))

    A = Solution1()
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(A.maxSubArray(n))
