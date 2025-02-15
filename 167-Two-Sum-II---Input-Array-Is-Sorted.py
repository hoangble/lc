class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
        

