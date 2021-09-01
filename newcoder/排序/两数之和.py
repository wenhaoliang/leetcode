"""
两数之和
https://www.nowcoder.com/questionTerminal/2025b57a0f4b464eb85a63fc617ab5b1
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
示例1 输入 [2, 7, 11, 15],9 输出 [0,1]
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]


class Solution1:
    def twoSum(self, numbers, target):
        # write code here
        hashMap = {}
        for index, num in enumerate(numbers):
            hashMap[num] = index

        for index, num in enumerate(numbers):
            divideNum = hashMap.get(target - num)
            if divideNum and divideNum != index:
                return [index, divideNum]


if __name__ == "__main__":
    # arr, k = [3, 2, 4], 6
    arr, k = [2, 7, 11, 15], 9
    A = Solution1()
    print(A.twoSum(arr, k))
