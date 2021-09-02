"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回 -1 )
示例 1：输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：1 <= values <= 10000 最多会对appendTail、deleteHead 进行10000次调用

链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
"""


class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# class CQueue1:
#
#     def __init__(self):
#
#
#     def appendTail(self, value: int) -> None:
#
#
#     def deleteHead(self) -> int:
#

if __name__ == "__main__":
    """
    ["CQueue", "appendTail", "deleteHead", "deleteHead"]
    [[], [3], [], []]
    输出：[null, null, 3, -1]
    一个队列具备的两个功能分别由两个栈来完成：栈A实现入队功能，栈B实现出队功能
    """
    obj = CQueue()
    obj.appendTail(1)
    obj.appendTail(2)
    obj.appendTail(3)
    parm = obj.deleteHead()
    obj.appendTail(4)
    obj.deleteHead()

    print('obj.A', obj.A)
    print('obj.B', obj.B)
    print('parm', parm)
