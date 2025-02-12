class Node:
    def __init__(self, freq = -1, prev = None, next_ = None):
        self.freq = freq
        self.keys = set()
        self.prev = prev
        self.next_ = next_

class AllOne:
    def __init__(self):
        self.d = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {} # key: freq_node
        
    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            curr_freq = node.freq
            next_node = node.next
            node.keys.remove(key)
            if next_node == self.tail or next_node.freq != curr_freq + 1:
                # create a new node
                new_node = Node(freq = curr_freq + 1)
                new_node.keys.add(key)
                self.map[key] = new_node


                new_node.next = next_node
                next_node.prev = new_node
                node.next = new_node
                new_node.prev = node
            else:
                next_node.keys.add(key)
                self.map[key] = next_node

            if len(node.keys) == 0: 
                self.remove_node(node)
        else:
            next_node = self.head.next
            if next_node == self.tail or next_node.freq > 1:
                    new_node = Node(1, self.head)
                    new_node.keys.add(key)
                    self.map[key] = new_node

                    new_node.next = next_node
                    new_node.prev = self.head
                    next_node.prev = new_node
                    self.head.next = new_node 
            else:
                next_node.keys.add(key)
                self.map[key] = next_node

    def dec(self, key: str) -> None:
        if key not in self.map: return 

        node = self.map[key]
        node.keys.remove(key)
        if node.freq == 1:
            del self.map[key]
        else:
            prev_node = node.prev
            if prev_node is self.head or prev_node.freq != node.freq - 1:
                new_node = Node(freq = node.freq - 1)
                new_node.keys.add(key)
                new_node.next = prev_node.next
                new_node.prev = prev_node
                prev_node.next = new_node
                new_node.next.prev = new_node
                self.map[key] = new_node
            else:
                prev_node.keys.add(key)
                self.map[key] = prev_node
        if len(node.keys) == 0: 
            self.remove_node(node)

       
    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return \\
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return \\
        return next(iter(self.head.next.keys))

    def remove_node(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        del(node)

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()