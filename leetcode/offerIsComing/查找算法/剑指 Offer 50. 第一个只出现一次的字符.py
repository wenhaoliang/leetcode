"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
示例:
s = "abaccdeff"
返回 "b"
s = ""
返回 " "
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        nums = {}
        for i in s:
            if i in nums:
                nums[i] += 1
            else:
                nums[i] = 1
        for i in s:
            if nums[i] == 1:
                print(nums)
                return i
        print(nums)
        return ' '


class Solution1:
    def firstUniqChar(self, s: str) -> str:
        nums = {}
        for i in s:
            if i not in nums:
                nums[i] = 1
            else:
                nums[i] += 1
        print('1', nums)
        for i in nums:
            if nums[i] == 1:
                return i

        return ' '


if __name__ == "__main__":
    """
    s = s = "abaccdeff"
    返回 "b"
    """
    A = Solution()
    s = "abaccdeff"
    print(A.firstUniqChar(s))
    A = Solution1()
    s = "abaccdeff"
    print(A.firstUniqChar(s))
