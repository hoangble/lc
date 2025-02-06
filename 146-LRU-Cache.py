class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cnt = 0
        self.d = {} # key: node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        # fetch key
        node = self.d[key]

        # rotate it to the back
        self.remove(node)
        self.move(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # make a node 
        if key in self.d:
            to_remove = self.d[key]
            self.remove(to_remove)
            del(self.d[key])

        node = Node(key, value)
        self.move(node)
        self.d[key] = node

        # if over capacity, remove the node from beginning
        if len(self.d) > self.cap:
            to_remove = self.head.next
            self.remove(to_remove)
            del(self.d[to_remove.key])

    def move(self, node):
        # put node to the end
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)