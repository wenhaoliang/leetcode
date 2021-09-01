from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def halfFind(target):
            i, j = 0, len(nums) - 1
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid - 1
            return i

        return halfFind(target) - halfFind(target - 1)


A = Solution()
nums = [5, 7, 8, 9, 10]
target = 8
A.search(nums, target)
