import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []

        for i, j in zip(range(1-k, 1-k+len(nums)),  range(len(nums))):
            if i > 0 and deque[0] == nums[i-1]:
                deque.popleft()

            while deque and deque[-1] < nums[j]:
                deque.pop()

            deque.append(nums[j])
            if i >= 0:
                res.append(deque[0])
        return res







A = Solution()
matrix = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(A.maxSlidingWindow(matrix, k))
