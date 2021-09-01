"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，
而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
示例1:
输入: [1,2,3,4,5]
输出: True
示例2:
输入: [0,0,1,2,5]
输出: True
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        numMax, numMin = 0, 14
        for i in nums:
            if i in repeat:
                return False
            if i == 0:
                continue
            numMax = max(i, numMax)
            numMin = min(i, numMin)
            repeat.add(i)

        return numMax - numMin < 5


class Solution1:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        numMax, numMin = 0, 14
        for num in nums:
            if num in repeat:
                return False
            if num == 0:
                continue
            repeat.add(num)

            numMax = max(num, numMax)
            numMin = min(num, numMin)
        return (numMax - numMin) < 5


if __name__ == "__main__":
    """
    输入: [1,2,3,4,5]
    输出: True
    """
    A = Solution()
    nums = [1, 2, 3, 4, 5]
    print(A.isStraight(nums))
    A = Solution1()
    nums = [1, 2, 3, 4, 5]
    print(A.isStraight(nums))
