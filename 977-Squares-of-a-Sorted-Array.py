class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = n - 1 
        neg = 0
        ans = [0] * n

        for i in range(n-1, -1, -1):
            if abs(nums[neg]) < abs(nums[pos]):
                square = nums[pos]
                pos -= 1
            else:
                square = nums[neg]
                neg += 1
            ans[i] = square * square
        return ans
