"""
给定一个整数数组 A，返回其中元素之和可被 K整除的（连续、非空）子数组的数目。
示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
"""

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSum = 0
        res = 0
        hashMap = {0: 1}

        for num in nums:
            preSum += num
            # 和为5
            if preSum % 5 in hashMap:
                res += hashMap[preSum]

        return 1


if __name__ == "__main__":
    """
    """
    num = [1, 1, 2, 1, 1]
    k = 3
    A = Solution()
    print(A.subarraysDivByK(num, k))
    # A = Solution1()
    # print(A.trap(num))
