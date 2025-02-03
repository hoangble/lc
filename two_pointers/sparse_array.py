from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = []
        for i, n in enumerate(nums):
            if n != 0:
                self.non_zeros.append((i, n))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        i = j = 0
        this_vec = self.non_zeros
        that_vec = vec.non_zeros
        ans = 0
        while i < len(this_vec) and j < len(that_vec):
            if this_vec[i][0] == that_vec[j][0]:
                ans += this_vec[i][1] * that_vec[j][1]
                i += 1
                j += 1
            elif this_vec[i][0] > that_vec[j][0]:
                j += 1
            else:
                i += 1
        return ans


# Your SparseVector object will be instantiated and called as such:
nums1 = [0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0]
nums2 = [0, 0, 2, 0, 0, 4, 3, 0, 0, 2, 0, 0, 0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
