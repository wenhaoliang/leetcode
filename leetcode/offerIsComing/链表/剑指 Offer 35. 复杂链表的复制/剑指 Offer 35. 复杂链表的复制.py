"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。

链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
"""
import sys


def printListNode(head):
    if head is None:
        sys.stdout.write("{}")
        return
    current = head
    sys.stdout.write("List: {")
    while current:
        if current == head:
            sys.stdout.write("%d" % current.val)
        else:
            sys.stdout.write(",%d" % current.val)
        current = current.next

    sys.stdout.write("}")
    print()


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next, default=None)
            dic[cur].random = dic.get(cur.random, default=None)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]


if __name__ == "__main__":
    """
    输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
    """
    A = Solution()
    a1 = Node(7)
    a2 = Node(13)
    a3 = Node(11)
    a4 = Node(10)
    a5 = Node(1)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    a1.random = None
    a2.random = a1
    a3.random = a5
    a4.random = a3
    a5.random = a1

    A.copyRandomList(a1)

    # dict['key']只能获取存在的值，如果不存在则触发KeyError
    # 而dict.get(key, default=None)则如果不存在则返回一个默认值，如果设置了则是设置的，否则就是None
    dict = {'Name': 'Runoob', 'Age': 27, }
    print("Value : %s" % dict.get('Age'))
    print("Value : %s" % dict['Age'])
    print("Value : %s" % dict.get('A'))
    # print("Value : %s" % dict['A'])
    print("Value : %s" % dict.get('Sex', "Not Available"))
