"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value需要返回 -1
示例 1：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出:[null,null,null,2,1,2]
示例 2：
输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出:[null,-1,-1]
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
"""


class MaxQueue1:
    """2个数组"""

    def __init__(self):
        self.queue = []
        self.max_stack = []

    def max_value(self) -> int:
        if self.max_stack:
            return self.max_stack[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max_stack and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        ans = self.queue.pop(0)
        if ans == self.max_stack[0]:
            self.max_stack.pop(0)
        return ans


class MaxQueue2:
    """
    两个数组
    一个用来保存最大值
    一个用来保存新加入的数值
    """

    def __init__(self):
        self.queue = []
        self.maxStack = []

    def max_value(self) -> int:
        if not self.maxStack:
            return -1
        else:
            return self.maxStack[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.maxStack and self.maxStack[-1] < value:
            self.maxStack.pop()
        self.maxStack.append(value)

    def pop_front(self) -> int:
        ans = self.queue.pop(0)
        if ans == self.maxStack[0]:
            self.maxStack.pop(0)
        return ans


if __name__ == "__main__":
    """
    ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
    [[],[1],[2],[],[],[]]
    输出:[null,null,null,2,1,2]
    """
    a = MaxQueue2()
    a.push_back(1)
    a.push_back(2)
    a.push_back(3)
    a.push_back(4)
    a.push_back(4)
    a.push_back(5)

    a.max_value()
    a.pop_front()
    a.pop_front()
    a.pop_front()
    a.max_value()
