"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
"""
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        初始化： 双端队列 deque ，结果列表 res ，数组长度 n；
        滑动窗口：
            左边界范围 i∈[1−k,n−k] ，右边界范围 j∈[0,n−1] ；
            若 i>0且队首元素deque[0] == 被删除元素 nums[i - 1]：则队首元素出队；
            删除 deque内所有 < nums[j]的元素，以保持 deque递减；
            将 nums[j]添加至 deque尾部；
            若已形成窗口（即 i≥0 ）：将窗口最大值（即队首元素 deque[0]）添加至列表 res ；
        返回值： 返回结果列表 res；
        """
        deque = collections.deque()
        res = []

        for i, j in zip(range(1 - k, 1 - k + len(nums)), range(len(nums))):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()

            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()

            deque.append(nums[j])

            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        初始化： 双端队列 deque ，结果列表 res ，数组长度 n；
        滑动窗口：
            左边界范围 i:[1−k,n−k] ，右边界范围 j:[0,n−1] ；
            若 i>0且队首元素deque[0] == 被删除元素 nums[i - 1]：则队首元素出队；
            在nums[j]入队时，删除 deque内所有 < nums[j]的元素，以保持 deque递减；
            将 nums[j]添加至 deque尾部；
            若已形成窗口（即 i≥0 ）：将窗口最大值（即队首元素 deque[0]）添加至列表 res ；
        返回值： 返回结果列表 res；
        """
        deque = collections.deque()
        res = []
        n = len(nums)

        for (i, j) in zip(range(1 - k, 1 - k + n), range(n)):
            if i > 0 and deque[0] == nums[i-1]:
                deque.popleft()

            while deque and deque[-1] < nums[j]:
                deque.pop()

            deque.append(nums[j])

            if i >= 0:
                res.append(deque[0])

        return res


if __name__ == "__main__":
    """
    

    """
    A = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(A.maxSlidingWindow(nums, k))

    A = Solution1()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(A.maxSlidingWindow(nums, k))
