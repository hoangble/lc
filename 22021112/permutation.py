class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.permute_helper(nums, [], [], len(nums), ans)
        return ans
    
    def permute_helper(self, nums, picked_idx, picked_nums, n, ans):
        if n == 0:
            ans.append(picked_nums.copy())
            return
        
        for i in range(len(nums)):
            if i not in picked_idx:
                picked_idx.append(i)
                picked_nums.append(nums[i])
                self.permute_helper(nums, picked_idx, picked_nums, n-1, ans)
                picked_nums.pop()
                picked_idx.pop()

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.permute_helper(0, nums, ans)
        return ans
    
    def permute_helper(self, start, nums, ans):
        if start == len(nums):            
            ans.append(nums.copy())
            return 
        
        for i in range(start, len(nums)):
            self.swap(nums, start, i)
            self.permute_helper(start+1, nums, ans)
            self.swap(nums, i, start)
            
    
    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b] 
        nums[b] = tmp
        
        # nums[a] = nums[a] + nums[b]
        # nums[b] = nums[a]- nums[b]
        # nums[a] = nums[a] - nums[b]

#%%
x = 0
sign = [1,-1][x<0]
print(sign)