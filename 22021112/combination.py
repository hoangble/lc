class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.pick_num(1, [], k, n, ans)
        return ans
    
    def pick_num(self, start_idx, picked_nums, k, n , ans):
        if k == 0:
            ans.append(picked_nums.copy())
            return 
        
        for i in range(start_idx, n+1):
            picked_nums.append(i)
            self.pick_num(i + 1,  picked_nums, k-1, n , ans)
            picked_nums.pop()
