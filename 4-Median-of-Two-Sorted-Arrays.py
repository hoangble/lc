class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m = len(nums1)
        n = len(nums2)

        # m <= n
        l, r = 0, m
        while l <= r:
            m_A = (l + r) //  2
            m_B = (m + n + 1) // 2 - m_A
        
            max_left_a = -float('inf') if m_A == 0 else nums1[m_A - 1]
            min_right_a = float('inf') if m_A == m else nums1[m_A]
            max_left_b = -float('inf') if m_B == 0 else nums2[m_B - 1]
            min_right_b = float('inf') if m_B == n else nums2[m_B]

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m + n) % 2 == 1:
                    return max(max_left_a, max_left_b)
                else:
                    return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2
            
            if max_left_a > min_right_b:
                r = m_A - 1
            else:
                l = m_A + 1
        return 0