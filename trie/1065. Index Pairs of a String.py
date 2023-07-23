from typing import List

class Node:
    def __init__(self):
        self.end = False
        self.edges = {}
    
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # build trie for words

        self.head = Node()
        for word in words:
            cur = self.head
            for w in word:
                if w not in cur.edges:
                    cur.edges[w] = Node()
                cur = cur.edges[w]
            cur.end = True

        ans = []
        for l in range(len(text)):
            cur = self.head

            for r in range(l, len(text)):
                if text[r] not in cur.edges:
                    break
                cur = cur.edges[text[r]]
                if cur.end:
                    ans.append([l, r])
        
        # sorted(ans, key = lambda x: x[0])
        return ans
        

        