class Node():
    def __init__(self, end = False):
        self.edge = {}
        self.end = end

class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr =  self.head
        for c in word:
            if c not in curr.edge:
                curr.edge[c] = Node()
            curr = curr.edge[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr =  self.head
        for c in word:
            if c not in curr.edge:
                return False
            curr = curr.edge[c]
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr.edge:
                return False
            curr = curr.edge[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)