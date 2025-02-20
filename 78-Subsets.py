class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(0, nums, [], ans)
        return ans
    
    def backtrack(self, start, nums, curr, ans):
        ans.append(curr[:])

        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.backtrack(i + 1, nums, curr, ans)
            curr.pop()
        
        