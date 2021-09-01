import collections
from typing import List


class Solution:
    def climbStairs(self, n, A) -> int:
        dp = [9999999] * (n + 1)
        dp[0] = -1
        for i in range(1, n + 1):
            dp[i] = min(dp[i], dp[i - 1] + 1)
            m = i + A[i - 1]
            q = n + 1
            if i + A[i - 1] < n + 1:
                w = dp[i] + 1
                e = dp[i + A[i - 1]]
                dp[i + A[i - 1]] = min(dp[i] + 1, dp[i + A[i - 1]])

        return dp[n]


A = Solution()
n, B = 10, [2, 3, 1, 9, 8, 7, 7, 7, 5, 6]
print(A.climbStairs(n, B))
