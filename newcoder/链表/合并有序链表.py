# -*- coding:utf-8 -*-
import sys

"""
将两个有序的链表合并为一个新链表，要求新的链表是通过拼接两个链表的节点来生成的，且合并后新链表依然有序。
示例1 输入：{1},{2} 返回值： {1,2}
示例2 输入：{2},{1} 返回值： {1,2}
"""


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
    def mergeTwoLists(self, l1, l2):
        # write code here
        listNodeRes = ListNode(-1)
        res = listNodeRes
        while l1 and l2:
            if l1.val < l2.val:
                listNodeRes.next = l1
                l1 = l1.next
            else:
                listNodeRes.next = l2
                l2 = l2.next
            listNodeRes = listNodeRes.next
        if l1:
            listNodeRes.next = l1
        else:
            listNodeRes.next = l2
        printListNode(res.next)
        return res.next


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2  # 终止条件，直到两个链表都空
        if not l2:
            return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


var = ("\n"
       "//(1,1):代表第一次进入递归函数，并且从第一个口进入，并且记录进入前链表的状态\n"
       "merge(1,1): 1->4->5->null, 1->2->3->6->null\n"
       "    merge(2,2): 4->5->null, 1->2->3->6->null\n"
       "    	merge(3,2): 4->5->null, 2->3->6->null\n"
       "    		merge(4,2): 4->5->null, 3->6->null\n"
       "    			merge(5,1): 4->5->null, 6->null\n"
       "    				merge(6,1): 5->null, 6->null\n"
       "    					merge(7): null, 6->null\n"
       "    					return l2\n"
       "    				l1.next --- 5->6->null, return l1\n"
       "    			l1.next --- 4->5->6->null, return l1\n"
       "    		l2.next --- 3->4->5->6->null, return l2\n"
       "    	l2.next --- 2->3->4->5->6->null, return l2\n"
       "    l2.next --- 1->2->3->4->5->6->null, return l2\n"
       "l1.next --- 1->1->2->3->4->5->6->null, return l1\n")

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node11 = ListNode(1)
    node21 = ListNode(2)
    node31 = ListNode(3)
    node41 = ListNode(6)
    node11.next = node21
    node21.next = node31
    node31.next = node41

    A = Solution()
    print(A.mergeTwoLists(node1, node11))
    # printListNode(A.hasCycle(node1))
    # printListNode(node1)
