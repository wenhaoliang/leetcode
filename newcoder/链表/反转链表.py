# -*- coding:utf-8 -*-
"""
描述
输入一个链表，反转链表后，输出新链表的表头。
示例1 输入： {1,2,3} 返回值： {3,2,1}
"""
import sys


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
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        p, q = pHead, None
        while p:
            temp = p.next
            p.next = q
            q = p
            p = temp
        return q


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    A = Solution()
    printListNode(A.ReverseList(node1))
