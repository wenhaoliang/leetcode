"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
输入：s = "We are happy."
输出："We%20are%20happy."

链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for i in s:
            if i == " ":
                res.append("%20")
            else:
                res.append(i)
        return ''.join(res)


if __name__ == "__main__":
    """
    输入：head = [1,3,2]
    输出：[2,3,1]
    """
    A = Solution()
    s = "We are happy."

    print(A.replaceSpace(s))
