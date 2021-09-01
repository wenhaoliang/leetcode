# -*- coding:utf-8 -*-
import sys

"""
输入一个链表，输出该链表中倒数第k个结点。
如果该链表长度小于k，请返回空。
示例1 输入{1,2,3,4,5},1  返回值 {5}
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, pHead, k):
        # write code here
        if not pHead:
            return None
        slow, quick = pHead, pHead
        while quick is not None and k > 0:
        # while not quick and k > 0:
            quick = quick.next
            k = k - 1
        if k > 0:
            return None
        while quick is not None:
            quick = quick.next
            slow = slow.next
        return slow.val

    # if not head:
    #     return head
    # slow, fast = head, head
    #
    # while not fast and k > 0:
    #     fast = fast.next
    #     k -= 1
    # if k > 0:
    #     return None
    # while not fast:
    #     slow = slow.next
    #     fast = fast.next
    # return slow


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


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    k = 3
    A = Solution()
    print(A.FindKthToTail(node1, k))
    printListNode(node1)
    # printListNode(A.hasCycle(node1))
    # printListNode(node1)
