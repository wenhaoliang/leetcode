"""
运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value)如果关键字已经存在，则变更其数据值；
如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
进阶：你是否可以在O(1) 时间复杂度内完成这两种操作？
示例：输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出[null, null, null, 1, null, -1, null, -1, 3, 4]
解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
链接：https://leetcode-cn.com/problems/lru-cache
"""


# class DLinkNode:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.next = None
#         self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.size = 0
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            node = DLinkNode(key, value)
            self.cache[key] = node
            print('cache:', self.cache)
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removedNode = self.removeTail()
                self.cache.pop(removedNode.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)


class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkNode(key, value)
            self.cache[key] = node
            self.size += 1
            self.addToHead(node)
            if self.size > self.capacity:
                removeNode = self.removeTail()
                self.cache.pop(removeNode.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)


if __name__ == "__main__":
    # a = ["LRUCache", "put",  "put",  "get", "put",   "get", "put",   "get", "get", "get"]
    # b = [[2],        [1, 1], [2, 2], [1],    [3, 3], [2],    [4, 4], [1],   [3],    [4]]
    # ["LRUCache", "put", "put", "get", "put", "put", "get"]
    # [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
    A = LRUCache1(2)
    A.put(1, 1)
    A.put(2, 2)
    A.put(3, 3)
    A.put(4, 10)
    A.put(5, 5)
    print('A.get(1):', A.get(1))
    print('A.get(2):', A.get(2))
    print('A.get(3):', A.get(3))
    print('A.get(4):', A.get(4))
    print('A.get(5):', A.get(5))
    for i in A.cache:
        print('i:', A.cache[i].value)
    A = LRUCache(2)
    A.put(1, 1)
    A.put(2, 2)
    A.put(3, 3)
    A.put(4, 10)
    A.put(5, 5)
    print('A.get(1):', A.get(1))
    print('A.get(2):', A.get(2))
    print('A.get(3):', A.get(3))
    print('A.get(4):', A.get(4))
    print('A.get(5):', A.get(5))
    for i in A.cache:
        print('i:', A.cache[i].value)
