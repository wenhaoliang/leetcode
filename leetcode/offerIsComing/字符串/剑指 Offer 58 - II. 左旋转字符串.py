"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请
定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
示例 1：
输入: s = "abcdefg", k = 2
输出:"cdefgab"
示例 2：
输入: s = "lrloseumgh", k = 6
输出:"umghlrlose"

链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # return s[n:] + s[:n]
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)


class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        length = len(s)
        for i in range(n, length):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)


if __name__ == "__main__":
    """
    输入：head = [1,3,2]
    输出：[2,3,1]
    """
    s = "abcdefg"
    k = 2
    A = Solution()
    print(A.reverseLeftWords(s, k))
    A = Solution1()
    print(A.reverseLeftWords(s, k))
