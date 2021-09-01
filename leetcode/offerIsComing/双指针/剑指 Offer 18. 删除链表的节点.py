"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
注意：此题对比原题有改动
示例 1:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        if head.val == val:
            return head.next

        pre, cur = head, head.next

        while cur and cur.val != val:
            pre, cur = cur, cur.next

        if cur:
            pre.next = cur.next

        return head


class Solution1:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head or head.val == val:
            return head

        pre, cur = head, head.next

        while cur and cur.val != val:
            pre, cur = cur, cur.next

        if cur:
            pre.next = cur.next
        return head


if __name__ == "__main__":
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(1)
    n4 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    val = 10
    # A = Solution()
    # print(A.deleteNode(n1, val))
    A = Solution1()
    print(A.deleteNode(n1, val))
