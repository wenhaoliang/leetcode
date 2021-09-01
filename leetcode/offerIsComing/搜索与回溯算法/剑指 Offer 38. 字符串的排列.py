"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        """
        首先将 s 字符化
        首先固定一位字符 x，序号为i
        然后将 x与后面字符依次交换，这里交换是从这个字符本身开始
        例如：当i = 0， 交换时要从0开始交换，这样就确保了不会漏掉种类
        然后当有重复字符时的处理，
        维护一个set()，当每次交换时，将该元素加入set，
        接下交换时，首先判断该元素是否在set()中，若在就跳过这个交换
        """
        n = len(s)
        strList = list(s)
        res = []

        def dfs(x):
            if x == n - 1:
                res.append(''.join(strList))
                return

            dic = set()
            for i in range(x, n):
                if strList[i] in dic:
                    continue

                dic.add(strList[i])
                strList[i], strList[x] = strList[x], strList[i]
                dfs(x + 1)
                strList[i], strList[x] = strList[x], strList[i]

        dfs(0)
        return res


class Solution1:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        list = [s[i] for i in range(n)]
        res = []

        def dfs(x):
            if x == n - 1:
                res.append(''.join(list))

            dic = set()
            for i in range(x, n):
                if list[i] in dic:
                    continue
                dic.add(list[i])
                list[i], list[x] = list[x], list[i]
                dfs(x + 1)
                list[i], list[x] = list[x], list[i]

        dfs(0)
        return res


if __name__ == "__main__":
    A = Solution()
    print(A.permutation("abc"))
    A = Solution1()
    print(A.permutation("abc"))
