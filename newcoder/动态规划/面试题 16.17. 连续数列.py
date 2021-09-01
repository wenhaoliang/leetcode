from typing import List


# -*- coding:utf-8 -*-
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        res = nums[0]
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
            res = max(dp[i], res)
        return res


if __name__ == "__main__":
    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [-1]
    A = Solution()
    print(A.maxSubArray(arr))
