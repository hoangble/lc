# https://github.com/hoangle96/lc/new/main/union_find

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

        # sort logs by time
        logs = sorted(logs, key= lambda x: x[0])
        # print(logs)
        n_components = n
        for log in logs:
            time, x, y = log
            if self.union(x, y): n_components -= 1
            # print(n_components, time, x, y, self.parent)
            if n_components == 1: return time
        
        return -1
    
    def find(self, node) -> int:
        if node == self.parent[node]: return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] <= self.rank[parent_y]:
                self.parent[parent_x] = self.parent[parent_y]
                self.rank[parent_y] += self.rank[parent_x]
            else:
                self.parent[parent_y] = self.parent[parent_x]
                self.rank[parent_x] += self.rank[parent_y]
            return True
        return False
