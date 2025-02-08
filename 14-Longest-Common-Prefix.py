class Node():
    def __init__(self):
        self.edges = {}
        self.end = False

class Solution:
    from collections import defaultdict
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # self.head = Node()

        # for word in strs:
        #     cur = self.head 
        #     for w in word:
        #         if w not in cur.edges:
        #             cur.edges[w] = Node()
        #         cur = cur.edges[w]
        #     cur.end = True
        
        # ans = \\
        # cur = self.head
        # while not cur.end:
        #     if len(cur.edges) > 1:
        #         return ans 
        #     for k, v in cur.edges.items():
        #         ans += k
        #     cur = cur.edges[k]
        
        # return ans
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''
        
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
