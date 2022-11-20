class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.permute_helper(nums, [], [], len(nums), ans)
        return ans
    
    def permute_helper(self, nums, picked_idx, picked_nums, n, ans):
        if n == 0 and picked_nums not in ans:
            ans.append(picked_nums.copy())
            return
        
        for i in range(len(nums)):
            if i not in picked_idx:
                picked_idx.append(i)
                picked_nums.append(nums[i])
                self.permute_helper(nums, picked_idx, picked_nums, n-1, ans)
                picked_nums.pop()
                picked_idx.pop()

# a better solution
class Solution:
    from collections import Counter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        num_freq = Counter(nums)
        all_nums = list(num_freq.keys())
        self.permute_helper(num_freq, all_nums, 0, [], len(nums), ans)
        return ans
    
    def permute_helper(self, num_freq, all_nums, start, picked_nums, n, ans):
        if n == 0:
            ans.append(picked_nums.copy())
            return
        
        for i in range(len(num_freq)):
            num_ = all_nums[i]
            cnt_ = num_freq[num_]
            if cnt_ > 0:
                num_freq[num_] -= 1
                picked_nums.append(all_nums[i])
                self.permute_helper(num_freq, all_nums, i, picked_nums, n - 1, ans)
                picked_nums.pop()
                num_freq[num_] += 1
