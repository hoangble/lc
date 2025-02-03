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

        # iterate backward
        i, j, p = m - 1, n - 1, len(nums1) - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        return nums1
