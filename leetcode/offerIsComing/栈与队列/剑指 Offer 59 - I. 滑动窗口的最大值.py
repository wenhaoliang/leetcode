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
        初始化： 双端队列deque,左右边界i,j
        滑动窗口：
            维护一个递减的双端队列
            左边界 i :(1-k, n-k+1) 右边界：j: (0,n)
            若左边界i > 0 且队首元素deque[0] == 被删除元素 Nums[i-1] 则将该元素从deque中出队
            入队新元素nums[j]时，删除deque内所有小于nums[j]的元素以保持deque递减
            将nums[j]入队
            若已形成窗口，即i>=0时，将窗口的最大值，即deque[0]添加到res
        返回值：res
        """
        deque = collections.deque()
        res = []
        n = len(nums)
        for (i, j) in zip(range(1 - k, n - k + 1), range(0, n)):
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()

            while deque and deque[-1] < nums[j]:
                deque.pop()

            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])

        return res

if __name__ == "__main__":
    """
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    """
    A = Solution()

    print('A', A.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
