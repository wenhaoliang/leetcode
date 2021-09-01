"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
"""
import sys


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(head):
    if head is None:
        sys.stdout.write("{}")
        return
    current = head
    sys.stdout.write("{")
    while current:
        if current == head:
            sys.stdout.write("%d" % current.val)
        else:
            sys.stdout.write(",%d" % current.val)
        current = current.next

    sys.stdout.write("}")


class Solution:
    def reversePrint(self, head: ListNode):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        res = []
        while stack:
            res.append(stack.pop())

        return res





if __name__ == "__main__":
    """
    输入：head = [1,3,2]
    输出：[2,3,1]
    """
    A = Solution()
    a1 = ListNode(1)
    a2 = ListNode(3)
    a3 = ListNode(2)
    a1.next = a2
    a2.next = a3

    print(A.reversePrint(a1))
    printListNode(a3)
