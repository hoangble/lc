from typing import List 

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        t = 0
        ans = 0
        time_tracker = [0] * len(edges)

        for i in range(len(edges)):
            if time_tracker[i] > 0: continue

            u = i
            start_time = t
            while u != -1 and time_tracker[u] == 0:
                time_tracker[u] = t
                t += 1
                u = edges[u]
            if u != -1 and time_tracker[u] >= start_time:
                ans = max(ans, t - time_tracker[u])
        return ans if ans > 0 else -1
    
        # in_stack = [False] * len(edges)
        # step_track = [0] * len(edges)

        # ans = 0

        # for i in range(len(edges)):
        #     if in_stack[i]: continue
        #     step_track = [0] * len(edges)
        #     in_stack = [False] * len(edges)
        #     curr_len = self.dfs(i, edges, in_stack, step_track, 0)
        #     ans = max(ans, curr_len)
        # return ans if ans > 0 else -1

    # def dfs(self, node, edges, in_stack, step_track, step) -> int:
    #     # if this node doesnt lead any where return 0
    #     if edges[node] == -1: return 0

    #     # if the node is just in stack, put the cycle track to true in the 2nd visit
    #     if in_stack[node] and step_track[node] > 0: return step - step_track[node]

    #     if in_stack[node]: return 0

    #     in_stack[node] = True
    #     step_track[node] = step
    #     next_node = edges[node]
        
    #     return self.dfs(next_node, edges, in_stack, step_track, step + 1)        

if __name__ == "__main__":
    edges = [1,2,0,4,5,6,3,8,9,7]
    sol = Solution()
    print(sol.longestCycle(edges=edges))