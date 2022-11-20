class Solution:
    from collections import Counter
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        num_freq = Counter(candidates)
        all_nums = list(num_freq.keys())
        self.combination_sum_helper(0, all_nums, num_freq, [], target, ans)
        return ans
    
    def combination_sum_helper(self, start, all_nums, num_freq, curr_pick, target_sum, ans):
        if target_sum < 0: return 
        if target_sum == 0: ans.append(curr_pick.copy())
            
        for i in range(start, len(all_nums)):
            num_ = all_nums[i]
            cnt_ = num_freq[num_]
            print(num_, cnt_)
            if cnt_ > 0: 
                curr_pick.append(num_)
                num_freq[num_] -= 1
                self.combination_sum_helper(i, all_nums, num_freq, curr_pick, target_sum - num_, ans)
                curr_pick.pop()
                num_freq[num_] += 1
                