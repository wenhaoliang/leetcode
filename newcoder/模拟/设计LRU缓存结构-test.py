class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
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
            self.size += 1
            self.addToHead(node)  # ?
            if self.size > self.capacity:
                removeNode = self.removeTail()
                self.size -= 1
                self.cache.pop(removeNode.key)
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        return None

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
        return None


if __name__ == "__main__":
    A = LRUCache(2)
    A.put(1, 1)
    A.put(2, 2)
    A.put(3, 3)
    A.put(4, 4)
    A.put(5, 5)
    for i in A.cache:
        print(A.cache[i].value)
