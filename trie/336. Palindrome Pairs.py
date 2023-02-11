# https://leetcode.com/problems/palindrome-pairs/solutions/1987826/python-trie-solution-explained/?languageTags=python3

class Node():
    def __init__(self):
        self.edges = {}
        self.idx = -1
        self.palindrome_idx = []

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.head = Node()
        
        for i, word in enumerate(words):
            rev_word = word[::-1]

            tmp = self.head
            for j, w in enumerate(rev_word):
                if self.is_palindrome(rev_word[j:]):
                    tmp.palindrome_idx.append(i) # the current prefix from j is a palindrome

                if w not in tmp.edges:
                    tmp.edges[w] = Node()

                tmp = tmp.edges[w]

            tmp.idx = i

        ans = []
        for i in range(len(words)):
            self.check_palindrome(words[i], i, ans)

        return ans
    
    def check_palindrome(self, word, idx, ans):
        node = self.head

        # if word < trie
        for i, w in enumerate(word):
            if node.idx > -1 and self.is_palindrome(word[i:]): 
                ans.append([idx, node.idx])

            if not w in node.edges: 
                return

            node = node.edges[w]

        # if word == trie:
        if node.idx > -1 and idx != node.idx: ans.append([idx, node.idx])
        
        # if word > trie
        for i in node.palindrome_idx:
            ans.append([idx, i])
        return

    def is_palindrome(self, str_):
        return str_[::-1] == str_
