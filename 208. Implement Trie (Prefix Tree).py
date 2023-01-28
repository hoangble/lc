class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        tmp = self.head
        for c in word:
            if not c in tmp.edges:
                node = Node()
                tmp.edges[c] = node
            tmp = tmp.edges[c]
 
        tmp.is_end = True

    def search(self, word: str) -> bool:
        tmp = self.head
        for c in word:
            if c in tmp.edges:
                tmp = tmp.edges[c]
            else:
                return False
 
        return tmp.is_end
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.head
        for c in prefix:
            if c in tmp.edges:
                tmp = tmp.edges[c]
            else:
                return False
        return True

class Node():
    def __init__(self):
        self.is_end = False
        self.edges = {}
