# -*- coding:utf-8 -*-
"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。
输入描述：输入分为2段，第一段是入环前的链表部分，第二段是链表环的部分，后台将这2个会组装成一个有环或者无环单链表
返回值描述：返回链表的环的入口结点即可。而我们后台程序会打印这个节点
示例1 输入： {1,2},{3,4,5} 返回值：3 
说明：返回环形链表入口节点，我们后台会打印该环形链表入口节点，即3    
示例2 输入： {1},{}        返回值："null" 
说明：没有环，返回null，后台打印"null" 
示例3 输入： {},{2}        返回值：2
说明：
只有环形链表节点2，返回节点2，后台打印2   
"""
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        # write code here
        if head is None:
            return
        slow, quick = head, head
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                break
        if not quick or not quick.next:
            return
        quick = head
        while slow != quick:
            slow = slow.next
            quick = quick.next

        return quick


class Solution1:
    def detectCycle(self, head):
        if not head:
            return

        slow, quick = head, head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if slow == quick:
                break
        if not quick or not quick.next:
            return
        quick = head
        while quick != slow:
            slow = slow.next
            quick = quick.next
        return quick

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
    """
    
    快指针走了n(n >= 1)圈后与慢指针相遇，
    固有：
    2(A + B) = n(B+C)+B+A
    A = nC+(n-1)B
    A = C + (n-1)(C+B)
    因为C+B为一圈的长度，所以用c， h两个指针从p点和head开始走，当h走完A时，c走过的路为C + (n-1)(C+B)，即n圈+C，所以h和c的相遇点为q
    """
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3
    A = Solution()
    print(A.detectCycle(node1))
    # printListNode(node1)
    printListNode(A.detectCycle(node1))
    # printListNode(node1)
