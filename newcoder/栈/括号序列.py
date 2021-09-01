#
#
# @param s string字符串
# @return bool布尔型
#
class Solution:
    def isValid(self, s):
        # write code here
        # 长度为奇数 一定不对
        if len(s) % 2 == 1:
            return False
        # 只有3种括号在s中，才进行替换
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('[]', '').replace('{}', '').replace('()', '')
        return True if s == '' else False


class Solution1:
    def isValid(self, s):
        # write code here
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False


class Solution2:
    def isValid(self, s):
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i == "]" and stack[-1] == '[':
                stack.pop()
            elif i == "}" and stack[-1] == '{':
                stack.pop()
            elif i == ")" and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False


if __name__ == "__main__":
    arr = "[](([[]]){}{[]}([]))"
    # arr = "[]"
    A = Solution1()
    print(A.isValid(arr))
    A = Solution2()
    print(A.isValid(arr))
