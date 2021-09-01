from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[n-1][0], dp[n-1][1])


if __name__ == "__main__":
    nums = [1]
    A = Solution()
    print(A.massage(nums))
