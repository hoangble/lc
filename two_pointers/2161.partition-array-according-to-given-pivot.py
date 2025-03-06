from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        smaller_i = 0
        greater_i = n - 1

        ans = [0] * n
        for i, j in zip(range(n), range(n - 1, -1, -1)):
            if nums[i] < pivot:
                ans[smaller_i] = nums[i]
                smaller_i += 1

            if nums[j] > pivot:
                ans[greater_i] = nums[j]
                greater_i -= 1

        while smaller_i <= greater_i:
            ans[smaller_i] = pivot
            smaller_i += 1

        return ans
