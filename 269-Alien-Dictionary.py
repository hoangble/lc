class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.adj = defaultdict(set)
        self.in_deg = defaultdict(int)
        for word in words:
            for c in word:
                self.in_deg[c]
        
        # step 1: build adj graph
        # for word1, word2 in zip(words, words[1:]):
        #     for c, d in zip(word1, word2):
        #         if c != d and c not in self.adj[d]:
        #             self.adj[c].add(d)
        #             self.in_deg[c] += 1
        #     else:
        #         if len(word2) < len(word1):
        #             return ''
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in self.adj[c]:
                        self.adj[c].add(d)
                        self.in_deg[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return \\

    
        output = []
        q = deque([c for c in self.in_deg if self.in_deg[c] == 0])
        # print(q)
        while q:
            curr = q.popleft()
            output.append(curr)
            for c in self.adj[curr]:
                self.in_deg[c] -= 1
                if self.in_deg[c] == 0:
                    q.append(c)
        
        if len(output) < len(self.in_deg): return ''
        return ''.join(output)

