import collections
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] == 0 and nums[i+1] != 1:
                nums[i] = -1
        maxLen = 0
        curLen = 0
        zeroNums = 0
        deque = collections.deque()
        for i in range(len(nums)):
            if nums[i] == 1:
                deque.append(nums[i])
                curLen += 1
            if nums[i] == 0 and zeroNums == 0:
                deque.append(nums[i])
                zeroNums = 1
                continue
            if nums[i] == 0 and zeroNums == 1:

                for j in range(len(deque)):
                    if deque[j] == 1:
                        deque.popleft()
                    if deque[j] == 0:
                        deque.popleft()
                        break

                deque.append(nums[i])

            maxLen = max(maxLen, curLen)
            if nums[i] == -1:
                deque = collections.deque()
                zeroNums = 0
                curLen = 0
        return maxLen


A = Solution()
nums = [1, 0, 1, 0, 1, 1, 1, 1]
target = 8
print(A.isStraight(nums))
