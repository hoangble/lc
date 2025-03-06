from collections import defaultdict
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)

        for word1, word2 in zip(words, words[1:]):
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c2].append(c1)
                    graph[c1]
                    break
            else:
                if len(word2) < len(word1):
                    return ""

        self.output = []
        seen = {}
        for node in graph:
            if not self.dfs(node, graph, seen):
                return ""
        return "".join(self.output)

    def dfs(self, node, reverse_adj_graph, seen):
        if node in seen:
            return seen[node]

        seen[node] = False
        for next_node in reverse_adj_graph[node]:
            result = self.dfs(next_node, reverse_adj_graph, seen)
            if not result:
                return False
        seen[node] = True
        self.output.append(node)
        return True


Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
