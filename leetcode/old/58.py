import collections
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        # print(s)
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1: j + 1])
            print(res)
            while s[i] == " ":
                i -= 1
            j = i
        return ' '.join(res)


A = Solution()
nums = "the sky is blue"
target = 8
print(A.reverseWords(nums))
