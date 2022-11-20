class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.combination_sum_helper(0, candidates, [], target, ans)
        return ans
        
    def combination_sum_helper(self, start, candidates, curr_pick, target_sum, ans):
        if target_sum < 0: return
        if target_sum == 0: ans.append(curr_pick.copy())
            
        for i in range(start, len(candidates)):
            curr_pick.append(candidates[i])
            self.combination_sum_helper(i, candidates, curr_pick, target_sum - candidates[i], ans)
            curr_pick.pop()