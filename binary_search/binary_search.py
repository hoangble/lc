class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right - 1:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else: # only if all numbers are unique
                return mid
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        else:
            return -1
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right - 1:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
            # else: # only if all numbers are unique
            #     return mid
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        else:
            return -1   
