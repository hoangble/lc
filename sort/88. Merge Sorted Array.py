from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1

        p = len(nums1) - 1
        i = m - 1
        j = n - 1

        while i >= 0:
            if j >= 0 and nums2[j] >= nums1[i]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
        return nums1


sol = Solution()
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
