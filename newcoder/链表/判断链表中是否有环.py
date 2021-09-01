# -*- coding:utf-8 -*-
"""
链接：https://www.nowcoder.com/practice/650474f313294468a4ded3ce0f7898b9?tpId=117&&tqId=37714&&companyId=134&rp=1&ru=/company/home/code/134&qru=/ta/job-code-high/question-ranking
判断给定的链表中是否有环。如果有环则返回true，否则返回false。
输入分为2部分，第一部分为链表，第二部分代表是否有环，然后回组成head头结点传入到函数里面。
-1代表无环，其他的数字代表有环，这些参数解释仅仅是为了方便读者自测调试
示例1 输入{3,2,0,-4},1 输出 true
说明 第一部分{3,2,0,-4}代表一个链表，第二部分的1表示，-4到位置1，即-4->2存在一个链接，组成传入的head为一个带环的链表 ,返回true
示例2 输入{1},-1 输出 false
说明 第一部分{1}代表一个链表，-1代表无环，组成传入head为一个无环的单链表，返回false
示例 3输入 {-1,-7,7,-4,19,6,-9,-5,-2,-5},6 输出 true
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


#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    # 一个链表从头节点开始一个个删除，所谓删除就是让他的next指针指向他自己。
    # 如果没有环，从头结点一个个删除，最后肯定会删完，
    def hasCycle1(self, head):
        if not head:
            return False

        node = head

        while node:
            nodeNext = node.next
            if nodeNext == node:
                return True
            else:
                node.next = node
                node = nodeNext
        return False

    # 快慢节点
    def hasCycle2(self, head):
        if not head:
            return False

        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class Solution1:
    # 一个链表从头节点开始一个个删除，所谓删除就是让他的next指针指向他自己。
    # 如果没有环，从头结点一个个删除，最后肯定会删完，
    def hasCycle1(self, head):
        if not head:
            return False

        node = head
        while node:
            nodeNext = node.next
            if nodeNext == node:
                return True
            else:
                node.next = node
                node = nodeNext
        return False

    # 快慢节点
    def hasCycle2(self, head):
        if not head:
            return False

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(0)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node1
    node3.next = node1
    A = Solution1()
    print(A.hasCycle2(node1))
    # printListNode(A.hasCycle(node1))
    # printListNode(node1)
