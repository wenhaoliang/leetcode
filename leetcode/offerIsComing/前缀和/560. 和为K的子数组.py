"""
给定一个整数数组和一个整数k，你需要找到该数组中和为k的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
"""

from typing import List


# O(n^2)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        preSum = [0] * (n + 1)
        res = 0
        resList = []

        # 本质上循环的是nums[i]，所以长度是n，preSum只是为了对齐i和左端0
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        for i in range(n):
            for j in range(i, n):
                if preSum[j + 1] - preSum[i] == k:
                    res += 1
                    resList.append([i, j])
        print('resList:', resList)
        return res


class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 细节，这里需要预存前缀和为 0 的情况，否则会漏掉前几位就满足的情况
        # 例如输入[1,1,0]，k = 2 如果没有这行代码，则会返回0,漏掉了1+1=2，和1+1+0=2的情况
        # 输入：[3,1,1,0] k = 2时则不会漏掉
        # preSum[3] - preSum[0]表示前面 3 位的和，所以需要map.put(0,1),垫下底
        hashMap = {0: 1}
        count = 0
        preSum = 0

        for x in nums:
            preSum += x
            # 当前前缀和已知，判断是否含有 preSum - k的前缀和，那么我们就知道某一区间的和为 k 了。
            if preSum - k in hashMap:
                # 获取次数
                count += hashMap.get(preSum - k)

            # 更新
            if hashMap.get(preSum) is None:
                hashMap[preSum] = 1
            else:
                hashMap[preSum] = hashMap[preSum] + 1

        return count


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0: 1}
        res = 0
        preSum = 0

        for num in nums:
            preSum += num

            if preSum - k in hashMap:
                res += hashMap.get(preSum - k)

            hashMap[preSum] = hashMap.get(preSum, 0) + 1


        return res


if __name__ == "__main__":
    """
    """
    num = [1, -1, 0]
    k = 0
    A = Solution()
    print(A.subarraySum(num, k))
    A = Solution1()
    print(A.subarraySum(num, k))
    A = Solution2()
    print(A.subarraySum(num, k))
    a = {0: 1}
    print('-------------')
    print(a[0])
    print(a.get(0))
