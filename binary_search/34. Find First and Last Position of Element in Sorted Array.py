class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search

        ans = [-1, -1]
        if len(nums) == 0:
            return ans

        # do 2 binary search, one for left end, one for right end

        # with left end, it's equivalent to find the first match
        left, right = 0, len(nums) - 1  # -> l, r are indices
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:  # condition(mid):
                right = mid
            else:
                left = mid + 1
            # print(mid, left, right)

        if nums[left] != target:
            left = -1
        ans[0] = left

        # print("right")

        # with right end, it's equivalent to find the last match
        # left, right = 0, len(nums) # -> l, r are indices
        left, right = 0, len(nums) - 1  # -> l, r are indices
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:  # condition(mid):
                right = mid - 1
            else:
                left = mid + 1
            # print(mid, left, right)

        if nums[right] != target:
            right = -1
        ans[-1] = right

        return ans


# %%
import math

print(math.sqrt(4).is_integer())
