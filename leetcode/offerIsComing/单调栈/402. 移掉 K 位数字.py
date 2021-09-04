"""
给你一个以字符串表示的非负整数num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
示例 1 ：
输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
示例 2 ：
输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 ：
输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 。
链接：https://leetcode-cn.com/problems/remove-k-digits
"""
import collections


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        # 首先创建一个单调栈->双端队列吧？
        deque = collections.deque()
        index = 0
        count = n - k

        while index < n:
            while index < n and (len(deque) == 0 or deque[-1] <= num[index]):
                deque.append(num[index])
                index += 1
            if index == n:
                break
            while len(deque) != 0 and deque[-1] > num[index] and len(deque) + n - index - 1 >= count:
                deque.pop()
            deque.append(num[index])
            index += 1

        res = ''.join(deque)
        if count == 0 or len(deque) == 0 or res == '0' or res == '00':
            return "0"

        return res[:count].lstrip('0')


# class Solution1:
#     def removeKdigits(self, num: str, k: int) -> str:


if __name__ == "__main__":
    """
    输入：num = "1432219", k = 3
    输出："1219"
    """
    num = "10001"
    k = 4
    A = Solution()
    print(A.removeKdigits(num, k))
    # A = Solution1()
    # print(A.removeKdigits(num, k))
