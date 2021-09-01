"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
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


# 返回链表节点
class Solution:
    # 返回ListNode
    def reversePrint(self, pHead):
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

    printListNode(a3)
