# https://leetcode.com/problems/longest-common-prefix/submissions/895809606/


class Node:
    def __init__(self):
        self.edges = {}
        self.end = False


class Solution:
    from collections import defaultdict

    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.head = Node()

        for word in strs:
            cur = self.head
            for w in word:
                if w not in cur.edges:
                    cur.edges[w] = Node()
                cur = cur.edges[w]
            cur.end = True

        ans = ""
        cur = self.head
        while not cur.end:
            if len(cur.edges) > 1:
                return ans
            for k, v in cur.edges.items():
                ans += k
            cur = cur.edges[k]

        return ans
