"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        状态定义：dp[j] 表示到j为止最长的子字符串
        转移方程：固定有边界j，向左查找与s[j]相等的s[i]，
        1、i < 0, 为向左查找不到与s[j]相等的字符， 此时d[j] = dp[j-1] + 1
        2、dp[j-1] < j - i, j-i这里表示有边界到左边界之间的字符串长度，
        若小于则表示左边界那个相等的字符对目前最长字串长度无影响，
        则可将有边界的这个字符加上去，即d[j] = dp[j-1] + 1
        3、dp[j-1] >= j - i, 即左边界的那个字符在目前的最长子字符里面，
        所以要重新计算最长子字符串长度，即dp[j] = j - i
        初始状态:  dp[0] = 0
        返回值:  设置一个res来记录最大值
        """
        length = len(s)
        dp = [0] * length
        res = 0
        for j in range(length):
            i = j - 1
            while i >= 0 and s[i] != s[j]:
                i -= 1  # 线性查找 i
            if dp[j - 1] < j - i:
                dp[j] = dp[j - 1] + 1
            else:
                dp[j] = j - i
            res = max(res, dp[j])
        return res


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        状态定义: dp[j] 表示到 j为止最长的无重复字符字串 长度
        转移方程：针对dp[j-1] >? j-i 来分类讨论
                s[i] 为 遍历得出，与s[j]相同的字符，若i<0则表示没有字符与s[j]匹配
                j-i 表示与s[j]匹配的字符s[i]的长度
            1、 dp[j-1] >= j-i => dp[j] = j-i
                表示dp[j-1]的长度，把与s[j]相匹配的[i]的长度包含进去了，所以要更新长度为j-i开始计数
            2、dp[j-1] < j-i => dp[j] = dp[j-1] + 1
                表示dp[j-1]的长度小于与s[j]相匹配的[i]的长度，那么就把当前元素的长度加上
        初始状态：dp[0] = 0
        返回结果： 设置一个res来记录最大值
        """
        n = len(s)
        dp = [0] * n
        res = 0
        for j in range(n):
            i = j - 1
            while i >= 0 and s[i] != s[j]:
                i -= 1

            if dp[j-1] < j - i:
                dp[j] = dp[j - 1] + 1
            else:
                dp[j] = j - i

            res = max(res, dp[j])

        return res


if __name__ == "__main__":
    A = Solution()
    n = "abcabcbb"
    print(A.lengthOfLongestSubstring(n))
    A = Solution1()
    n = "abcabcbb"
    print(A.lengthOfLongestSubstring(n))

    """
    举个例子，比如“abcdbaa”，索引从0开始。 
    我们容易得到，当 j = 4时，以s[4]结尾字符串sub[4] = “cdb”的 长度dp[4] =3。 
    接下来我们看 j +1的情况。根据定义，sub[4]字符串中的字符肯定不重复，
    所以当 j = 5时，这时距离字符s[5]的左侧的重复字符a的索引 i = 0， 
    也就是说s[ 0 ]在子字符串sub[ 4 ]之外了，
    以s[5]结尾的字符串自然在sub[4]的基础上加上字符s[5]就构成了新的最长的不重复的子串sub[5]，
    长度dp[5] = dp[4] + 1; 接下来我们继续看 j =6的情况，
    这时s[6]的左侧重复字符a的索引 i = 5，该重复字符在sub[ 5 ]中。
    新的最长不重复的字串sub[6]左边界以 i 结尾，长度dp[6] = j - i = 1。
    """
